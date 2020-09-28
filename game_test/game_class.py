"""
Написать для консоли простую игру для двух игроков:
- Программа генерирует простое число x в промежутке между 12 и 120 и сообщает игрокам.
- Игроки в свой ход могут выбрать число между 1 и 5. Это число вычитается из x.
- Выигрывает тот, кто первым получит 0.
- При старте предлагается ввести свои никнеймы, они хранятся до конца игры. 
- Добавить возможность игры между двумя игроками, игроком и компьютером (однопользовательская игра).
- Предложить реализацию разных уровней сложности.
    -Простая сложность: вывод оставшегося числа в консоль после каждого хода,
        выбор числа между 1 и 5
    -Средняя сложность: вывод оставшегося числа в консоль после каждого хода,
        выбор числа между 1 и 10
    -Максимальная сложность: Нет вывода оставшегося числа между ходами,
        выбор числа между 1 и 5
"""

import random

# Основной класс
class Game:
    def __init__(self, player_one,  difficult, player_two = None):
        self.player_one = player_one
        self.player_two = player_two
        self.difficult = difficult
        self.__number = random.randint(13, 119)
        self.__answer_range = self.__get_difficult()['answer_range']
        self.__answer_between = self.__get_difficult()['answer_between']

    # Выбор диапазона ответов и вывода промежуточного остатка в зависимости от сложности
    def __get_difficult(self):
        difficult_level = {1:{'answer_range': 5, 'answer_between': True},
                            2:{'answer_range': 10, 'answer_between': True},
                            3:{'answer_range': 5, 'answer_between': False},
                            }
        
        return difficult_level[self.difficult]
    
    # Логика ввода числа для AI (для одного игрока)
    def __ai_player(self, current_number):
        if current_number in range(1, self.__answer_range + 1):
            print('Компьютер победил.\n')
            print('Текущий остаток - 0')    
            return 0
        else:
            ai_random = random.randint(1, self.__answer_range)
            
            print(f'Компьютер выбирает - {ai_random}')    
            return (current_number - ai_random)
    
    # Логика ввода числа для живых игроков
    def __real_player(self, player, current_number):
        if current_number not in range(1, self.__answer_range +1):
            last_number = self.__answer_range
        else:
            last_number = current_number
            
        player_input = input(f'{player}, введите ваше число (от 1 до {last_number}) - ')
        
        if player_input.isdigit() and int(player_input) in range(1, last_number + 1):
            result = current_number - int(player_input)
        else:
            print('Некорректный ввод, попробуйте ещё раз')    
            return self.__real_player(player, current_number)
        
        if result == 0:
            #print('Текущий остаток - 0')
            print(f'{player} - вы победили\n')
            print('Текущий остаток - 0')
        return result
    
    # Основная логика игры 
    @property
    def start_game(self):
        current_number = self.__number
        
        print(f'\nЗагадано число {current_number}')

        while current_number != 0:
            current_number = self.__real_player(self.player_one, current_number)
            if current_number == 0:
                break
                
            if self.__answer_between:
                print(f'\nТекущий остаток - {current_number}')
                
            if self.player_two != None:
                current_number = self.__real_player(self.player_two, current_number)
            else:
                current_number = self.__ai_player(current_number)
                
            if current_number == 0:
                break
                
            if self.__answer_between:
                print(f'\nТекущий остаток - {current_number}')
        return print('\n\nИгра окончена')
