import pandas as pd
import json
import math

def get_pythagoras(x, y):
    return math.sqrt(x ** 2 + y ** 2)

with open("YourFilepath") as json_data:
    data = json.load(json_data)
full_dataset = pd.DataFrame(data['_notes'])
full_dataset['_yCenter'] = full_dataset.loc[:, ('_lineLayer')].apply(lambda x: 1 + x * 0.55)
full_dataset['_xCenter'] = full_dataset.loc[:, ('_lineIndex')].apply(lambda x: -0.9 + x * 0.6)
left = (full_dataset[full_dataset['_type'] == 0]) #All left handed notes
right = (full_dataset[full_dataset['_type'] == 1]) #All right handed notes

left['_xMovement'] = left.loc[:, ['_xCenter']].diff().fillna(0)
left['_yMovement'] = left.loc[:, ['_yCenter']].diff().fillna(0)
left['_totMovement'] = left.apply(lambda x: get_pythagoras(x['_xMovement'], x['_yMovement']), axis=1).fillna(0) 
left['_angleChange'] = left.apply(lambda x: math.atan(x['_yMovement']/x['_xMovement']), axis=1)

right['_xMovement'] = right.loc[:, ['_xCenter']].diff().fillna(0)
right['_yMovement'] = right.loc[:, ['_yCenter']].diff().fillna(0)
right['_totMovement'] = right.apply(lambda x: get_pythagoras(x['_xMovement'], x['_yMovement']), axis=1).fillna(0)
right['_angleChange'] = right.apply(lambda x: math.atan(x['_yMovement']/x['_xMovement']), axis=1)


average_angle = (left['_angleChange'].mean() + right['_angleChange'].mean()) / 2
time = (full_dataset['_time'].max() - full_dataset['_time'].min())
total_distance= (left['_totMovement'].sum() + right['_totMovement'].sum()) / 2
average_speed = total_distance/time


complexity_speed= average_speed/2
complexity_angle= average_angle/30

complexity = complexity_angle + complexity_speed

print(complexity)