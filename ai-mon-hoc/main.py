import io
import os

import nest_asyncio
import uvicorn
# from PIL import Image
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
# from coreai.tichHop import Vgg16DetectFace
from rete import tinhluong
import numpy as np

load_dotenv()
# HOST = os.getenv("HOST")
app = FastAPI()
LIST_BANG_CAP = ["Cử nhân", "Thạc sĩ", "Tiến sĩ", "Phó giáo sư", "Giáo sư", "Khác"]
# vgg = Vgg16DetectFace()
# vgg.LoadModel()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    soBuoiDay: float
    phiGuiXe: float
    thuongThem: float
    chucVu: str
    khoa: str
    namKinhNghiem: int
    thoiGianLamViec: int
    bangCap: str


class Item2(BaseModel):
    image: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/tinhLuong/")
def read_item(item: Item):
    
    print(item)
    
    luong = tinhluong(item.phiGuiXe,
                      item.thuongThem,
                      item.chucVu,
                      item.khoa,
                      item.namKinhNghiem,
                      item.thoiGianLamViec,
                      item.bangCap,
                      item.soBuoiDay)
    
    return {
        "luong": luong
    }





# def getAndDeCodeImage(data):
#     file_bytes = np.asarray(bytearray(data), dtype=np.uint8)
#     img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
#     return img


# def stringToRGB(base64_string):
#     imgdata = base64.b64decode(str(base64_string))
#     image = Image.open(io.BytesIO(imgdata))
#     return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)


# def encodeImage(image):
#     retval, buffer = cv2.imencode('.jpg', image)
#     jpg_as_text = base64.b64encode(buffer)
#     return jpg_as_text


# @app.post("/deAndRecorg/")
# async def create_file(
#         request: Request,
#         data: Item2,
# ):
#     img = stringToRGB(data.image.split(",")[1])
#     data = vgg.predictFace(img)
#     data['image'] = "data:image/jpg;base64," + encodeImage(data['image']).decode('utf-8')
#     return data


# PORT = 8000
# ngrok_tunnel = ngrok.connect(PORT)
# print('Public URL:', ngrok_tunnel.public_url)
# nest_asyncio.apply()
# uvicorn.run(app, host=HOST, port=PORT)
# uvicorn.run(app, host=HOST, port=PORT)
# uvicorn.run(app, port=PORT)
