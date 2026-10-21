from datetime import date


class Usuario:
    cadastrados = []

    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
        self.logado = False

    def cadastrar(self):
        if self not in Usuario.cadastrados:
            Usuario.cadastrados.append(self)

    def login(self):
        self.logado = self in Usuario.cadastrados
        return self.logado


class Musica:
    def __init__(self, titulo, duracao, genero):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero
        self.tocando = False

    def reproduzir(self):
        self.tocando = True

    def pausar(self):
        self.tocando = False


class Divulgacao:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.data = date.today()
        self.publicada = False

    def publicar(self):
        self.publicada = True

    def remover(self):
        self.publicada = False


class Playlist:
    def __init__(self, nome, descricao=""):
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = date.today()
        self.musicas = []

    def adicionar_musica(self, musica):
        if musica not in self.musicas:
            self.musicas.append(musica)

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)


class Artista(Usuario):
    def __init__(self, id, nome, email, biografia, genero_principal):
        super().__init__(id, nome, email)
        self.biografia = biografia
        self.genero_principal = genero_principal
        self.musicas = []
        self.divulgacoes = []

    @staticmethod
    def todos():
        return [u for u in Usuario.cadastrados if isinstance(u, Artista)]

    def divulgar_musica(self, musica):
        if musica not in self.musicas:
            self.musicas.append(musica)
        divulgacao = Divulgacao(
            f"Novo lançamento: {musica.titulo}",
            f"{self.nome} acabou de lançar {musica.titulo}",
        )
        divulgacao.publicar()
        self.divulgacoes.append(divulgacao)
        return divulgacao

    def editar_biografia(self, biografia):
        self.biografia = biografia


class Busca:
    def __init__(self, termo):
        self.termo = termo.lower()

    def buscar_musicas(self):
        return [
            musica
            for artista in Artista.todos()
            for musica in artista.musicas
            if self.termo in musica.titulo.lower()
        ]

    def buscar_artistas(self):
        return [a for a in Artista.todos() if self.termo in a.nome.lower()]


class Descoberta:
    def __init__(self, criterio):
        self.criterio = criterio

    def recomendar_musicas(self):
        return [
            musica
            for artista in Artista.todos()
            for musica in artista.musicas
            if musica.genero == self.criterio
        ]

    def recomendar_artistas(self):
        return [a for a in Artista.todos() if a.genero_principal == self.criterio]


class Player:
    def __init__(self, fila=None):
        self.estado = "parado"
        self.fila = list(fila or [])
        self.musica_atual = None

    def tocar(self):
        if self.musica_atual is None and self.fila:
            self.musica_atual = self.fila.pop(0)
        if self.musica_atual is None:
            self.estado = "parado"
            return
        self.musica_atual.reproduzir()
        self.estado = "tocando"

    def pausar(self):
        if self.musica_atual:
            self.musica_atual.pausar()
            self.estado = "pausado"

    def proxima(self):
        self.pausar()
        self.musica_atual = None
        self.tocar()


class Ouvinte(Usuario):
    def __init__(self, id, nome, email, preferencias=None):
        super().__init__(id, nome, email)
        self.preferencias = preferencias or []
        self.playlists = []
        self.seguindo = []

    def criar_playlist(self, nome, descricao=""):
        playlist = Playlist(nome, descricao)
        self.playlists.append(playlist)
        return playlist

    def seguir_artista(self, artista):
        if artista not in self.seguindo:
            self.seguindo.append(artista)

    def buscar(self, termo):
        busca = Busca(termo)
        return busca.buscar_musicas(), busca.buscar_artistas()


if __name__ == "__main__":
    artista = Artista(1, "Luna Vega", "luna@email.com", "Cantora de indie", "indie")
    artista.cadastrar()
    artista.divulgar_musica(Musica("Maré Alta", 210, "indie"))
    artista.divulgar_musica(Musica("Noite Longa", 185, "indie"))

    ouvinte = Ouvinte(2, "Soul", "soul@email.com", ["indie"])
    ouvinte.cadastrar()
    print("login:", ouvinte.login())

    ouvinte.seguir_artista(artista)
    musicas, artistas = ouvinte.buscar("luna")
    print("artistas:", [a.nome for a in artistas])
    musicas, _ = ouvinte.buscar("maré")
    print("musicas:", [m.titulo for m in musicas])

    playlist = ouvinte.criar_playlist("Favoritas")
    for musica in Descoberta("indie").recomendar_musicas():
        playlist.adicionar_musica(musica)
    print("playlist:", [m.titulo for m in playlist.musicas])

    player = Player(playlist.musicas)
    player.tocar()
    print(player.estado, "-", player.musica_atual.titulo)
    player.proxima()
    print(player.estado, "-", player.musica_atual.titulo)
    player.proxima()
    print(player.estado)
