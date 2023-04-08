# What is Driver Monitoring System

### A driver-monitoring system — sometimes called a driver state sensing (DSS) system

## Features we need:
1. Driver-monitoring systems typically use a driver-facing camera equipped with infrared light-emitting diodes (LEDs) or lasers so that it can “see” the driver’s face.
2. We need to set a baseline for a driver to tell when he is being attentive
3. We want to give a percenatage value of how attentive a person is being. Inattentiviness could be due to a variety of reasons, drowsiness, inhibriation, etc.
4. We can make use various in vehicle features to grab the attention of the driver back:
    - Seat
    - Temperature 
    - Interior lights


## Our Current Solution: 

We create a passenger profile for every passenger that enters the vehicle, based on this info we can detect annomalies.

1. Install heart rate sensor on the stearing wheel.  
2. We install a camera system with the rear view mirror, this mirror can run a deep learning model that can detect and track the following:
    - Eye motion.
    - The head is tilting at an odd angle. // For this we make use of haarcascade in opencv
    - Blinking of the eye. 
    - Eyes are narrowing or closing. 
    - Yawn: Audio analysis / Image processing
3. IR camera to detect temprature of the temprature. 
     <b>Citation:</b> <i>Koukiou G. Intoxication Identification Using Thermal Imaging [Internet]. Human-Robot Interaction - Theory and Application. InTech; 2018. Available from: http://dx.doi.org/10.5772/intechopen.72128</i>


#### The Goal is to setup a graphing system with all these parameters, each parameter should be given a weight, based on which we can tell if if the deviation is off from the baseline.

<br>

### Eye Tracking system, we use an opencv based solution to detect the eyeball movement
<!-- ![Link Name](../image.png)  -->

### Face Tilt tracking




