from fastapi import FastAPI, Response
from base64_conv import b64_to_byte
import uvicorn
from db import *
import random

app = FastAPI()

@app.get('/')
async def root():
    pictures = list(map(lambda x : fs.get(file_id=x['image']['file_id']).read() , list(db.pictures.find({}))))
    image_byte = b64_to_byte(random.choice(pictures))
    return Response(content=image_byte, media_type="image/jpg")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


db, fs, collection = conexion_db()