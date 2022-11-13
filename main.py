from quest1 import QuestionOne
from quest2 import QuestionTwo
from quest3 import QuestionThree


def start():
    quest1 = QuestionOne()
    # quest1.get_entrada(')(')

    quest2 = QuestionTwo()
    # quest2.get_entradas('juini#####', 'juini####')

    quest3 = QuestionThree()
    quest3.push(6)
    quest3.push(-3)
    quest3.push(3)
    print(quest3)

    quest3.pop()
    quest3.top()
    quest3.getMin()
    print(quest3)







if __name__ == '__main__':
    start()
