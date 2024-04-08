import cv2

video = cv2.VideoCapture(1)
sucess, frame = video.read()

while sucess:
    cv2.imshow('frame', frame)

    if cv2.waitkey(1) == ord('q'):  #press 'q' to close the window
        break
    sucess, frame = video.read()

video.release()
cv2.destroyAllWindows()