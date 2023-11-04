import gradio as gr
import cv2
import tempfile
import base64


def capture_photo():
    
    cap = cv2.VideoCapture(0)    
    ret, frame = cap.read()
    cap.release()

    
    if ret:
        
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            cv2.imwrite(temp_file.name, frame)

        with open(temp_file.name, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode()

        return encoded_image
    else:
        return None


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Tabs() as tabs:
        with gr.TabItem("Learning Mode", id=0):
            t = gr.Textbox()
        with gr.TabItem("Game Mode", id=1):
            with gr.Row():   
                captured_image = gr.Image()
                def take_photo(): 
                    captured_image.image = capture_photo()

                

demo.launch()
