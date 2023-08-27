# Hand Tracking using OpenCV and Mediapipe

This repository contains a Python script that utilizes the OpenCV and Mediapipe libraries to perform hand tracking using your computer's webcam.

## Installation

Before running the script, make sure you have the following libraries installed:

1. OpenCV
2. Mediapipe

You can install these libraries using the following commands:

```bash
pip install opencv-python
pip install mediapipe
```

## Usage

1. Clone this repository to your local machine or download the provided code.

2. Run the script using the following command:

```bash
python hand_tracking.py
```

3. A window will open displaying the webcam feed with hand landmarks drawn on the detected hands.

4. Press the 'Esc' key to exit the application.

## How It Works

The script performs the following steps:

1. It captures video from the default webcam (index 0).

2. The webcam feed is flipped horizontally and converted from BGR to RGB format for better visualization.

3. The `Hands` class from Mediapipe is used to process the video frames and detect hand landmarks.

4. If hands are detected in the frame, landmarks are drawn on the hands using the `mp_drawing.draw_landmarks` function.

5. The processed frame is displayed in a window named "Handtracker".

6. The application continues to run until the 'Esc' key is pressed.

## Credits

This code is based on the OpenCV and Mediapipe libraries. Credits to their respective developers.

## License

This project is licensed under the [MIT License](LICENSE).

