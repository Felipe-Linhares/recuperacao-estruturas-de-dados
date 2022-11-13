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
        menor = self.__pilha[0]
        for numero in self.__pilha:
            if numero < menor:
                menor = numero

        print(menor)

    def pop(self):
        self.__pilha.pop()

    def __str__(self):
        ret = ' '.join(str(element) for element in self.__pilha)
        return ret
