class QuestionTwo:
    def __init__(self):
        self.__entradaS = []
        self.__entradaT = []
        self.__contadorDeBackspaceS = 0
        self.__contadorDeBackspaceT = 0

    def get_entradas(self, entradaS, entradaT):
        entradaSReversa = []
        entradaTReversa = []

        # Para cada entrada enserida é mandada para sua respectiva pilha.
        for entrada in entradaS:
            self.__entradaS.append(entrada)

        for entrada in entradaT:
            self.__entradaT.append(entrada)

        # ANALIZANDO A PILHA entradaS

        # Uso um while para rodar enquanto a entradaS for maior que zero
        while len(self.__entradaS) > 0:
            # Inverto a ordem dos itens
            for item in reversed(self.__entradaS):
                # Se o item for igual ao backspace, adiciono 1 no contador e dou um pop
                if item == "#":
                    self.__contadorDeBackspaceS += 1
                    self.__entradaS.pop()
                # Se o contador for maior que zero e o item for diferente do backspace
                elif self.__contadorDeBackspaceS > 0 and item != "#":
                    # Faço um for no range do contador,  dou um pop
                    for _ in range(self.__contadorDeBackspaceS):
                        self.__entradaS.pop()
                        # Se o tamanho da minha entradaS é igual a zero, paro o while e digo que meu contadro recebe zero
                        if len(self.__entradaS) == 0:
                            break
                    self.__contadorDeBackspaceS = 0
                # Se não adiciono meu item na minha pilha reversa e dou um pop na entradaS
                else:
                    entradaSReversa.append(item)
                    self.__entradaS.pop()
        # Depois pego os item da minha pilha reversa e reverto ao original e adiciono na minha entradaS
        for itemReverso in reversed(entradaSReversa):
            self.__entradaS.append(itemReverso)


        # ANALIZANDO A PILHA entradaT

        # Uso um while para rodar enquanto a entradaT for maior que zero
        while len(self.__entradaT) > 0:
            # Inverto a ordem dos itens
            for item in reversed(self.__entradaT):
                # Se o item for igual ao backspace, adiciono 1 no contador e dou um pop
                if item == "#":
                    self.__contadorDeBackspaceT += 1
                    self.__entradaT.pop()
                # Se o contador for maior que zero e o item for diferente do backspace
                elif self.__contadorDeBackspaceT > 0 and item != "#":
                    # Faço um for no range do contador,  dou um pop
                    for _ in range(self.__contadorDeBackspaceT):
                        self.__entradaT.pop()
                        # Se o tamanho da minha entradaS é igual a zero, paro o while e digo que meu contadro recebe zero
                        if len(self.__entradaT) == 0:
                            break
                    self.__contadorDeBackspaceT = 0
                else:
                    # Se meu item for dirente do backspace e o contador for igual a zero
                    if item != "#" and self.__contadorDeBackspaceT == 0:
                        # Adiciono meu item na minha pilha reversa e dou um pop na entradaT
                        entradaTReversa.append(item)
                        self.__entradaT.pop()
        # Depois pego os item da minha pilha reversa e reverto ao original e adiciono na minha entradaT
        for itemReverso in reversed(entradaTReversa):
            self.__entradaT.append(itemReverso)
        # Comparação se uma pilha é igual a outra
        if self.__entradaS == self.__entradaT:
            print(True)
        else:
            print(False)
