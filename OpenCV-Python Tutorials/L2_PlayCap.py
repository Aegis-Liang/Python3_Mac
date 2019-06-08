import cv2

cap = cv2.VideoCapture('output.mov')

while(cap.isOpened()):
    ret, frame = cap.read()

    # add checking whether ret is true, otherwise will occur an error like this in cvtColor function:
    # cv2.error: OpenCV(4.1.0) ../modules/imgproc/src/color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor'
    gray = None
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
