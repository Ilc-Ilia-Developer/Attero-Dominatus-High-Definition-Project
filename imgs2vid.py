import cv2
import os
import sys
from tqdm import tqdm

def images_to_video(input_folder, output_video_path, fps=30):
    image_files = os.listdir(input_folder)

    first_image = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width, _ = first_image.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for i in tqdm(range(len(image_files))):
        image_file = image_files[i]
        image_path = os.path.join(input_folder, image_file)
        frame = cv2.imread(image_path)
        out.write(frame)

    out.release()
    print(f"Created video {output_video_path}.")

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("Too many arguements. Expected a video path and an output directory.")
    elif len(sys.argv) < 3:
        print("Too few arguements. Expected a video path and an output directory.")
    else:
        images_to_video(sys.argv[2], sys.argv[1])