import os
import cv2
from tqdm import tqdm
from pathlib import Path, PureWindowsPath
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--videoFolder', type=str, default=r"D:\Ali Waqas\Projects\Drone\backup_laptop\anafi_backup\errors",
                    help='full path of path of folder containing videos')
parser.add_argument('--outFolder', type=str, default="", help='output folder to store images')
parser.add_argument('--fps', type=int, default=0, help='frames to output per second.')

class VideoToImages:
    def __init__(self, config):
        self.videoFolder = PureWindowsPath(r"{}".format(config.videoFolder))
        self.files = [file for file in os.listdir(self.videoFolder) if file.endswith(".mp4") or file.endswith(".MP4")]
        self.outFolder = config.outFolder


        if len(config.outFolder) == 0:
            self.outFolder = os.path.join(self.videoFolder, "imagesConverted")
            try:
                print(f"saving images to : {self.outFolder}")
                os.mkdir(self.outFolder)
            except OSError:
                print("Creation of the directory %s failed" % self.outFolder)
            else:
                print("Successfully created the directory %s " % self.outFolder)

        self.run()
    def run(self):
        print("Starting conversion")
        for file in self.files:
            print(f"converting file: {file}")
            vidcap = cv2.VideoCapture(os.path.join(self.videoFolder, file))
            frameCount = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
            success, image = vidcap.read()
            for i in tqdm(range(frameCount-1)):
                if not success:
                    break
                cv2.imwrite(os.path.join(self.outFolder, f"{file}_{i}.png"), image)
                success, image = vidcap.read()


def main():
    print("hello World!")
    VideoToImages(parser.parse_args())

if __name__ == '__main__':
    main()