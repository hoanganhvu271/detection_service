from flask import current_app 
def insert_new_dataset(data):
    collection = current_app.db.extended_datasets
    if collection.find_one({"package_id": data.get("package_id")}) is None:
        collection.insert_one(data)
        # print("Data inserted successfully.")
    else: 
        # print("Package ID already exists. No data inserted.")
   