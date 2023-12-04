import cv2
import os
import sys
from tqdm import tqdm

def video_to_images(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0
    #while True:
    for i in tqdm(range(length)):
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        img_name = str(frame_count).zfill(8)
        frame_filename = os.path.join(output_folder, f"{img_name}.png")
        cv2.imwrite(frame_filename, frame)

    cap.release()
    print(f"Created frames in {video_path}.")

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Too many arguements. Expected a video path and an output directory.")
    elif len(sys.argv) < 3:
        print("Too few arguements. Expected a video path and an output directory.")
    else:
        video_to_images(sys.argv[1], sys.argv[2])