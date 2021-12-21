import pandas as pd
from pathlib import Path
from os import walk
import os
import json
from pymongo import MongoClient




def connect_database():
    client = MongoClient('localhost', 27017)
    db = client['assemblee']
    return db['votes']

votes_table = connect_database()
path = Path(__file__).parent / "../data/votes/"

for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r') as f: # open in readonly mode
        print(filename)
        try:
            file_data = json.load(f)
            votes_table.insert_one(file_data)
        except:
            pass # doing nothing on exception

        #df.scrutin.syntheseVote.to_csv(os.path.join(path, 'synthese' + df.scrutin.uid) + '.csv', index = None)
