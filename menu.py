# Classe que constrói objetos Menu com características semelhantes

class Menu:

    __menuName = ""
    __itemsArray = []  # Array de strings que representam as opções do menu
    __funcArray = []  # Array de funções a serem executadas correspondente ao item do menu
    __userInput = 0  # Entrada do usuário para cada menu
    __previousMenu = None  # Menu anterior

    # Função construtora do objeto menu
    def __init__(self, __menuName, __itemsArray, __funcArray):
        self.__menuName = __menuName
        self.__itemsArray = __itemsArray
        self.__funcArray = __funcArray
        self.__userInput = 0
        self.__previousMenu = None

    # Métodos setters e getters
    def setItem(self, string):
        self.__itemsArray.append(string)

    def getItem(self, index):
        return self.__itemsArray[index]

    def setFunction(self, function):
        self.__funcArray.append(function)

    def getFunction(self, index):
        return self.__funcArray[index]

    # Método que exibe o array das opções
    def __showMenu(self):
        print(self.__menuName + "\n")
        for item in self.__itemsArray:
            print(item)

    # Método que resgata a entrada do usuário
    def __getUserInput(self):
        self.__userInput = int(
            input("\nInsira um número correspondente à opção desejada:\n"))

    # Método que verifica se a entrada é válida e retorna um booleano
    def __isUserImputValid(self):
        return (self.__userInput > 0 and self.__userInput <= len(self.__itemsArray))    

    # Método que exibe a interface de atendimento
    def showInterface(self):
        self.__showMenu()

        # Laço de entrada: o sistema irá pedir entrada do usuário enquanto não for válida
        while(not self.__isUserImputValid()):
            self.__getUserInput()
            print("")

            if(self.__isUserImputValid()):
                # resgata a função correspondente à entrada inserida e executa ela
                menuFunction = self.getFunction(self.__userInput - 1)
                menuFunction(self)
                break
            else:
                print("Entrada inválida! Por favor, tente novamente")

    # Método de chamada da interface anterior
    def __callbackInterface(self, menuObject):
        self.__previousMenu.__userInput = 0
        self.__previousMenu.showInterface()

    # Método que retorna se há uma opção de voltar
    def __hasBackOption(self):
        for item in self.__itemsArray:
            if(item.find("Voltar para o menu anterior") != -1):
                return True
        return False

    # Método que adiciona opção de voltar para menus secundários
    def addBackMenuOption(self, previousMenu):
        lastOption = len(self.__itemsArray)

        if (not self.__hasBackOption()):
            self.__previousMenu = previousMenu
            self.__itemsArray.append(
                (str(lastOption + 1) + " - Voltar para o menu anterior"))
            self.__funcArray.append(self.__callbackInterface)
            
