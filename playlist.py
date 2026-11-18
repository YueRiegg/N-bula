from abc import ABC
from datetime import date


class Playlist(ABC):
    def __init__(self, nome, descricao=""):
        self._nome = nome
        self._descricao = descricao
        self._data_criacao = date.today()
        self._musicas = []

    #===========================================================

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    #===========================================================

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    #===========================================================

    @property
    def data_criacao(self):
        return self._data_criacao

    @data_criacao.setter
    def data_criacao(self, data_criacao):
        self._data_criacao = data_criacao

    #===========================================================

    @property
    def musicas(self):
        return list(self._musicas)

    @musicas.setter
    def musicas(self, musicas):
        self._musicas = list(musicas)

    #===========================================================

    def adicionar_musica(self, musica):
        if musica not in self._musicas:
            self._musicas.append(musica)

    def remover_musica(self, musica):
        if musica in self._musicas:
            self._musicas.remove(musica)

    def listar_musicas(self):
        return list(self._musicas)