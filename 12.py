> ⚝ Нереальный талант ☓ ☓ ☓ けいれん:
import sqlite3

# Инициализация базы данных для хранения результатов
def init_db():
    conn = sqlite3.connect('tic_tac_toe.db')  # Создаем или подключаемся к базе данных
    cursor = conn.cursor()
    
    # Создаем таблицу для хранения результатов
    cursor.execute('''CREATE TABLE IF NOT EXISTS game_results (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        winner TEXT,
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    
    conn.commit()
    conn.close()

# Класс для логики игры "Крестики-нолики"
class TicTacToe:
    def init(self):
        self.board = [' ' for _ in range(9)]  # Игровое поле 3x3
        self.current_player = 'X'

    def print_board(self):
        for i in range(3):
            print(f'{self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]}')
            if i < 2:
                print('---------')
    
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False
    
    def check_winner(self):
        # Все возможные комбинации для победы
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные линии
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные линии
            (0, 4, 8), (2, 4, 6)               # Диагонали
        ]
        
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return self.board[condition[0]]  # Возвращаем победителя ('X' или 'O')
        
        if ' ' not in self.board:
            return 'D'  # Ничья (если нет пустых клеток)
        
        return None  # Игра продолжается
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def reset_board(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

# Сохранение результатов игры в базу данных
def save_game_result(winner):
    conn = sqlite3.connect('tic_tac_toe.db')
    cursor = conn.cursor()
    
    # Сохраняем результаты игры
    cursor.execute("INSERT INTO game_results (winner) VALUES (?)", (winner,))
    
    conn.commit()
    conn.close()

# Просмотр истории игр
def view_game_history():
    conn = sqlite3.connect('tic_tac_toe.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM game_results")
    games = cursor.fetchall()
    
    if not games:
        print("Нет истории игр.")
    else:
        for game in games:
            print(f"Игра #{game[0]}: Победитель: {game[1]}, Дата: {game[2]}")
    
    conn.close()

# Главная функция игры
def play_game():
    init_db()
    game = TicTacToe()
    
    while True:
        game.print_board()
        print(f"Ход игрока: {game.current_player}")
        
        # Запросить ход игрока
        try:
            move = int(input("Введите номер клетки (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Неверный номер клетки, попробуйте снова.")
                continue
        except ValueError:
            print("Введите число.")
            continue
        
        if game.make_move(move):
            winner = game.check_winner()
            if winner:
                game.print_board()
                if winner == 'D':
                    print("Ничья!")
                    save_game_result('D')
                else:
                    print(f"Победил игрок {winner}!")
                    save_game_result(winner)
                break
            game.switch_player()
        else:
            print("Эта клетка уже занята, попробуйте снова.")
        
        # Запросить, хочет ли кто-то сыграть снова
        replay = input("Хотите сыграть снова? (y/n): ").lower()
        if replay != 'y':
            break

> ⚝ Нереальный талант ☓ ☓ ☓ けいれん:
# Главная точка входа программы
if name == "main":
    while True:
        print("\nМеню:")
        print("1. Играть в Крестики-нолики")
        print("2. Просмотреть историю игр")
        print("3. Выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            view_game_history()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")
