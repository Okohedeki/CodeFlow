import inspect
import json
from TabNannyTest import check


if __name__ == '__main__':
    data = check('/home/okohedeki/Desktop/CodeFlow/SampleProject/backend/app.py')
    json_object = json.dumps(data, indent = 4) 
    print(json_object)