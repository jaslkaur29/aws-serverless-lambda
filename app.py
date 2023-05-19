import boto3
import pandas as pd
def handler(event, context):
  print(event)
  data_set = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
  }
  tab_data = pd.DataFrame(data_set)

  print(tab_data)