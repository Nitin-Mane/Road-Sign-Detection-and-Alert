import cv2
import tensorflow as tf
import numpy as np
import RPi.GPIO as GPIO
import time

#Set up the LED pin
led_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

#Load the TensorFlow model for road sign detection
model = tf.keras.models.load_model('roadsign_model.h5')

#Set up the camera
camera = cv2.VideoCapture(0)

while True:
    #Capture an image from the camera
    ret, image = camera.read()

    #Resize the image to match the model's input size
    image = cv2.resize(image, (32, 32))
    image = np.expand_dims(image, axis=0)

    #Use the model to predict the class of the road sign
    predictions = model.predict(image)

    #Check if the model predicts a road sign
    if np.argmax(predictions) == 1:
        #Turn on the LED
        GPIO.output(led_pin, True)
    else:
        #Turn off the LED
        GPIO.output(led_pin, False)

    #Show the image on the screen
    cv2.imshow("Road Sign Detection", image)

    #Wait for the user to press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Clean up
camera.release()
cv2.destroyAllWindows()
GPIO.cleanup()
