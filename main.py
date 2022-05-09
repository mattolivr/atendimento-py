from menu import Menu

from modules.principal import (itemsPrincipal, funcsPrincipal)

principal = Menu("MENU PRINCIPAL", itemsPrincipal, funcsPrincipal)

print("SEJA BEM-VINDO(a) À MELISSÃO CRÉDITOS ESPECIAIS LTDA\n")

principal.showInterface()