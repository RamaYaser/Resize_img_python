# project to Resize folder of imegs

import cv2 as cv
import os


def resize_img(input_folder, output_folder, size):
    list_img = os.listdir(input_folder)
    for img_name in list_img:
        if img_name.endswith(".png") or img_name.endswith(".jpg"):
            img_path = os.path.join(input_folder, img_name)
            img = cv.imread(img_path)
            img_resize = cv.resize(img, size)
            img_resize_path = os.path.join(output_folder, img_name)
            cv.imwrite(img_resize_path, img_resize)
            print("Resize of %s Done" % (img_name))
        else:
            print("%s is not image" % (img_name))


#example
input_folder = input("please inter the path of your input folder:")
output_folder = input("please inter the path of your output folder:")
w=int(input("please inter the new width"))
h=int(input("please inter the new hight"))
resize_img(input_folder, output_folder, (w,h))
