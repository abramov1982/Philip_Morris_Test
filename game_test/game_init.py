"""
Написать для консоли простую игру для двух игроков:
- Программа генерирует простое число x в промежутке между 12 и 120 и сообщает игрокам.
- Игроки в свой ход могут выбрать число между 1 и 5. Это число вычитается из x.
- Выигрывает тот, кто первым получит 0.
- При старте предлагается ввести свои никнеймы, они хранятся до конца игры. 
- Добавить возможность игры между двумя игроками, игроком и компьютером (однопользовательская игра).
- Предложить реализацию разных уровней сложности.
    -Простая сложность: вывод оставшегося числа в консоль после каждой пары ходов,
        выбор числа между 1 и 5
    -Средняя сложность: вывод оставшегося числа в консоль после каждой пары ходов,
        выбор числа между 1 и 10
    -Максимальная сложность: Нет вывода оставшегося числа между ходами,
"""     

from game_class import Game

# Проверка корректности ввода опций
def check_options(option, option_range):
    if option.isdigit() and int(option) in option_range:
        return True
    
# Ввод опций игры
def game_options(): 
    def choose_players():
        players = input('Введите количество игроков (1/2) - ')
        
        if check_options(players, [1,2]):
            return int(players)
        else: 
            print('Некорректный ввод')
            choose_players()

    def name_players():
        players_counter = choose_players()
        player_one = input('Введите имя первого игрока - ')

        if players_counter == 2:
            player_two = input('Введите имя второго игрока - ')
        else:
            player_two = None 
        return {'player_one':player_one, 'player_two':player_two}
    
    def choose_difficult():
        difficult = input('Выберите сложность (1/2/3) - ')
        
        if check_options(difficult, [1,2,3]):
            return {'difficult':int(difficult)}
        else: 
            print('Некорректный ввод')
            choose_difficult()    
    return {**name_players(), **choose_difficult()}


# Инициализация игры и запуск
current_game = Game(**game_options())
current_game.start_game
