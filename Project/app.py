import cv2
import mediapipe as mp
import numpy as np
import gradio as gr

mp_selfie = mp.solutions.selfie_segmentation

def segment(image):
    with mp_selfie.SelfieSegmentation(model_selection=0) as model:
        res = model.process(image)
        mask = np.stack((res.segmentation_mask,)*3, axis=-1) > 0.5
        return np.where(mask, image, cv2.blur(image, (40, 40))

# Create a Gradio input for the webcam feed
webcam = gr.inputs.Camera()

# Create a Gradio output for the segmented image
output_image = gr.outputs.Image(type="pil")

# Define a Gradio interface with the segment function
webapp = gr.Interface(
    fn=segment,
    inputs=webcam,
    outputs=output_image,
)

# Launch the Gradio interface within the Jupyter notebook
webapp.launch()
