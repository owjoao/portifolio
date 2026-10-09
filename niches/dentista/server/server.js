/**
 * ==============================================================================
 * LUMINA OS - SECURE BACKEND API GATEWAY & AUTHENTICATION SERVER
 * Arquitetura de Isolamento de Infraestrutura & Cyber Security
 * ==============================================================================
 */

const express = require('express');
const cors = require('cors');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');

// Carregamento de variáveis de ambiente
const PORT = process.env.PORT || 3001;
const NODE_ENV = process.env.NODE_ENV || 'development';
const SUPABASE_URL = process.env.SUPABASE_URL || '';
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || '';
const ADMIN_SECRET_PIN = process.env.ADMIN_SECRET_PIN || '948210';
const JWT_SECRET = process.env.JWT_SECRET || 'lumina_default_dev_secret_key_change_in_prod';
const JWT_EXPIRES_IN = process.env.JWT_EXPIRES_IN || '8h';

const rawAllowedOrigins = process.env.ALLOWED_ORIGINS || 'http://localhost:8080,http://127.0.0.1:8080';
const allowedOrigins = rawAllowedOrigins.split(',').map(o => o.trim());

const app = express();

// ============================================================================
// 1. HARDENING DE CABEÇALHOS HTTP (SECURITY HEADERS)
// ============================================================================
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  res.setHeader('Content-Security-Policy', "default-src 'self'; frame-ancestors 'none';");
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  res.removeHeader('X-Powered-By');
  next();
});

// ============================================================================
// 2. ISOLAMENTO DE ORIGEM (STRICT CORS POLICY)
// ============================================================================
app.use(cors({
  origin: function(origin, callback) {
    // Permite requisições sem origin (como mobile apps, curl ou scripts locais autorizados)
    if (!origin || allowedOrigins.indexOf(origin) !== -1 || allowedOrigins.includes('*')) {
      callback(null, true);
    } else {
      callback(new Error('Origem não permitida pela política de segurança CORS da clínica.'));
    }
  },
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true
}));

app.use(express.json({ limit: '100kb' })); // Mitiga ataques de Payload Denial of Service

// ============================================================================
// 3. PROTEÇÃO CONTRA FORÇA BRUTA (IN-MEMORY RATE LIMITING)
// ============================================================================
const failedLoginAttempts = new Map();

function loginRateLimiter(req, res, next) {
  const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || 'unknown';
  const now = Date.now();
  const windowMs = 15 * 60 * 1000; // 15 minutos
  const maxAttempts = 5;

  const userAttempts = failedLoginAttempts.get(ip) || { count: 0, resetTime: now + windowMs };

  if (now > userAttempts.resetTime) {
    userAttempts.count = 0;
    userAttempts.resetTime = now + windowMs;
  }

  if (userAttempts.count >= maxAttempts) {
    const minutesLeft = Math.ceil((userAttempts.resetTime - now) / 60000);
    return res.status(429).json({
      error: 'Excesso de tentativas incorretas.',
      message: `Bloqueio de segurança temporário ativado. Tente novamente em ${minutesLeft} minutos.`
    });
  }

  req.clientIp = ip;
  req.attemptsRecord = userAttempts;
  next();
}

// ============================================================================
// 4. CLIENTE SUPABASE PRIVILEGIADO (SERVER-SIDE SERVICE_ROLE)
// ============================================================================
let supabaseServerClient = null;
if (SUPABASE_URL && SUPABASE_SERVICE_ROLE_KEY) {
  try {
    const { createClient } = require('@supabase/supabase-js');
    supabaseServerClient = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, {
      auth: { persistSession: false }
    });
    console.log('✓ Conexão privilegiada com Supabase (service_role) inicializada com sucesso.');
  } catch (err) {
    console.warn('Aviso: @supabase/supabase-js não instalado ou credenciais pendentes. Operando em modo seguro simulado.');
  }
}

// ============================================================================
// 5. MIDDLEWARE DE AUTENTICAÇÃO JWT (RBAC)
// ============================================================================
function requireAdminAuth(req, res, next) {
  const authHeader = req.headers['authorization'];
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({
      error: 'Unauthorized',
      message: 'Token de autenticação obrigatório ausente ou em formato inválido.'
    });
  }

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.adminUser = decoded;
    next();
  } catch (err) {
    return res.status(401).json({
      error: 'Unauthorized',
      message: 'Sessão expirada ou assinatura de token inválida.'
    });
  }
}

// ============================================================================
// 6. ROTAS DE AUTENTICAÇÃO COM COMPARAÇÃO TIMING-SAFE
// ============================================================================

/**
 * POST /api/auth/login
 * Valida o PIN sem enumeração e usando comparação de tempo constante para mitigar Timing Attacks.
 */
