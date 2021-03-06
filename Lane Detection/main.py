from __future__ import division

import cv2

import track
import detect
#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument("--path", type=str, help="Video path")

def main():
    cap = cv2.VideoCapture('videoplayback2.mp4')

    ticks = 0

    lt = track.LaneTracker(2, 0.1, 500)
    ld = detect.LaneDetector(180)
    while cap.isOpened():
        precTick = ticks
        ticks = cv2.getTickCount()
        dt = (ticks - precTick) / cv2.getTickFrequency()

        ret, frame = cap.read()

        predicted = lt.predict(dt)

        lanes = ld.detect(frame)

        if predicted is not None:
            cv2.line(frame, (predicted[0][0], predicted[0][1]), (predicted[0][2], predicted[0][3]), (0, 0, 255), 5)
            cv2.line(frame, (predicted[1][0], predicted[1][1]), (predicted[1][2], predicted[1][3]), (0, 0, 255), 5)

        lt.update(lanes)

        cv2.imshow('', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    #args = parser.parse_args()
    main()