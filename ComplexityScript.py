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
full_dataset['_xMovement'] = full_dataset.loc[:, ['_xCenter']].diff()
full_dataset['_yMovement'] = full_dataset.loc[:, ['_yCenter']].diff()
full_dataset['_totMovement'] = full_dataset.apply(lambda x: get_pythagoras(x['_xMovement'], x['_yMovement']), axis=1) 
full_dataset['_angleChange'] = full_dataset.apply(math.atan(['_yMovement ']/['xMovement ']))
left = (full_dataset[full_dataset['_type'] == 0]) #All left handed notes
right = (full_dataset[full_dataset['_type'] == 1]) #All right handed notes

average_angle = full_dataset['_AngleChange'].mean()
time = (full_dataset['_time'].max() - full_dataset['_time'].min()).idxmax()
total_distance= full_dataset.groupby['_totMovement'].sum
average_speed = int(total_distance)/int(time)

complexity_speed= int(average_speed)/2
complexity_angle=int(average_angle)/30

complexity = int(complexity_angle) + int(complexity_speed)

print(complexity)