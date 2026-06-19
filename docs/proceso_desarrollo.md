Proceso de desarrollo
1. Idea inicial

El proyecto nació con la idea de crear una herramienta sencilla capaz de generar distintos tipos de textos usando inteligencia artificial. El objetivo principal fue automatizar tareas como la creación de descripciones de productos, generación de ideas y elaboración de resúmenes de manera rápida.

2. Análisis del problema

La aplicación está dirigida a estudiantes, emprendedores o cualquier usuario que necesite generar contenido de forma ágil. Busca facilitar la creación de textos sin requerir conocimientos avanzados en inteligencia artificial.

3. Diseño de la solución

Se utilizó la arquitectura MVC (Modelo–Vista–Controlador) para organizar el proyecto:

Modelo: TextGenerator, encargado de interactuar con el modelo de IA.
Controlador: TextController, responsable de procesar las solicitudes del usuario y coordinar el flujo de datos.
Vista: interfaz gráfica desarrollada con Gradio.

El flujo de la aplicación consiste en que el usuario introduce un texto en la interfaz, el controlador lo procesa, el modelo genera la respuesta y el resultado se muestra en pantalla.

4. Implementación

El proyecto fue desarrollado en Python, utilizando la librería Transformers de Hugging Face y el modelo distilgpt2.
La interfaz gráfica se implementó con Gradio, lo que permitió construir una aplicación web funcional de manera rápida y sencilla.

5. Pruebas

Se implementó una prueba básica con PyTest para verificar que el método de generación de texto devolviera un resultado de tipo str. La prueba se ejecutó correctamente, confirmando el funcionamiento básico del sistema.

6. Dificultades encontradas

Durante el desarrollo se presentaron algunos retos:

Configuración del entorno virtual y dependencias.
Tiempo de carga del modelo en la primera ejecución.
Comprensión e implementación de la arquitectura MVC.
Manejo de rutas de archivos y ejecución de pruebas.
7. Mejoras futuras

Una de las principales limitaciones del proyecto es el uso del modelo distilgpt2, el cual es ligero y funcional, pero no siempre genera textos completamente coherentes o con calidad profesional.

En futuras versiones, se propone la integración de modelos más avanzados como GPT-2 completo, GPT-J o modelos más recientes basados en transformers, con el objetivo de mejorar la coherencia, naturalidad y calidad de los textos generados.

También se podría implementar fine-tuning con datasets específicos según la tarea (descripciones de productos, resúmenes o generación de ideas), lo que permitiría obtener resultados más precisos y adaptados al contexto.