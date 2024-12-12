import gradio as gr
from main import main_func


def greet(name):
    return main_func(name).content


with gr.Blocks() as demo:
    name = gr.Textbox(label="User Linkedin Profile")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Click to fetch")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

if __name__ == "__main__":
    demo.launch()
