import cv2

filter_index = 0

def switchFilter(arrow, image, filter_index):
    print("Received function")
    input_image_path = image
    bgr_image = cv2.imread(input_image_path)

    if arrow == 97:  # Go back with 'a' key
        if filter_index <= 0:
            filter_index = 5
        else:
            filter_index -= 1
    elif arrow == 100:  # Go forward with 'd' key
        if filter_index >= 5:
            filter_index = 0
        else:
            filter_index += 1
    
    match filter_index:
        case 0:
            # Original
            print("case 0 met")
            cv2.imshow("Captured Image", mirror_frame)
        case 1:
            print("case 1 met")
            # BGR to RGB
            rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
            cv2.imshow("Captured Image", rgb_image)
        case 2:
            print("case 2 met")
            # BGR to Grayscale
            gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Captured Image", gray_image)
        case 3:
            print("case 3 met")
            # BGR to HSV
            hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
            cv2.imshow("Captured Image", hsv_image)
        case 4:
            print("case 4 met")
            # BGR to LAB
            lab_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2LAB)
            cv2.imshow("Captured Image", lab_image)
        case 5:
            print("case 5 met")
            # Invert
            inverted_image = cv2.bitwise_not(bgr_image)
            cv2.imshow("Captured Image", inverted_image)
    return filter_index


# Initialize camera -- 0 is default code for webcam
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Cannot open camera")
    exit()

# Displays live (mirrored) video until spacebar is pressed to capture image
# Or until escape key is pressed to exit
# "a" and "d" keys rotate through filters on captured image

while True:
    check, frame = cam.read()
    mirror_frame = cv2.flip(frame, 1)
    cv2.imshow('Mirrored Video', mirror_frame)

    key = cv2.waitKey(1)

    if key == 27:
        print("Exiting Photo Booth")
        break

    if key == 32:
        print("Photo taken")
        cv2.imwrite("captured_image.jpg", mirror_frame)
        cv2.imshow("Captured Image", mirror_frame)
        key = cv2.waitKey(0)
        if key == 97 or key == 100:
            while key == 97 or key == 100:
                print("Received arrow")
                filter_index = switchFilter(key, "captured_image.jpg", filter_index)
                key = cv2.waitKey(0)


cam.release()
cv2.destroyAllWindows()