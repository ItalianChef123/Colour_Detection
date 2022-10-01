import cv2


def take_frame():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite("webcamphoto.png", frame)
    cam.release()


savedOrCamera = input("Do you want to use a saved image or take an image from your webcam ")
savedOrCamera = savedOrCamera.lower()
if savedOrCamera == "saved image":
    image = cv2.imread("image.png")
elif savedOrCamera == "webcam":
    take_frame()
    image = cv2.imread("webcamphoto.png")


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str(x) + ", " + str(y), (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow("image", image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(x, ' ', y)
        b = image[y, x, 0]
        g = image[y, x, 1]
        r = image[y, x, 2]
        print(r, g, b)
        if r <= 255 and g >= 0 and b >= 0 and r >= 100 and g <= 75 and b <= 100:
            print("red")
        elif r <= 175 and g >= 20 and b >= 0 and r >= 0 and g <= 200 and b <= 200:
            print("blue")
        elif  r <= 255 and g >= 130 and b >= 130 and r >= 130 and g <= 255 and b <= 255:
            print("white")


image = cv2.resize(image, (1047, 432))
cv2.imshow("image", image)
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
