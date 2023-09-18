# Background Remover

This Python code removes the background of an image using OpenCV.

## How to use

1. Install the required dependencies:

pip install cv2


2. Run the code:

```python
import cv2
import numpy as np

input_image = cv2.imread("input_image.jpg")

grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

contours = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
largest_contour = max(contours, key=cv2.contourArea)

mask = np.zeros(input_image.shape, dtype=np.uint8)
cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), -1)

foreground = cv2.bitwise_and(input_image, input_image, mask=mask)

cv2.imwrite("output_image.jpg", foreground)
Dependencies
OpenCV (>= 4.5.5)
License
This code is licensed under the MIT License.
