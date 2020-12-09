"""
Saves a series of snapshots with the current camera as snapshot_<width>_<height>_<nnn>.jpg

Buttons:
    q           - quit
    space bar   - save the snapshot


"""

import cv2
import argparse
import os

__author__ = "Sidharth S"
__date__ = "09/12/2020"


def save_snaps(width=1280, height=720, name="snapshot", folder="G:\Final Year Project\calib_pics"):

    url = "http://10.0.0.9:8080/video"
    cap = cv2.VideoCapture(url)
    if width > 0 and height > 0:
        print("Setting the custom Width and Height")
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
            # ----------- CREATE THE FOLDER -----------------
            folder = os.path.dirname(folder)
            try:
                os.stat(folder)
            except:
                os.mkdir(folder)
    except:
        pass

    nSnap = 0
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fileName = "%s/%s_%d_%d_" % (folder, name, w, h)
    while True:
        ret, frame = cap.read()

        cv2.imshow('camera', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord(' '):
            print("Saving image ", nSnap)
            cv2.imwrite("%s%d.jpg" % (fileName, nSnap), frame)
            nSnap += 1

    cap.release()
    cv2.destroyAllWindows()


def main():
    # ---- DEFAULT VALUES ---
    SAVE_FOLDER = "."
    FILE_NAME = "snapshot"
    FRAME_WIDTH = 1280  #default value
    FRAME_HEIGHT = 720

    # ----------- PARSE THE INPUTS -----------------

    save_snaps()

    print("Files saved")


if __name__ == "__main__":
    main()
