import cv2


def take_frame():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imwrite("webcamphoto.png", frame)
    cam.release()


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        print(x, ' ', y)
        b = image[y, x, 0]
        g = image[y, x, 1]
        r = image[y, x, 2]
        print(r, g, b)
        if r <= 255 and g >= 0 and b >= 0 and r >= 65 and g <= 75 and b <= 100:
            print("red")
        elif r <= 100 and g >= 0 and b >= 120 and r >= 0 and g <= 100 and b <= 255:
            print("blue")
        elif r <= 255 and g >= 175 and b >= 175 and r >= 175 and g <= 255 and b <= 255:
            print("white")
        elif r <= 255 and g >= 0 and b >= 50 and r >= 60 and g <= 219 and b <= 255:
            print("pink")
        elif r >= 0 and g >= 0 and b >= 0 and r <= 65 and g <= 65 and b <= 65:
            print("black")
        elif r >= 0 and g >= 35 and b >= 75 and r <= 165 and g <= 255 and b <= 250:
            print("turquoise")
        elif r >= 0 and g >= 60 and b >= 0 and r <= 175 and g <= 255 and b <= 180:
            print("green")
        elif r >= 66 and g >= 76 and b >= 0 and r <= 255 and g <= 255 and b <= 150:
            print("yellow")
        elif r >= 66 and g >= 76 and b >= 0 and r <= 255 and g <= 255 and b <= 150:
            print("orange`")


savedOrCamera = input("Do you want to use a saved image or take an image from your webcam ")
savedOrCamera = savedOrCamera.lower()
if savedOrCamera == "saved image":
    image = cv2.imread("colours.png")
elif savedOrCamera == "webcam":
    take_frame()
    image = cv2.imread("webcamphoto.png")

image = cv2.resize(image, (1047, 432))
cv2.imshow("image", image)
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
