class QuestionOne:
    def __init__(self):
        self.__entrada = []

    def get_entrada(self, entrada):

        for item in entrada:

            if item != '(' and item != '[' and item != '{' and len(self.__entrada) > 0:
                anterior = self.__entrada[-1]
                if (item == ")" and anterior == "(") or (item == "]" and anterior == "[") or (item == "}" and anterior == "{"):
                    self.__entrada.pop()
                else:
                    return print(False)
            else:
                self.__entrada.append(item)
        if len(self.__entrada) == 0:
            return print(True)
        else:
            return print(False)

