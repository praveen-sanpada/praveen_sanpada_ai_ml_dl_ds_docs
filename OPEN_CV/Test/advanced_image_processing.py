import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# === Config ===
image_path = "flight.png"  # Change this if needed

# === Utility: Resize with Aspect Ratio ===
def resize_image(img, width=800):
    h, w = img.shape[:2]
    aspect_ratio = width / w
    new_dims = (width, int(h * aspect_ratio))
    return cv2.resize(img, new_dims, interpolation=cv2.INTER_AREA)

# === Load Image ===
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError(f"Image not found at: {image_path}")
img = resize_image(img)

# === Grayscale ===
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# === Gaussian Blur ===
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# === Canny Edge Detection ===
edges = cv2.Canny(blur, 100, 200)

# === Morphological Transformations ===
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
eroded = cv2.erode(dilated, kernel, iterations=1)

# === HSV Conversion ===
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# === Adaptive Thresholding ===
adaptive_thresh = cv2.adaptiveThreshold(gray, 255,
                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY,
                                        11, 2)

# === Sharpening Kernel ===
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, sharpen_kernel)

# === Contour Detection ===
contour_img = img.copy()
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

# === Histogram ===
def show_histogram(gray_image):
    plt.figure(figsize=(6, 3))
    plt.title("Grayscale Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.hist(gray_image.ravel(), bins=256, range=[0, 256])
    plt.tight_layout()
    plt.savefig("histogram.png")
    plt.close()

show_histogram(gray)

# === Save Outputs ===
output_dir = "processed_outputs"
os.makedirs(output_dir, exist_ok=True)

cv2.imwrite(f"{output_dir}/gray.jpg", gray)
cv2.imwrite(f"{output_dir}/blur.jpg", blur)
cv2.imwrite(f"{output_dir}/edges.jpg", edges)
cv2.imwrite(f"{output_dir}/dilated.jpg", dilated)
cv2.imwrite(f"{output_dir}/eroded.jpg", eroded)
cv2.imwrite(f"{output_dir}/adaptive_thresh.jpg", adaptive_thresh)
cv2.imwrite(f"{output_dir}/sharpened.jpg", sharpened)
cv2.imwrite(f"{output_dir}/contours.jpg", contour_img)

# === Display Key Stages ===
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Canny Edges", edges)
cv2.imshow("Contours", contour_img)
cv2.imshow("Sharpened", sharpened)

print("✅ All processed images saved in 'processed_outputs/'")
print("📊 Histogram saved as 'histogram.png'")
cv2.waitKey(0)
cv2.destroyAllWindows()
