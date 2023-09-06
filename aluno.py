class Aluno:

    def __init__(self, rgm, nome, sexo, media):
        self.rgm = rgm
        self.nome = nome
        self.sexo = sexo
        self.media = media

    def __str__(self) -> str:
        return f'{self.rgm} - {self.nome} - {self.sexo} - {self.media:.2f}'

    def __eq__(self, other: object) -> bool:
        return self.rgm == other.rgm

    def __lt__(self, other: object) -> bool:
        return self.rgm < other.rgm
