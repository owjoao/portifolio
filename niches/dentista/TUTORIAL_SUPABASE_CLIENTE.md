# 🚀 Guia Rápido de Configuração: Conexão em Nuvem (Supabase)
**Sistema Lumina OS • Gestão & CRM Clínico**

Este guia foi elaborado para você ou seu cliente realizarem a ativação da sincronização em nuvem em menos de **3 minutos**, sem necessidade de conhecimentos técnicos.

---

## 📋 Passo 1: Criar a Conta Gratuita no Supabase
1. Acesse o site oficial: [https://supabase.com](https://supabase.com)
2. Clique no botão verde **"Start your project"**.
3. Faça login usando sua conta do **Google**, **GitHub** ou **E-mail**.

---

## 🏢 Passo 2: Criar o Projeto da Clínica
1. No painel inicial, clique no botão **"New Project"**.
2. Preencha os campos simples:
   * **Name**: Digite o nome da clínica (ex: `Clinica-Lumina`).
   * **Database Password**: Crie uma senha segura (anote em local seguro).
   * **Region**: Selecione **São Paulo (sa-east-1)** para garantir a menor latência e velocidade ultrarrápida no Brasil.
3. Clique em **"Create new project"**.
4. Aguarde cerca de 1 a 2 minutos enquanto o Supabase prepara o banco de dados na nuvem.

---

## ⚡ Passo 3: Criar a Tabela com 1 Clique (SQL Editor)
1. No menu lateral esquerdo do Supabase, clique no ícone **SQL Editor** (parece um terminal `>_`).
2. Clique no botão **"+ New query"**.
3. Cole o código abaixo exatamente como está:

```sql
-- 1. Criação da Tabela de Pacientes e Agendamentos
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

-- 2. Habilita acesso seguro
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Acesso Total Leads" ON leads FOR ALL USING (true) WITH CHECK (true);

-- 3. Habilita Sincronização em Tempo Real (Realtime)
ALTER PUBLICATION supabase_realtime ADD TABLE leads;
```

4. Clique no botão verde **"Run"** (no canto inferior direito da tela).
5. Você verá a mensagem **"Success. No rows returned"** em verde. A tabela já está pronta!

---

## 🔑 Passo 4: Copiar as 2 Chaves de Acesso
No menu lateral esquerdo do Supabase:
1. Clique no ícone de **Engrenagem (Project Settings)** no rodapé.
2. No submenu, clique em **API**.
3. Você encontrará duas informações essenciais:
   * **Project URL**: (ex: `https://abcdefghijklmnopqrst.supabase.co`)
   * **Project API Keys** ➔ copie o código longo da chave **`anon` / `public`**.

---

## 💻 Passo 5: Ativar no Painel do Consultório
1. Abra o arquivo do painel administrativo da clínica no computador (`index.html`).
2. Clique no botão **"Modo Demo (Local)"** ou acesse **Configurações** (no menu lateral).
3. Na seção **Conexão Nuvem (Supabase)**:
   * Cole o **Project URL**.
   * Cole a **Chave Anon**.
4. Clique em **"Conectar e Sincronizar"**.

---

### 🎉 Pronto! O que acontece a partir de agora?
* O status no topo do painel mudará para: **🟢 Nuvem Conectada**.
* Quando qualquer paciente agendar uma consulta no site da clínica, **o card do paciente aparecerá automaticamente em tempo real** na coluna *"Novos Contatos"* do Kanban e na Agenda do consultório, sem precisar recarregar a página!
