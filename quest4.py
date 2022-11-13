class QuestionFour:
    def __init__(self):
        self.__pilha = []

    def decodificar(self, item):
        for dado in range(len(item)):
            if item[dado] == "]":
                texto = ''
                while self.__pilha:
                    valor = self.__pilha.pop()
                    if valor == "[":
                        break
                    texto = valor + texto
                num = ''
                while self.__pilha and self.__pilha[-1].isdigit():
                    num = self.__pilha.pop() + num
                self.__pilha.append(int(num) * texto)
            else:
                self.__pilha.append(item[dado])
        return print(''.join(self.__pilha))


