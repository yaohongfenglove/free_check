import gradio as gr


def main():
    with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.blue),
                   title="FreeCheck") as app:
        gr.Markdown("# <center>FreeCheck")
        with gr.Tab("文章原创度检测"):
            ele_input_text = gr.Textbox()
            ele_button = gr.Button("提交", variant="primary")
        with gr.Tab("文本相似度计算"):
            ele_input_text1 = gr.Textbox()
            ele_input_text2 = gr.Textbox()
            ele_button12 = gr.Button("提交", variant="primary")

    app.launch()


if __name__ == '__main__':
    main()
