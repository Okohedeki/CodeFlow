import inspect
import json
from tracemalloc import start
from TabNannyTest import check
import subprocess
import os
import time


indentation = []
indentation.append(0)
depth = 0
data = [[]]
code_groupings = []

f = open('/home/okohedeki/Desktop/CodeFlow/SampleProject/backend/app.py', 'r')


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


while len(data) > 1:
    top = data.pop()
    data[-1].append(top)

current_depth = 0
for i in range(0, len(code_groupings)):

    if code_groupings[i][0] == 0:
        continue
        #print(code_groupings[i][0], code_groupings[i][1])

    else:
        start_line_num = code_groupings[i-1][1]
        print(start_line_num)

                
        
        


#print(data[0])
# for i in data[0]:
#     if isinstance(i+1, list):

# def groupLogic(indent_json, len_json):
#     final_logic_grouping = {}
#     current_count = 0
#     del indent_json['MetaData']
#     for i in range(0, len_json - 1):
#         if indent_json[i]['string_indent_level'] == 'newLine' and current_count == 0:
#             final_logic_grouping['line_start'] = indent_json[i]['lineNo']
#             final_logic_grouping['line_end'] = indent_json[i]['lineNo']

#         elif indent_json[i]['string_indent_level'] == 'indent':
#             current_count += 1

#         elif indent_json[i]['string_indent_level'] == 'dedent':
#             current_count -= 1


#     # for item in json_object:
#     #     print(item)

# if __name__ == '__main__':
#     data = check('/home/okohedeki/Desktop/CodeFlow/SampleProject/backend/app.py')
#     len_data = data['MetaData']['len']
#     groupLogic(data, len_data)
#     #universal-ctags --output-format=json --fields="*" -R backend/app.py > test.json
    
#     #os.system("universal-ctags --output-format=json --fields=""a+e+E+f+m+i+F+K+Z+l+n+P+r+s+Z+p+S+t"" -R ../../SampleProject/backend/app.py > test.json")
#     #print(Logical_indent_json[0])