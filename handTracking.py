import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


def getFinger(thummb_cords, index_cords, middle_cords, ring_cords, pinky_cords):

    if index_cords==sorted(index_cords,reverse=True):
        return "I"
    elif middle_cords==sorted(middle_cords,reverse=True):
        return "M"
    elif ring_cords==sorted(ring_cords,reverse=True):
        return "R"
    elif pinky_cords==sorted(pinky_cords,reverse=True):
        return "P"
    elif thummb_cords==sorted(thummb_cords,reverse=True):
        return "T"
    else:
        return "None"

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    # checking whether a hand is detected
    thummb_cords = []
    index_cords = []
    middle_cords = []
    ring_cords = []
    pinky_cords = []
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand

            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if 1<=id<=4:
                    thummb_cords.append(cy)
                elif 5<=id<=8:
                    index_cords.append(cy)
                elif 9<=id<=12:
                    middle_cords.append(cy)
                elif 13<=id<=16:
                    ring_cords.append(cy)
                elif 17<=id<=20:
                    pinky_cords.append(cy)

                else:
                    pass

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)


        finger = getFinger(thummb_cords, index_cords, middle_cords, ring_cords, pinky_cords)
        
        cv2.putText(image,finger,(100,30),cv2.FONT_HERSHEY_PLAIN,1.2,(0,0,0),2)

    cv2.imshow("Output", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break



