import gradio as gr

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Tabs() as tabs:
        with gr.TabItem("Learning Mode", id=0):
            t = gr.Textbox()
        with gr.TabItem("Game Mode", id=1):
            i = gr.Image()
            
demo.launch()