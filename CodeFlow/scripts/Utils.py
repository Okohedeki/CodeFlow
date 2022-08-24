import inspect
import json
from TabNannyTest import check
import subprocess
import os


if __name__ == '__main__':
    #data = check('/home/okohedeki/Desktop/CodeFlow/SampleProject/backend/app.py')
   # Logical_indent_json = json.dumps(data, indent = 4) 


    #universal-ctags --output-format=json --fields="*" -R backend/app.py > test.json
    
    os.system("universal-ctags --output-format=json --fields=""a+e+E+f+m+i+F+K+Z+l+n+P+r+s+Z+p+S+t"" -R ../../SampleProject/backend/app.py > test.json")
    #print(Logical_indent_json[0])