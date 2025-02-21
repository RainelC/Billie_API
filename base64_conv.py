import os 
import base64

def base64_converter(path, namefile):
    with open(f"{path}/{namefile}", "rb") as pic_file:
        base64_pic = base64.b64encode(pic_file.read())
    return base64_pic

def get_pic_base64(path):
    pics = [picture for picture in os.listdir(path)]
    pics_base64 = list(map( lambda x : base64_converter(path,x), pics))
    return pics_base64

def b64_to_byte(b64):
    return base64.b64decode(b64)


