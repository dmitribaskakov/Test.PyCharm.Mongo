import datetime
from uuid import uuid4
from storage import MongodbService


storage = MongodbService.get_instance()

for _ in range (5):
    dto = {
        "_id": str(uuid4()),
        "payload": str(uuid4()),
        "datetime": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    storage.save_data(dto)


for data in storage.get_data():
    print(data)
