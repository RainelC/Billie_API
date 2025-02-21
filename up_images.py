import os 
from PIL import Image
from base64_conv  import *
from db import conexion_db
from dotenv import load_dotenv

def up_db(files):
    for file in files:
        fileid = fs.put(file, filename = "Billie pic")
        db.pictures.insert_one({
            "name": "Billie",
            "image": {
                "file_id": fileid,
                "alt": "Billie picture"
            }
        })

    return "listo"

db, fs, collection = conexion_db()

load_dotenv()
path = os.getenv("PATH")
pics_base64 = get_pic_base64(path)

# up_db(pics_base64)
