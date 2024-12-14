from colorama import init, Fore, Back, Style

# Инициализация colorama
init(autoreset=True)

# Демонстрация работы с текстом и фоном
print(Fore.RED + 'Красный текст')
print(Back.YELLOW + 'Текст с желтым фоном')
print(Fore.GREEN + Back.CYAN + 'Зеленый текст на голубом фоне')

# Использование стиля
print(Style.DIM + 'Текст с приглушенным стилем')
print(Style.BRIGHT + 'Текст с ярким стилем')
print(Style.RESET_ALL + 'Сброс всех стилей')

# Без autoreset (ручной сброс)
print(Fore.MAGENTA + 'Текст без autoreset', end='')
print(' Все еще с фиолетовым цветом')
print(Style.RESET_ALL + 'Теперь сброшено')
