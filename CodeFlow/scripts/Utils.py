import inspect
import json
from tokenize import String
from tracemalloc import start
from TabNannyTest import check
import subprocess
import os
import time

from itertools import islice
from typing import Iterator


def changes(lst: list) -> Iterator[int]:

    logic_groups = []
    for index, (current, next) in enumerate(zip(lst, islice(lst, 1, None))):
        if current != next and current == 0:
            start_value = index + 1

        elif current != next and next == 0 :
            end_value = index + 1
            logic_groups.append([start_value, end_value])

            start_value, end_value = '', ''

        elif current == next and current != 0:
            continue
        
        elif current == next and current == 0:
            logic_groups.append([index])

    return logic_groups

def depthIndex(filename: String) -> list:
    indentation = []
    indentation.append(0)
    depth = 0
    data = [[]]
    code_groupings = []
    
    f = open(filename, 'r')


    for index, line in enumerate(f):
        line = line[:-1]

        content = line.strip()
        indent = len(line) - len(content)
        if indent > indentation[-1] and content != '':
            depth += 1
            indentation.append(indent)
            data.append([])

        elif indent < indentation[-1] and content != '':
            while indent < indentation[-1]:
                depth -= 1
                indentation.pop()
                top = data.pop()
                data[-1].append(top)

        data[-1].append(index+1)
        code_groupings.append((depth, index))
    
    f.close()

    #adding blank line at end of file to indent goes back to 0 if needed. 
    max_index = code_groupings[-1][1]
    code_groupings.append((0,max_index+1))    


    while len(data) > 1:
        top = data.pop()
        data[-1].append(top)

    only_depth = [i[0] for i in code_groupings]
    return only_depth

def createLogicGroups(filename: String, depth_list: list) -> list:
        logic_group_list = []
        f = open(filename)
        new_f = f.readlines()
        for index, i in enumerate(depth_list):
            if len(i) == 1:
                logic_group = new_f[i[0]]
                logic_group_list.append([logic_group])
            elif len(i) == 2:
                logic_group = new_f[i[0]-1:i[1]]
                logic_group_list.append(logic_group)
        f.close()
        return logic_group_list

if __name__ == '__main__':

    filename = '/home/okohedeki/Desktop/CodeFlow/SampleProject/backend/app.py'

    only_depth = depthIndex(filename)

    depth_index = changes(only_depth)
    logic_groups = createLogicGroups(filename, depth_index)

    for x in logic_groups:
        print(x)