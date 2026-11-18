from .usuario import Usuario
from .divulgacao import Divulgacao


class Artista(Usuario):
    def __init__(self, id, nome, email, biografia, genero_principal):
        super().__init__(id, nome, email)
        self._biografia = biografia
        self._genero_principal = genero_principal
        self._musicas = []
        self._divulgacoes = []

    
    @staticmethod
    def todos():
        return [usuario for usuario in Usuario.cadastrados if isinstance(usuario, Artista)]

    
    def divulgar_musica(self, musica):
        if musica not in self._musicas:
            self._musicas.append(musica)
            
        divulgacao = Divulgacao(f"Novo lançamento: {musica._titulo}", f"{self._nome} acabou de lançar {musica._titulo}")
        divulgacao.publicar()
        
        self._divulgacoes.append(divulgacao)
        
        return divulgacao

    
    def editar_biografia(self, biografia):
        self._biografia = biografia
