import cv2





# Setările camerei
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
cap.set(cv2.CAP_PROP_FPS, 36)


def video_camera():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Afișează frame-ul
        cv2.imshow("Video Feed", frame)

        # Așteaptă 1 ms pentru a verifica dacă utilizatorul apasă 'q' pentru a ieși
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Eliberare resurse
    cap.release()
    cv2.destroyAllWindows()



