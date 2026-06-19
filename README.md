# AI Text Generator (POO)

Aplicación desarrollada en Python que utiliza modelos de inteligencia artificial para generar textos automáticamente. El proyecto sigue la arquitectura MVC (Modelo–Vista–Controlador) y permite generar textos cortos, descripciones de productos, ideas de proyectos y resúmenes.

---

## Características

- Generación de textos cortos a partir de un prompt.
- Creación automática de descripciones de productos.
- Generación de ideas creativas para proyectos.
- Resumen automático de textos.
- Interfaz gráfica desarrollada con Gradio.
- Exportación de resultados a archivos de texto.
- Pruebas básicas utilizando PyTest.

---

## Tecnologías utilizadas

- Python 3.x
- Transformers
- Gradio
- PyTest

---

## Estructura del proyecto

```text
AITextGenerator/
│
├── controllers/
│   └── text_controller.py
│
├── models/
│   └── text_generator.py
│
├── views/
│   └── app.py
│
├── exports/
│   └── exporter.py
│
├── tests/
│   └── test_generator.py
│
├── docs/
│   ├── proceso_desarrollo.md
│   └── capturas/
│       ├── menu_principal.png
│       ├── funcionalidad.png
│       ├── pytest.png
│       └── github.png
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Instalación

1. Clonar o descargar el proyecto.

2. Crear un entorno virtual:

```bash
python -m venv .venv
```

3. Activar el entorno virtual:

### Windows

```bash
.venv\Scripts\activate
```


4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Uso

Ejecutar la aplicación:

```bash
python main.py
```

Se abrirá una interfaz web local donde podrás:

- Generar textos cortos.
- Crear descripciones de productos.
- Obtener ideas para proyectos.
- Resumir textos.

---

## Arquitectura MVC

### Modelo (Model)

La clase `TextGenerator` contiene la lógica de generación de texto utilizando la librería Transformers y el modelo distilgpt2.

### Vista (View)

La interfaz gráfica fue desarrollada con Gradio mediante pestañas para cada funcionalidad.

### Controlador (Controller)

La clase `TextController` conecta la interfaz con el modelo y procesa las solicitudes del usuario.

---

## Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

La prueba verifica que el método `generate_text()` retorna un valor de tipo texto (`str`).

---

## Autor

Michelle Mercado

Proyecto académico desarrollado para la asignatura de Programación Orientada a Objetos.
