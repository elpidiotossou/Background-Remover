import tensorflow as tf
from tensorflow.keras.applications import DeepLabV3Plus
import cv2

input_image = cv2.imread("add3.jpg")
input_image = cv2.resize(input_image, (512, 512))
input_image = tf.expand_dims(input_image, axis=0)

model = DeepLabV3Plus(weights='pascal_voc')
prediction = model.predict(input_image)

segmentation_mask = tf.argmax(prediction, axis=-1)
segmentation_mask = segmentation_mask[0, :, :, 0]
foreground = input_image[0, :, :, :][segmentation_mask == 1]

cv2.imwrite("output_image.jpg", foreground)
