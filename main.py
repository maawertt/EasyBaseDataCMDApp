from Handler import Handler
from Menu import *

def main() -> int:

    menu = Menu('q', '1', '2', '3')
    messageHandler = Handler()

    Menu.clear_console()
    while True:
        print(menu, '\n')
        inputUser: str = input('Выберите меню списка: ')
        if inputUser == menu.get_button_append(): messageHandler.append_user()
        if inputUser == menu.get_button_pop(): messageHandler.del_user()
        if inputUser == menu.get_button_print(): messageHandler.print_users_list()
        if inputUser == menu.get_button_exit(): break

    return 0

if __name__ == '__main__': main()
