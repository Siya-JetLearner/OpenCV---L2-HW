import cv2
import numpy as np

# Load your own image
image = cv2.imread("my_image.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# 1. ADDITION
added = cv2.add(image, 50)
cv2.imshow("Addition", added)

# 2. SUBTRACTION
subtracted = cv2.subtract(image, 50)
cv2.imshow("Subtraction", subtracted)

# 3. RESIZING
resized = cv2.resize(image, (300, 300))
cv2.imshow("Resized Image", resized)

# 4. EROSION
kernel3 = np.ones((3, 3), np.uint8)
kernel5 = np.ones((5, 5), np.uint8)
kernel7 = np.ones((7, 7), np.uint8)

erosion3 = cv2.erode(image, kernel3, iterations=1)
erosion5 = cv2.erode(image, kernel5, iterations=1)
erosion7 = cv2.erode(image, kernel7, iterations=1)

cv2.imshow("Erosion 3x3", erosion3)
cv2.imshow("Erosion 5x5", erosion5)
cv2.imshow("Erosion 7x7", erosion7)

# 5. GAUSSIAN BLUR
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Gaussian Blur", gaussian)

# 6. MEDIAN BLUR
median = cv2.medianBlur(image, 7)
cv2.imshow("Median Blur", median)

# 7. BILATERAL FILTER
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("Bilateral Filter", bilateral)

# 8. BORDERING
border = cv2.copyMakeBorder(
    image,
    30, 30, 30, 30,
    cv2.BORDER_CONSTANT,
    value=(0, 255, 0)
)

cv2.imshow("Bordered Image", border)

# SAVE ALL RESULTS
cv2.imwrite("addition.jpg", added)
cv2.imwrite("subtraction.jpg", subtracted)
cv2.imwrite("resized.jpg", resized)
cv2.imwrite("erosion3.jpg", erosion3)
cv2.imwrite("erosion5.jpg", erosion5)
cv2.imwrite("erosion7.jpg", erosion7)
cv2.imwrite("gaussian.jpg", gaussian)
cv2.imwrite("median.jpg", median)
cv2.imwrite("bilateral.jpg", bilateral)
cv2.imwrite("border.jpg", border)

# CLOSE WINDOWS
cv2.waitKey(0)
cv2.destroyAllWindows()

print("All image manipulations completed!")