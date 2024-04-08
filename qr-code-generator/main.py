import qrcode
import cv2
import webbrowser

def scan_detect_qr_codes():
    video = cv2.VideoCapture(1)
    sucess, frame = video.read()
    detector = cv2.QRCodeDetector()

    while sucess:
        url, coords, pixels = detector.detectAndDecode(frame)
        if url:
            webbrowser.open(url)
            break

        cv2.imshow('frame', frame)

        if cv2.waitkey(1) == ord('q'):  #press 'q' to close the window
            break
        sucess, frame = video.read()

    video.release()
    cv2.destroyAllWindows()

def create_qr_code():
    img = qrcode.make('https://google.com')
    img.save('qr1.png')

def create_multiple_qr_codes():
    with open('urls.txt') as file:
        lines = file.readlines()
        count = 1
    for line in lines:
        img = qrcode.make(line)
        img.save(f"{count}.png")
        count += 1