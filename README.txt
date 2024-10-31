# Proyecto de Predicción con XGBoost Hecho por Jaime Alvarez de Neyra y Antonio Salinas

Este proyecto utiliza un modelo de XGBoost para realizar predicciones basadas en datos de entrada proporcionados a través de una interfaz de usuario construida con Gradio.

## Estructura del Proyecto
## Requisitos

- Docker
- Python 3.10

## Instrucciones para Ejecutar el Proyecto

### Usando Docker

1. Construir la imagen de Docker:

    ```sh
    docker build -t prediccion-xgboost .
    ```

2. Ejecutar el contenedor:

    ```sh
    docker run -p 7860:7860 prediccion-xgboost
    ```

3. Abrir tu navegador y acceder a `http://localhost:7860` para usar la interfaz de Gradio.

### Sin Docker

1. Crear un entorno virtual:

    ```sh
    python -m venv venv
    ```

3. Instalar las dependencias:

    ```sh
    pip install -r app/requirements.txt
    ```

4. Ejecutar la aplicación:

    ```sh
    python app/app.py
    ```

5. Abrir tu navegador y acceder a `http://localhost:7860` para usar la interfaz de Gradio.

