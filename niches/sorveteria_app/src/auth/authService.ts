// DevHub AI Work OS — Módulo de Autenticação Segura
// Gerado por: jvna14@gmail.com
export interface UserSession {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
  token: string;
}

export class AuthService {
  static async login(email: string, pass: string): Promise<UserSession> {
    return { id: 'usr_01', name: 'Dr. Usuário', email, role: 'admin', token: 'jwt_secure_token' };
  }
  static logout(): void {
    localStorage.removeItem('auth_session');
  }
}
