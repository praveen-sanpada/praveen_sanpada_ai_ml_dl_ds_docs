import cv2
import numpy as np

# 1. Load the image
image_path = "flight.png"  # Replace with your image
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

# 2. Resize the image
resized_img = cv2.resize(img, (600, 400))

# 3. Convert to Grayscale
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# 4. Apply Gaussian Blur
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# 5. Edge Detection using Canny
edges = cv2.Canny(blurred_img, 100, 200)

# 6. Draw rectangle and circle
annotated_img = resized_img.copy()
cv2.rectangle(annotated_img, (50, 50), (200, 200), (255, 0, 0), 2)  # Blue rectangle
cv2.circle(annotated_img, (300, 200), 50, (0, 255, 0), 3)           # Green circle

# 7. Show all images
cv2.imshow("Original", resized_img)
cv2.imshow("Grayscale", gray_img)
cv2.imshow("Blurred", blurred_img)
cv2.imshow("Edges (Canny)", edges)
cv2.imshow("Annotated Image", annotated_img)

# 8. Save final result
cv2.imwrite("output_edges.jpg", edges)
cv2.imwrite("output_annotated.jpg", annotated_img)

print("✅ Processing completed. Press any key to exit.")
cv2.waitKey(0)
cv2.destroyAllWindows()
