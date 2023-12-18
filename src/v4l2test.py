import cv2
from picamera2 import Picamera2
import os
import time

image_list = []
time_list = []
width  = 640 			#4608, 2304, 1536. 1153, 640,, 1152     1240
height = 480			#2592, 1296,  864,  648, 360,,  864      930
folder_path = "/tmp/img"
#folder_path = "/home/airpocket/Workspace/picamera2_test/img"



if not os.path.exists(folder_path):
    # フォルダが存在しない場合は作成
    os.makedirs(folder_path)
    print(f'{folder_path}を作成しました。')
else:
    print(f'{folder_path}は既に存在しています。')

#camera = Picamera2()
#camera.configure(camera.create_preview_configuration(lores={"size":(320,180)},display="lores"))
#camera.configure(camera.create_preview_configuration(queue=False,main={"size": (width,height)},lores={"size":(320, 180)},encode="lores"))
#camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (width, height)}))
#preview_config = camera.create_preview_configuration(queue=False)
#camera.configure(camera.create_preview_configuration(main={"size": (width, height)}))
#camera.configure(camera.create_preview_configuration(main={"size":(2304,1296)}))
#camera.start()
capture = cv2.VideoCapture(0, cv2.CAP_V4L2)

for i in range(1000):
	start_time = time.time()
	ret, image = capture.read()
	print(ret)
	#image = camera.capture_array()
	#image = cv2.resize(image,(640,360))
	#image_list.append(camera.capture_array())
	#image_list.append(cv2.resize(camera.capture_array(),(640,480)))
	#print(type(image))
	#image_list.append(image)
	#image_list.append(camera.capture_array())
	cv2.imwrite(folder_path + "/test" + str(width) + "x" + str(height) + "_" + str(i) + ".jpg", image)
	#cv2.imwrite(folder_path + "/test" + str(width) + "x" + str(height) + "_" + str(i) + ".jpg", cv2.resize(camera.capture_array(),(640,480)))	
	elapsed_time = time.time() - start_time
	print("i = " + str(i) + " / time = " + str(elapsed_time))
	#time_list.append(elapsed_time)
	#time.sleep(0.1)
	i += 1
print(time_list)
print(elapsed_time)
