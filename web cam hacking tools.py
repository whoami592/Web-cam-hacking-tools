import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a frame from the webcam
ret, frame = cap.read()

# Check if the frame was captured correctly
if not ret:
    print("Error: Could not capture frame.")
    exit()

# Display the captured frame
cv2.imshow("Webcam", frame)

# Wait for a key press to close the window
cv2.waitKey(0)

# Release the webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()