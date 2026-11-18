from abc import ABC, abstractmethod
from datetime import datetime


class Usuario(ABC):
    def __init__(self, id, nome, email, senhaHash):
        self._id = id
        self._nome = nome
        self._email = email
        self._senhaHash = senhaHash
        self._dataCriacao = datetime.now()
        self._ativo = True

#====================================================================

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

#====================================================================

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

#====================================================================

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

#====================================================================

    @property
    def senhaHash(self):
        return self._senhaHash

    @senhaHash.setter
    def senhaHash(self, nova_senha):
        self._senhaHash = nova_senha

#====================================================================

    @property
    def dataCriacao(self):
        return self._dataCriacao

    @dataCriacao.setter
    def dataCriacao(self, nova_data):
        self._dataCriacao = nova_data

#====================================================================

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, novo_status):
        self._ativo = novo_status

#====================================================================

    def cadastrar(self):
        self._ativo = True
        return True

    def entrar(self, email, senha):
        if self._email == email and self._senhaHash == senha:
            return "Login realizado com sucesso."
        return "Email ou senha incorretos."

    def sair(self):
        return "Sessão encerrada."

    def editarPerfil(self, nome):
        self._nome = nome
        return True

    def alterarSenha(self, novaSenha):
        self._senhaHash = novaSenha
        return True

    def excluirConta(self):
        self._ativo = False
        return True

    @abstractmethod
    def obterTipo(self):
        pass