class QuestionFour:
    def __init__(self):
        self.__pilha = []

    def decodificar(self, item):
        # Para cada dado no tamanho do meu item
        for dado in range(len(item)):
            # Se o meu item tiver o dado igual ao simbolo
            if item[dado] == "]":
                # meu texto começa vazio
                texto = ''
                # Pecorro minha pilha
                while self.__pilha:
                    # atribuio o meu pop a uma variavel
                    valor = self.__pilha.pop()
                    # se meu valor for igual ao simbolo, eu paro o while
                    if valor == "[":
                        break
                    # Altero o valor do meu texto, difgo que o meu texto antigo recebe o valor + texto
                    texto = valor + texto
                # Digo que minha variavel numero começa vazia
                numero = ''
                # Faço um while na minha pilha e no ultimo item da pilha, uso um builtin para verificar se todo os caracteres são digitiro
                while self.__pilha and self.__pilha[-1].isdigit():
                    # Digo que meu novo numero é um pop + o numero
                    numero = self.__pilha.pop() + numero
                # adiciono meu numero inteiro na minha pilha e multiplico o texto
                self.__pilha.append(int(numero) * texto)
            # se o item não tiver um simbolo diferente , ele adiciona o dado na pilha
            else:
                self.__pilha.append(item[dado])
        return print(''.join(self.__pilha))


