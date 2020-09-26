#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
        выбор числа между 1 и 10
"""

import random

players = int(input('Введите количество игроков (1/2) - '))
player_one = input('Введите имя перовго игрока - ')

if players == 2:
    player_two = input('Введите имя второго игрока - ')
else:
    player_two = None

difficult = int(input('Выберите сложность (1-простая, 2-средняя, 3-сложная) - '))

class Game():
    def __init__(self, player_one, player_two = None, difficult = 2):
        self.player_one = player_one
        self.player_two = player_two
        self.difficult = difficult
        self.__number = random.randint(13, 119)
        self.__answer_range = self.__get_difficult()['answer_range']
        self.__answer_between = self.__get_difficult()['answer_between']
        
    def __get_players(self):
        if self.player_two is not None:
            return True
        else:
            return False
    
    def __get_difficult(self):
        diffilulty_level = {1:{'answer_range': 5, 'answer_between': True},
                            2:{'answer_range': 10, 'answer_between': True},
                            3:{'answer_range': 5, 'answer_between': False},
                            }
        return diffilulty_level[self.difficult]
    
    def __ai_player(self, current_number):
        if current_number in range(1, self.__answer_range + 1):
            return current_number
        else:
            return random.randint(1, self.__answer_range + 1)
    
    def __num_player(self, player_number, current_number):
        
        if current_number not in range(1, self.__answer_range +1):
            last_number = self.__answer_range
        else:
            last_number = current_number
        
# Переписать этот кусок через try except
# --------------------------------------------------        
        player_input = input(f'{player_number}, введите ваше число (от 1 до {last_number}) - ')
        
        if type(int(player_input)) is int and int(player_input) in range(1, last_number + 1):
            result = current_number - int(player_input)
            return str(result)
        else:
            print('Введено некорректное число')
            print(last_number)
            self.__num_player(player_number, current_number)
        return f'pizda'
# --------------------------------------------------    
    def start_game(self):
        current_number = self.__number
        
        print(f'Загадано число {current_number}')
        
        while current_number is not None:
            current_number = int(self.__num_player(self.player_one, current_number))
            print(current_number)
            current_number = int(self.__num_player(self.player_two, current_number))
            print(current_number)
        return True
            
a = Game(player_one, player_two, difficult)

# print(a.get_difficult())
# print(a.answer_range)
# print(a.answer_between)
print(a.start_game())