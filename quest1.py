class QuestionOne:
    def __init__(self):
        self.__entrada = []

    def get_entrada(self, entrada):

        # Verifico cada item que foi inserido
        for item in entrada:
            # Se o item for diferente dos símbolos e se a pilha for maior que zero
            if item != '(' and item != '[' and item != '{' and len(self.__entrada) > 0:
                ultimo = self.__entrada[-1]
                # Se o item for igual ao símbolo e se o ultimo for igual ao simbolo
                if (item == ")" and ultimo == "(") or (item == "]" and ultimo == "[") or (item == "}" and ultimo == "{"):
                    # Dou um pop se a condição for atendida
                    self.__entrada.pop()
                else:
                    return print(False)
            else:
                # Se o if inicial não for atendido adiciono o símbolo na minha pilha

                self.__entrada.append(item)

        if len(self.__entrada) == 0:
            return print(True)
        else:
            return print(False)

