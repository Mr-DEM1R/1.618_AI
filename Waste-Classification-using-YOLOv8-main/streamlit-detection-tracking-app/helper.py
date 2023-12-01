

from ultralytics import YOLO
import streamlit as st
import cv2
import pafy
import pickle
import settings

#loaded_model=pickle.load(open('C:/Users/MY PC/Desktop/yolov8/yolov8-streamlit-detection-tracking/weights/yolov8.pkl', 'rb'))
with open('/Users/mehmetomer/Desktop/Waste-Classification-using-YOLOv8-main/streamlit-detection-tracking-app/weights/yolov8(1).pkl', 'rb') as file:
    model1= pickle.load(file)



def load_model(model_path):
  
    model = YOLO('streamlit-detection-tracking-app/weights/yoloooo.pt')
    return model


def display_tracker_options():
    is_display_tracker = st.checkbox("Display Tracker")
    
    if is_display_tracker:
        tracker_type = st.radio("Tracker", ("bytetrack.yaml", "botsort.yaml"))
        return is_display_tracker, tracker_type
    
    return is_display_tracker, None


def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """

    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image, conf=conf)

    # # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )

