#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Дана хэш-таблица ваших знакомых первого и второго уровня и словарь с профессиями.
Нужно найти самого ближайшего знакомого — продавца яблок.
"""

import collections


graph = {'you': ['alice', 'bob', 'claire'],
         'bob': ['anuj', 'peggy'],
         'alice': ['peggy'],
         'claire': ['thom', 'jonny'],
         'anuj': [],
         'peggy': [],
         'thom': [],
         'jonny': []
         }

profession = {'alice':'writer',
              'bob':'doctor',
              'claire':'receptionist',
              'anuj':'baker',
              'peggy':'apple seller',
              'thom':'teacher',
              'jonny':'artist'}


def search_apple_seller(graph, start_point, target): 
    visited = set()
    queue = collections.deque([start_point])
    visited.add(start_point)
    counter = 0
    while queue:
        element = queue.popleft()
        counter += 1
        for i in graph[element]:
            if i not in visited: 
                visited.add(i) 
                queue.append(i)
                if profession[i] == target:
                    queue.clear()
                    print(f'{i} is our {target}')
                    print(f'{counter} step to {i}')
            

if __name__ == '__main__':
        search_apple_seller(graph, 'you', 'apple seller')  