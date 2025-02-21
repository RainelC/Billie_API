from fastapi import FastAPI, Response
from base64_conv import b64_to_byte
from db import *
import random

app = FastAPI()

@app.get('/')
async def root():
    pictures = list(map(lambda x : fs.get(file_id=x['image']['file_id']).read() , list(db.pictures.find({}))))
    image_byte = b64_to_byte(random.choice(pictures))
    return Response(content=image_byte, media_type="image/jpg")


db, fs, collection = conexion_db()