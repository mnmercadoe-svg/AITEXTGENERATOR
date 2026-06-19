from models.text_generator import TextGenerator

class TextController:
    # Inicializamos el modelo de generación de texto
    def __init__(self):
        self.model = TextGenerator()

    # Genera un texto corto a partir de un prompt dado
    def short_text(self, prompt):
        return self.model.generate_text(prompt, 80)

    # Genera una descripción de producto
    def product_description(self, product):
        return self.model.generate_text(
            f"Write a professional product description for: {product}",
            100
        )

    # Genera ideas creativas para proyectos
    def project_ideas(self, topic):
        return self.model.generate_text(
            f"Give 5 creative project ideas about: {topic}",
            120
        )

    # Resume un texto de forma clara
    def summarize(self, text):
        return self.model.generate_text(
            f"Summarize clearly this text: {text}",
            100
        )