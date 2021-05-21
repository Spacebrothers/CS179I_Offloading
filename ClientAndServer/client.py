import cv2
import socket

Host = '128.110.155.82'
Port = 65432
camera = cv2.VideoCapture(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

if not camera.isOpened():
    raise IOError("Cannot open webcam")

while True:
    try:
        ret, frame = camera.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)
        data, buf = cv2.imencode('.jpg', frame)

        s.sendall(buf)
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break
    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
s.close()
