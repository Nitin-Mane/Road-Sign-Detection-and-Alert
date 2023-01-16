# Road-Sign-Detection-and-Alert

## Introduction

This project aims to develop a real-time road sign detection system using a Raspberry Pi and a camera module. The system will be able to detect common road signs such as stop signs, speed limit signs, and yield signs. When a road sign is detected, the system will trigger an LED to alert the user.

## Hardware Requirements
- Raspberry Pi 4
- Camera module
- LED
- Breadboard
- Jumper wires
- Software Requirements
- Python 3
- OpenCV
- TensorFlow

## Installation
Install Raspbian OS on your Raspberry Pi.

Install the following packages:

```
sudo apt-get update
sudo apt-get install python3-opencv
pip3 install tensorflow
```

Clone the repository to your Raspberry Pi using the following command:

```
git clone https://github.com/Nitin-Mane/Road-Sign-Detection-and-Alert.git
```

Connect the camera module, LED and breadboard to the Raspberry Pi as per the circuit diagram provided.

Run the python script by using the command:
```
python3 main.py
```

## Usage
The script will start capturing images from the camera and using the trained model to predict the road sign, if the sign is detected the LED will be turned on, else it will be off.

## Contributing
We welcome contributions to this project. If you have an idea for a feature or improvement, feel free to create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- OpenCV
- Tensorflow