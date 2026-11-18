# controle_acesso.py - cadastro e login dos usuários

import secrets

from usuarios.papeis import papeis_validos

CREDENCIAL_INVALIDA = "Matrícula ou senha inválida."


class ControleAcesso:
    # Começa sem usuários e sem sessões abertas
    def __init__(self):
        self.usuarios = []
        self.sessoes = {}

    # Procura um usuário pela matrícula
    def buscar(self, matricula):
        for u in self.usuarios:
            if u.matricula == matricula:
                return u
        return None

    # Cadastra um usuário se a matrícula ainda não existir
    def cadastrar(self, usuario):
        achado = self.buscar(usuario.matricula)
        if achado is not None:
            return False
        self.usuarios.append(usuario)
        return True

    # Confere os dados e cria um token de acesso
    def entrar(self, matricula, senha):
        usuario = self.buscar(matricula)
        if usuario is None:
            return None
        if not usuario.conferir_senha(senha) or usuario.situacao != "ativo":
            return None
        token = secrets.token_hex(16)
        self.sessoes[token] = matricula
        return token

    # Devolve o usuário ligado ao token
    def usuario_logado(self, token):
        matricula = self.sessoes.get(token)
        if matricula is None:
            return None
        return self.buscar(matricula)

    # Encerra uma sessão
    def sair(self, token):
        if token not in self.sessoes:
            return False
        del self.sessoes[token]
        return True

    # Troca os cargos de um usuário
    def mudar_papeis(self, quem, matricula, papeis):
        if not quem.pode("mudar_papeis"):
            return "Você não tem permissão para mudar papéis."
        usuario = self.buscar(matricula)
        if usuario is None:
            return "Usuário não encontrado."
        if len(papeis) == 0:
            return "Escolha pelo menos um papel."
        validos = papeis_validos()
        for papel in papeis:
            if papel not in validos:
                return "Papel inválido: " + papel
        usuario.papeis = papeis
        return None
