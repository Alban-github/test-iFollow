import cv2

def basic_cam_read():
    #fonction simple avec la video
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # save when using 'q' key , uncomment for step 2
            # cv2.imwrite("testing_webcam.jpg", frame)
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #decommenter si la camera fonctionne :
    #basic_cam_read()

    print("""
    Camera not working ! 
    Normally, follow these steps.
    Step 1 :
    openCV video capture
    Step 2 :
    imwrite on key
    Step 3 :
    use the same functions as in exercice5.py
    """)