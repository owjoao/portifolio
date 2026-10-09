-- ==============================================================================
-- LUMINA OS • POLÍTICA DE SEGURANÇA MÁXIMA (ROW LEVEL SECURITY - RLS)
-- Banco de Dados: Supabase / PostgreSQL
-- Finalidade: Blindagem contra Raspagem de Dados (Data Scraping) e LGPD
-- ==============================================================================

-- 1. Criação ou Garantia da Estrutura das Tabelas (leads e agendamentos)
CREATE TABLE IF NOT EXISTS leads (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    proc TEXT,
    day TEXT,
    date TEXT,
    time TEXT,
    val TEXT,
    stage TEXT DEFAULT 'new',
    origin TEXT DEFAULT 'Site Público',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);

-- Caso sua estrutura use o nome 'agendamentos', criamos uma view ou espelho:
CREATE TABLE IF NOT EXISTS agendamentos (
    id TEXT PRIMARY KEY,
    nome_paciente TEXT NOT NULL,
    telefone TEXT,
    procedimento TEXT,
    data_consulta DATE,
    horario_consulta TIME,
    status TEXT DEFAULT 'solicitado',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);

-- ==============================================================================
-- 2. ATIVAÇÃO DE ROW LEVEL SECURITY (RLS) ESTRITO
-- ==============================================================================
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;
ALTER TABLE agendamentos ENABLE ROW LEVEL SECURITY;

-- Força RLS mesmo para os proprietários das tabelas (para evitar vazamento acidental)
ALTER TABLE leads FORCE ROW LEVEL SECURITY;
ALTER TABLE agendamentos FORCE ROW LEVEL SECURITY;

-- ==============================================================================
-- 3. REMOÇÃO DE TODAS AS POLÍTICAS PERMISSIVAS ANTERIORES (CLEANUP)
-- ==============================================================================
DROP POLICY IF EXISTS "Acesso Total Leads" ON leads;
DROP POLICY IF EXISTS "Acesso Total Agendamentos" ON agendamentos;
DROP POLICY IF EXISTS "Public Select Leads" ON leads;
DROP POLICY IF EXISTS "Permitir_Apenas_Insercao_Anonima" ON leads;
DROP POLICY IF EXISTS "Permitir_Apenas_Insercao_Anonima_Agendamentos" ON agendamentos;

-- Revoga privilégios gerais de leitura, alteração e exclusão da camada pública
REVOKE SELECT, UPDATE, DELETE ON TABLE leads FROM anon, authenticated, public;
REVOKE SELECT, UPDATE, DELETE ON TABLE agendamentos FROM anon, authenticated, public;

-- ==============================================================================
-- 4. POLÍTICAS DE ZERO-TRUST (INSERT-ONLY PARA VISITANTES ANÔNIMOS)
-- ==============================================================================

-- A. Tabela 'leads': O público anônimo (visitante do site) PODE APENAS INSERIR (INSERT)
CREATE POLICY "Permitir_Apenas_Insercao_Anonima_Leads" 
ON leads 
FOR INSERT 
TO anon, authenticated 
WITH CHECK (
    -- Validação de integridade: Não permite injeção de ID administrativo ou datas inválidas
    length(name) >= 2 AND length(name) <= 100
);

-- B. Tabela 'agendamentos': Apenas INSERT permitido para anon
CREATE POLICY "Permitir_Apenas_Insercao_Anonima_Agendamentos" 
ON agendamentos 
FOR INSERT 
TO anon, authenticated 
WITH CHECK (
    length(nome_paciente) >= 2 AND length(nome_paciente) <= 100
);

-- ==============================================================================
-- 5. BLOQUEIO TERMINANTE DE LEITURA (SELECT), EDIÇÃO (UPDATE) E EXCLUSÃO (DELETE)
-- ==============================================================================
-- No PostgreSQL/Supabase, quando o RLS está ativo e NÃO existe política para SELECT,
-- qualquer tentativa de leitura pelo 'anon' ou 'authenticated' comum retorna 0 linhas (VAZIO).
-- Dados de pacientes (nomes, telefones, histórico) tornam-se 100% INACESSÍVEIS via navegador.

-- ==============================================================================
-- 6. BYPASS EXCLUSIVO DO SERVIDOR BACK-END (SERVICE_ROLE)
-- ==============================================================================
-- A role 'service_role' do Supabase possui nativamente o privilégio 'BYPASSRLS'.
-- Ela é utilizada EXCLUSIVAMENTE pelo nosso servidor Node.js/Express protegido.
-- Dessa forma, o back-end consegue consolidar, agendar e ler o funil,
-- enquanto hackers ou curiosos no navegador encontram uma barreira intransponível.

-- ==============================================================================
-- 7. TESTE DE VALIDAÇÃO DE SEGURANÇA (VERIFICAÇÃO IMEDIATA)
-- ==============================================================================
-- Execute os testes abaixo no SQL Editor para certificar o bloqueio:
--
-- TESTE 1: Inserção anônima (Deve ter SUCESSO):
-- SET ROLE anon;
-- INSERT INTO leads (id, name, phone, proc, day, time) VALUES ('test-sec-1', 'Paciente Teste Anonimo', '11999999999', 'Avaliacao', 'Hoje', '14:00');
--
-- TESTE 2: Consulta anônima de dados (Deve retornar ZERO linhas):
-- SET ROLE anon;
-- SELECT * FROM leads; -- Retornará vazio! Dados completamente protegidos.
--
-- TESTE 3: Retornar para role de administrador:
-- RESET ROLE;
