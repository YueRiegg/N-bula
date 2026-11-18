from datetime import date


class Divulgacao:
    def __init__(self, titulo, descricao):
        self._titulo = titulo
        self._descricao = descricao
        self._data = date.today()
        self._publicada = False

    def publicar(self):
        self._publicada = True

    def remover(self):
        self._publicada = False