app.post('/api/auth/login', loginRateLimiter, (req, res) => {
  const { pin } = req.body || {};

  if (!pin || typeof pin !== 'string') {
    return res.status(400).json({ error: 'Bad Request', message: 'Parâmetro PIN ausente.' });
  }

  // Prepara buffers de tamanho fixo para timingSafeEqual
  const expectedBuffer = Buffer.from(String(ADMIN_SECRET_PIN));
  const candidateBuffer = Buffer.from(String(pin));

  let isValid = false;
  if (expectedBuffer.length === candidateBuffer.length) {
    isValid = crypto.timingSafeEqual(expectedBuffer, candidateBuffer);
  }

  if (!isValid) {
    // Incrementa contagem de falhas para mitigar força bruta
    req.attemptsRecord.count += 1;
    failedLoginAttempts.set(req.clientIp, req.attemptsRecord);

    // Resposta genérica e uniforme (mitiga ataques de enumeração)
    return res.status(401).json({
      error: 'Unauthorized',
      message: 'Credenciais inválidas ou acesso não autorizado.'
    });
  }

  // Sucesso: Zera contadores de falha
  failedLoginAttempts.delete(req.clientIp);

  // Emite token JWT de curta/média duração
  const token = jwt.sign(
    {
      sub: 'admin-clinical-session',
      role: 'clinical_administrator',
      cro: '128.490',
      clinic: 'Lumina Odontologia'
    },
    JWT_SECRET,
    { expiresIn: JWT_EXPIRES_IN }
  );

  return res.status(200).json({
    success: true,
    message: 'Autenticação bem-sucedida.',
    token,
    expiresIn: JWT_EXPIRES_IN,
    user: {
      name: 'Marina Costa',
      role: 'Sócia administradora',
      cro: 'CRO 128.490'
    }
  });
});

// ============================================================================
// 7. ROTAS PROTEGIDAS DO CRM (ACESSO EXCLUSIVO DO ADMIN)
// ============================================================================

/**
 * GET /api/appointments
 * Puxa todos os pacientes via service_role contornando o RLS estrito com segurança.
 */
app.get('/api/appointments', requireAdminAuth, async (req, res) => {
  if (!supabaseServerClient) {
    return res.status(200).json({
      mode: 'mock_server_mode',
      leads: []
    });
  }

  try {
    const { data, error } = await supabaseServerClient
      .from('leads')
      .select('*')
      .order('created_at', { ascending: false });

    if (error) throw error;
    return res.status(200).json({ success: true, count: data.length, leads: data });
  } catch (err) {
    console.error('Erro na consulta administrativa:', err);
    return res.status(500).json({ error: 'Internal Server Error', message: 'Erro seguro de consulta ao banco.' });
  }
});

/**
 * PUT /api/appointments/:id/stage
 * Atualiza o status/fase do paciente no funil com validação estrita.
 */
app.put('/api/appointments/:id/stage', requireAdminAuth, async (req, res) => {
  const { id } = req.params;
  const { stage } = req.body;

  const validStages = ['new', 'scheduled', 'proposal', 'closed'];
  if (!validStages.includes(stage)) {
    return res.status(400).json({ error: 'Bad Request', message: 'Fase de funil inválida.' });
  }

  if (!supabaseServerClient) {
    return res.status(200).json({ success: true, mode: 'mock_mode', id, stage });
  }

  try {
    const { data, error } = await supabaseServerClient
      .from('leads')
      .update({ stage })
      .eq('id', id)
      .select();

    if (error) throw error;
    return res.status(200).json({ success: true, updated: data });
  } catch (err) {
    console.error('Erro ao atualizar estágio:', err);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// ============================================================================
// 8. ROTA PÚBLICA DE AGENDAMENTO (PUBLIC INTAKE COM SANITIZAÇÃO)
// ============================================================================
app.post('/api/appointments/public', async (req, res) => {
  const { name, phone, proc, day, date, time, val } = req.body || {};

  // Sanitização estrita contra XSS e SQL Injection
  if (!name || typeof name !== 'string' || name.length > 80) {
    return res.status(400).json({ error: 'Bad Request', message: 'Nome inválido.' });
  }

  const cleanName = name.replace(/[<>'"]/g, '').trim();
  const cleanPhone = String(phone || '').replace(/[^\d()+\-\s]/g, '').substring(0, 20);
  const cleanProc = String(proc || 'Consulta Geral').replace(/[<>'"]/g, '').substring(0, 50);

  const newLead = {
    id: 'lead-' + Date.now(),
    name: cleanName,
    phone: cleanPhone,
    proc: cleanProc,
    day: String(day || 'Hoje').substring(0, 20),
    date: String(date || new Date().toISOString().split('T')[0]).substring(0, 10),
    time: String(time || '10:00').substring(0, 10),
    val: String(val || 'R$ 0,00').substring(0, 20),
    stage: 'new',
    origin: 'Site Público (API Gateway)'
  };

  if (!supabaseServerClient) {
    return res.status(201).json({ success: true, message: 'Agendamento registrado com sucesso.', leadId: newLead.id });
  }

  try {
    const { data, error } = await supabaseServerClient.from('leads').insert([newLead]).select();
    if (error) throw error;
    return res.status(201).json({ success: true, message: 'Agendamento registrado com sucesso.', lead: data[0] });
  } catch (err) {
    console.error('Erro ao inserir agendamento:', err);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Fallback de rota desconhecida
app.use((req, res) => {
  res.status(404).json({ error: 'Not Found', message: 'Endpoint seguro inexistente.' });
});

// Inicia servidor se executado diretamente
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`=======================================================`);
    console.log(` 🛡️  LUMINA OS - SECURE API GATEWAY INICIADO`);
    console.log(` Porta: ${PORT} | Modo: ${NODE_ENV}`);
    console.log(` Origens permitidas: ${allowedOrigins.join(', ')}`);
    console.log(`=======================================================`);
  });
}

module.exports = app;
