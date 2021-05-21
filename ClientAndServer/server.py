import cv2
import socket
import numpy as np

HOST = '128.110.155.82'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')

# bind and listen
s.bind((HOST, PORT))
print('Socket Binding Done')
s.listen()
print('Socket listening')

# accept connection
conn, address = s.accept()

# count images
a = 0
while True:
    try:
        data = conn.recv(4096)
        if not data:
            break
        image = np.frombuffer(data, dtype=np.uint8)
        frame = cv2.imdecode(image, cv2.COLOR_BGR2GRAY)

        colorName = "/Users/concop/mnt/data/Result{}.jpg".format(a)
        cv2.imwrite(colorName, frame)
        a = a + 1
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break
conn.close()
s.close()
