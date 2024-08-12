import cv2
import os

# Step 1: Define the desired frame size
frame_width = 640  # Desired width
frame_height = 480  # Desired height

# Step 2: Load the video
video_path = 'sample.mp4'
cap = cv2.VideoCapture(video_path)

# Step 3: Create a directory to store the extracted frames
output_folder = 'extracted_frames'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 4: Resize the first frame to the desired size and allow ROI selection
ret, first_frame = cap.read()
if not ret:
    print("Error reading video")
    exit()

resized_first_frame = cv2.resize(first_frame, (frame_width, frame_height))
roi = cv2.selectROI("Select ROI", resized_first_frame, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()

# Step 5: Process the video frame by frame
frame_number = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame to the desired size
    resized_frame = cv2.resize(frame, (frame_width, frame_height))

    # Crop the frame to the selected ROI
    x, y, w, h = roi
    cropped_frame = resized_frame[y:y+h, x:x+w]

    # Save the cropped frame to the output folder
    frame_filename = f'frame_{frame_number}.jpg'
    frame_filepath = os.path.join(output_folder, frame_filename)
    cv2.imwrite(frame_filepath, cropped_frame)
    
    frame_number += 1

cap.release()
cv2.destroyAllWindows()

print(f"Frames extracted and saved in folder '{output_folder}'")
