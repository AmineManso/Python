import cv2

width, height = 640, 480
cap = cv2.VideoCapture(0)

path = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(path)

while True:
    success, img = cap.read()
    imgGray = cv2_cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1, 4); print(faces)
    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow(img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#################
# img = cv2.imread("face.jpg")
# # img = cv2.resize(img, (300, 500))
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# faces = faceCascade.detectMultiScale(imgGray,1.1, 4); print(faces)
# for (x, y, w, h) in faces:
#     print(x, y, w, h)
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2_imshow(img)
# cv2.waitKey(0)

# #############
# while True:
#     success, img = cap.read()
#     imgResult = img.copy()
#     findColor(img, myColors, myColorValues)
#     cv2.imshow("Webcam", imgResult)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break