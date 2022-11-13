class QuestionTwo:
    def __init__(self):
        self.__entradaS = []
        self.__entradaT = []
        self.__contadorDeBackspaceS = 0
        self.__contadorDeBackspaceT = 0

    def get_entradas(self, entradaS, entradaT):
        entradaSReversa = []
        entradaTReversa = []

        for entrada in entradaS:
            self.__entradaS.append(entrada)

        for entrada in entradaT:
            self.__entradaT.append(entrada)

        # ANALIZANDO A PILHA entradaS
        while len(self.__entradaS) > 0:
            for item in reversed(self.__entradaS):

                if item == "#":
                    self.__contadorDeBackspaceS += 1
                    self.__entradaS.pop()

                elif self.__contadorDeBackspaceS > 0 and item != "#":
                    for _ in range(self.__contadorDeBackspaceS):
                        self.__entradaS.pop()
                        if len(self.__entradaS) == 0:
                            break
                    self.__contadorDeBackspaceS = 0

                else:
                    entradaSReversa.append(item)
                    self.__entradaS.pop()

        for itemReverso in reversed(entradaSReversa):
            self.__entradaS.append(itemReverso)

        while len(self.__entradaT) > 0:
            for item in reversed(self.__entradaT):
                if item == "#":
                    self.__contadorDeBackspaceT += 1
                    self.__entradaT.pop()

                elif self.__contadorDeBackspaceT > 0 and item != "#":
                    for _ in range(self.__contadorDeBackspaceT):
                        self.__entradaT.pop()
                        if len(self.__entradaT) == 0:
                            break

                    self.__contadorDeBackspaceT = 0

                else:
                    if item != "#" and self.__contadorDeBackspaceT == 0:
                        entradaTReversa.append(item)
                        self.__entradaT.pop()

        for itemReverso in reversed(entradaTReversa):
            self.__entradaT.append(itemReverso)

        if self.__entradaS == self.__entradaT:
            print(True)
        else:
            print(False)
