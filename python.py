import cv2

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load image
image = cv2.imread(r"your image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sample data - you can modify this with real data
face_info = [
    {"name": "your_name", "age": your age},
    # Add more entries for each face you expect to detect
]

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles and add text for detected faces
for (x, y, w, h), info in zip(faces, face_info):
    # Draw rectangle
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Add name and age text
    text = f"{info['name']}, {info['age']}"
    cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display result
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

