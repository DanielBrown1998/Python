
class Avaliacao:
    def __init__(self, usuario, restaurante, nota, avaliacao):
        self.__usuario = usuario
        self.__restaurante = restaurante
        self.__nota = nota
        self.__avaliacao = avaliacao

    def __str__(self):
        return f'{self.__usuario} avaliou o curso {self.__restaurante} com nota {self.__nota} e avaliação: {self.__avaliacao}'

    @property
    def usuario(self):
        return self.__usuario

    @property
    def restaurante(self):
        return self.__restaurante

    @property
    def nota(self):
        return self.__nota

    @property
    def avaliacao(self):
        return self.__avaliacao
    
    