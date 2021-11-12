import cv2
import numpy as np
import tensorflow as tf

from coreai.src.setting import IMAGE_WIDTH, IMAGE_HEIGHT, CLASS


class Vgg16DetectFace(object):
    def __init__(self):

        self.modelPath = 'C:/hieu/QuangHieuCode/WebstormProjects/hechuyengiapython/coreai/models/my_model'
        # self.model = tf.keras.models.load_model(self.modelPath)
        self.path = "C:/hieu/QuangHieuCode/WebstormProjects/hechuyengiapython/coreai/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(self.path)
        self.ImagePath = ""
        self.cap = cv2.VideoCapture(0)
        self.max_softmax_output = "0.0"

    def LoadModel(self):
        if self.modelPath:
            self.model = tf.keras.models.load_model(self.modelPath)

    # Truyền binary vào đây
    def getAndDeCodeImage(self, data):
        file_bytes = np.asarray(bytearray(data), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        return img

    def predictFace(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, 1.3, 5)
        name = ""
        for face in faces:
            x, y, w, h = face
            image = frame[y:y + h, x:x + w]
            # image = cv2.equalizeHist(image)

            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.equalizeHist(image)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # image[:, :, 0] = cv2.equalizeHist(image[:, :, 0])
            image = tf.convert_to_tensor(image, dtype=tf.float32)
            image = tf.image.resize(image, [IMAGE_WIDTH, IMAGE_HEIGHT])
            image /= 255.0
            image_x = tf.expand_dims(image, axis=0)
            pred = self.model.predict(image_x)
            # print(pred)
            num = np.argmax(pred)
            try:
                self.max_softmax_output = pred[0][num]
            except:
                pass
            item = CLASS[num]
            name = item["ten"]
            id_ = item["id"]
            # str(max_softmax_output)
            # print("OKOK234234234234234")
            # print("Tên là: ", name)
        print("            ---------------------------------                    ")
        if(name == ""): 
            result = dict()
            result["name"] = "Không nhận diện được"
            result["id"] = "0"
            result["image"] = frame
            return result
    
        cv2.putText(frame, name + " - " + str(self.max_softmax_output), (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 0, 0), 2, cv2.LINE_AA)
        print("Đây là: " + name)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        result = dict()
        result["name"] = name
        result["id"] = id_
        result["image"] = frame
        return result

# img = cv2.imread(
#     "C:/hieu/QuangHieuCode/WebstormProjects/hechuyengiapython/coreai/test_data/166691023_765671504140070_3083427628472309525_n.jpg")
