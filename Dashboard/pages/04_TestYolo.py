import streamlit as st
import os
import subprocess
from tempfile import NamedTemporaryFile
import glob

# Streamlit configuration
st.title("YOLOv5 Video Detector")
st.markdown("Upload a video and run YOLOv5 for object detection.")

# Upload video
video_upload = st.file_uploader("Upload a video", type=["mp4", "avi"])

# YOLOv5 command
yolov5_command = "python yolov5-master/detect.py --source {}"

if video_upload:
    with NamedTemporaryFile(delete=False, suffix='.mp4') as video_file:
        # Save the uploaded video
        video_file.write(video_upload.read())
        video_path = video_file.name

    # Run YOLOv5 on the uploaded video
    st.write("Running YOLOv5 on the video... This may take some time.")
    try:
        result = subprocess.run(yolov5_command.format(video_path), shell=True, capture_output=True, text=True, check=True)
        st.write(result.stdout)
        st.write("Video Saved Successfully")
    except subprocess.CalledProcessError as e:
        st.error("An error occurred while running YOLOv5. Please check your video and YOLOv5 setup.")

    # Find the latest experiment folder
    latest_exp_folder = max(glob.glob('yolov5-master/runs/detect/exp*'), key=os.path.getctime)
    
    # List files in the latest experiment folder
    exp_files = os.listdir(latest_exp_folder)
    
    # Find the output video file
    output_video = None
    for exp_file in exp_files:
        if exp_file.endswith(".mp4"):
            output_video = os.path.join(latest_exp_folder, exp_file)
            break
    
    if output_video:
        # Display the processed video
        # with open(output_video, "rb") as video_file:
        #     video_bytes = video_file.read()
        # st.video(video_bytes, format="video/mp4")
        video_bytes = output_video.read()
        st.video(video_bytes, 'rb')
        # Provide a download link for the video
        #st.markdown(f"[Download Processed Video](data:video/mp4;base64,{video_bytes.hex()})")
    else:
        st.warning("No output video found in the latest experiment folder.")
    
    # Clean up the temporary video file
    os.remove(video_path)
else:
    st.warning("Please upload a video to get started.")
