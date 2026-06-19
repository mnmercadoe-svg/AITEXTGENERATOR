from transformers import pipeline

class TextGenerator:
    # Inicializamos el modelo de generación de texto usando Hugging Face
    def __init__(self):
        # Usamos un modelo liviano (distilgpt2) para generar texto
        self.generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )

    # Método principal que genera texto a partir de un prompt
    def generate_text(self, prompt, max_length=80):
        # Llamamos al modelo para generar texto
        result = self.generator(
            prompt,
            max_new_tokens=max_length,  # cantidad máxima de tokens nuevos
            do_sample=True,             # permite generación aleatoria
            temperature=0.7,            # controla creatividad (más alto = más creativo)
            top_p=0.9,                  # nucleus sampling (mejora coherencia)
            repetition_penalty=1.2,     
            pad_token_id=50256         
        )

        # Retornamos solo el texto generado (sin metadatos)
        return result[0]["generated_text"]