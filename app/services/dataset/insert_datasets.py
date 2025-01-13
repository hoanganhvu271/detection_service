from flask import current_app 
def insert_new_dataset(data):
    # Insert data into the database
    current_app.db.extended_datasets.insert_one(data)
    # print(data)