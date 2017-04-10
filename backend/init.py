import pymongo
from config import config, RUN_LEVEL
from tdata import plane, task, person, image

FLAG_DB_CLEAN = True

# Mongo Client
mg_cl = pymongo.MongoClient(config[RUN_LEVEL].MONGO_HOST,
                            config[RUN_LEVEL].MONGO_PORT)
# Database - winhye
mg_db = mg_cl.winhye

# Collection - image | task | record
mg_image = mg_db.image
mg_task = mg_db.task
mg_plane = mg_db.plane
mg_person = mg_db.person

if FLAG_DB_CLEAN:
    mg_image.remove()
    mg_task.remove()
    mg_plane.remove()
    mg_person.remove()

for item in image:
    mg_image.insert(item)

for item in task:
    mg_task.insert(item)

for item in plane:
    mg_plane.insert(item)

for item in person:
    mg_person.insert(item)