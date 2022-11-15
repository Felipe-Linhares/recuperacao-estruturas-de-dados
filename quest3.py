class QuestionThree:
    def __init__(self):
        self.__pilha = []

    def push(self, elemento):
        self.__pilha.append(elemento)

    def top(self):
        print(self.__pilha[-1])

    def getMin(self):
        if len(self.__pilha) == 0:
            return print('I rapaz, tá vazio aqui.')
        # pego o primeiro numero da pilha
        menor = self.__pilha[0]
        # percorro a lista
        for numero in self.__pilha:
            # Verifico se os numeros da minha lista é menor que o primeiro numero da pilha
            if numero < menor:
                # Se for digo que esse numero é o menor numero
                menor = numero

        print(menor)

    def pop(self):
        self.__pilha.pop()

    def __str__(self):
        ret = ' '.join(str(element) for element in self.__pilha)
        return ret
