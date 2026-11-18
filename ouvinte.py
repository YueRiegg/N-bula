from .usuario import Usuario
from .playlist import Playlist
from modules.busca import Busca


class Ouvinte(Usuario):
    def __init__(self, id, nome, email, preferencias=None):
        super().__init__(id, nome, email)
        self._preferencias = list(preferencias or [])
        self._playlists = []
        self._seguindo = []

    def criar_playlist(self, nome, descricao=""):
        playlist = Playlist(nome, descricao)
        self._playlists.append(playlist)
        return playlist

    def seguir_artista(self, artista):
        if artista not in self._seguindo:
            self._seguindo.append(artista)

    def buscar(self, termo):
        busca = Busca(termo)
        return busca.buscar_musicas(), busca.buscar_artistas()
