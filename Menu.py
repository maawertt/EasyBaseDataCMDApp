import os
import csv
from collections.abc import Callable


class Menu:

    def __init__(self, button_exit: str, button_append: str,
                 button_pop: str, button_print: str) -> None:
        self.__button_exit = button_exit
        self.__button_append = button_append
        self.__button_pop = button_pop
        self.__button_print = button_print

    def __str__(self) -> str:
        return (f'{self.__button_append}: Добавить пользователя\n'
              f'{self.__button_pop}: Удалить пользователя\n'
              f'{self.__button_print}: Вывести список всех пользователя\n'
              f'{self.__button_exit}: Выйти')

    def get_button_exit(self) -> str: return self.__button_exit

    def get_button_append(self) -> str: return self.__button_append

    def get_button_pop(self) -> str: return self.__button_pop

    def get_button_print(self) -> str: return self.__button_print

    @staticmethod
    def clear_console() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')


