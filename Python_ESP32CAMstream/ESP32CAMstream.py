import cv2
# ให้เปลี่ยนเป็น IP ของ ESP32-CAM เช่น http://192.168.1.100:81/stream
url = "http://192.168.0.100:81/stream"
cap = cv2.VideoCapture(url)
if not cap.isOpened():
    print("ไม่สามารถเชื่อมต่อกับ ESP32-CAM ได้")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("ไม่สามารถอ่านเฟรมได้")
        break
    cv2.imshow("ESP32-CAM Stream", frame)
    # กด 'q' เพื่อออกจากลูป
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
