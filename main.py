import time
from uuid import uuid4
from storage import MongodbService


storage = MongodbService.get_instance()

for _ in range (5):
    dto = {
        "_id": str(uuid64()),
        "payload": str(uuid64())
    }
    storage.save_data(dto)


for data in storage.get_data():
    print(data)
