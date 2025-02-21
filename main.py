from fastapi import FastAPI, Response
from base64_conv import b64_to_byte
import uvicorn
from db import *

app = FastAPI()

@app.get('/')
def root():
    picture = fs.get(file_id=db.pictures.aggregate([{"$sample":{"size":1} }]).next()["image"]["file_id"]).read()
    image_byte = b64_to_byte(picture)
    return Response(content=image_byte, media_type="image/jpg")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


db, fs, collection = conexion_db()