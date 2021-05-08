import cv2
from detect import detect, Arguments

frame = cv2.imread('.\sample\sample.jpg')

opt = Arguments(source=frame, nosave=True)

proc_frame, output, class_names = detect(opt)

cv2.imshow('Processed frame', proc_frame)
cv2.waitKey(0)

labels = [[class_names[int(line[0])], line[1], line[2], line[3], line[4]] for line in output]