import cv2
import pytesseract

def get_text_from_frame(frame):
    # Convert the frame to grayscale for better OCR performance
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use Tesseract OCR to detect text in the frame
    text = pytesseract.image_to_string(gray_frame)

    return text

def main():
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Detect text from the current frame
        text_detected = get_text_from_frame(frame)
        print(text_detected)

        # Display the text on the frame
        cv2.putText(frame, text_detected, (500, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Text Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
