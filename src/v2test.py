import cv2
from picamera2 import Picamera2
import os

width  = 1920 
height = 1080
folder_path = "/tmp/img"

if not os.path.exists(folder_path):
    # フォルダが存在しない場合は作成
    os.makedirs(folder_path)
    print(f'{folder_path}を作成しました。')
else:
    print(f'{folder_path}は既に存在しています。')


camera = cv2.VideoCapture(0)
#camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (width, height)}))
#camera.start()
let, image = camera.read()
print(let)
print(image)

#cv2.imwrite(folder_path + "/test" + str(width) + "x" + str(height) + ".jpg", image)
