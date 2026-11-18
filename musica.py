from abc import ABC

class Musica(ABC):
    def __init__(self, titulo, duracao, genero):
        self._titulo = titulo
        self._duracao = duracao
        self._genero = genero
        self._tocando = False

#===========================================================

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

#===========================================================

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        if duracao < 0:
            raise ValueError("A duração não pode ser negativa.")
        self._duracao = duracao

#===========================================================

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

#===========================================================

    @property
    def tocando(self):
        return self._tocando

    @tocando.setter
    def tocando(self, tocando):
        self._tocando = tocando

#===========================================================
    
    def reproduzir(self):
        self._tocando = True

    def pausar(self):
        self._tocando = False

    def __repr__(self):
        return f"Musica({self._titulo!r}, {self._genero!r})"