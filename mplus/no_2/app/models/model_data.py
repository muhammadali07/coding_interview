from schematics.models import Model
from bson import ObjectId
from schematics.types import StringType
import connection
class MasterData(Model):
    user_id = ObjectId()
    nama_category = StringType(required=True)
    jenis_category = StringType(required=True)

newdata = MasterData()

def create_new_data(nama_category, jenis_category):
    newdata.user_id = ObjectId()
    newdata.nama_category = nama_category
    newdata.jenis_category = jenis_category

def data_exist(nama_category):
    data_exist = True
    if connection.db.master_pulsa.find({'nama_category': nama_category}).count() == 0:
        data_exist = False
        return data_exist