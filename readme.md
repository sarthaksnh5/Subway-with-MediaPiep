# Subway Surfers with Mediapipe

This project involves the usage of mediapipe library and opencv. This project aims to make a person move who loves to play game on screen but also want to do physical exercise.

## `Code`

Code consist of two files, one is `Pose Detector` class file which is doing major of the work. Another is the `main.py` file which is doing camera stream and parsing.

## `Working`

Your camera stream is divided in 2 compartments both vertical and horizontal and your nose movements will be followed. When your nose is in the 
1. `up` region then it will jump
1. `down` region then it will duck
1. `left` region then it will left lane
1. `right` region then it will right lane

## `How to Start`

1. Open [Subway Sufers](https://poki.com/en/g/subway-surfers)
2. Install the required libraries by running follwing command
> pip install -r requirements.txt
3. After the successful installation of all the libraries, run
> python main.py
4. It will start a live stream of the camera of your pc.

## `Example`
<video width="320" height="240" controls>
  <source src="subway_mediapipe.mp4" type="video/mp4">
</video>