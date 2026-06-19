import gradio as gr
from controllers.text_controller import TextController

# Creamos el controlador principal que maneja la generación de texto
controller = TextController()

# Funciones puente entre la interfaz y el controlador
def ui_short(x):
    return controller.short_text(x)

def ui_product(x):
    return controller.product_description(x)

def ui_ideas(x):
    return controller.project_ideas(x)

def ui_summary(x):
    return controller.summarize(x)

# Construcción de la interfaz gráfica con Gradio
with gr.Blocks(title="AI Text Generator POO") as app:

    # Título principal de la app
    gr.Markdown("# 🧠 AI Text Generator (POO)")

    # Pestaña para generar textos cortos
    with gr.Tab("✍️ Text"):
        inp = gr.Textbox(label="Prompt")
        out = gr.Textbox()
        gr.Button("Generate").click(ui_short, inp, out)

    # Pestaña para generar descripciones de productos
    with gr.Tab("📦 Product"):
        inp = gr.Textbox(label="Product")
        out = gr.Textbox()
        gr.Button("Generate").click(ui_product, inp, out)

    # Pestaña para generar ideas de proyectos
    with gr.Tab("💡 Ideas"):
        inp = gr.Textbox(label="Topic")
        out = gr.Textbox()
        gr.Button("Generate").click(ui_ideas, inp, out)

    # Pestaña para generar resúmenes de texto
    with gr.Tab("📝 Summary"):
        inp = gr.Textbox(label="Text")
        out = gr.Textbox()
        gr.Button("Generate").click(ui_summary, inp, out)

# Ejecuta la aplicación web
app.launch()