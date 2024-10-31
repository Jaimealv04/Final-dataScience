# Proyecto de Predicción con XGBoost

### Desarrollado por: Jaime Alvarez de Neyra y Antonio Salinas

Este proyecto implementa un modelo de predicción utilizando **XGBoost**, integrado con una interfaz de usuario construida en **Gradio**. El objetivo es realizar predicciones basadas en datos de entrada suministrados por el usuario a través de esta interfaz gráfica.

---

## Tabla de Contenidos
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instrucciones para Ejecutar el Proyecto](#instrucciones-para-ejecutar-el-proyecto)
- [Usando Docker](#usando-docker)
- [Sin Docker](#sin-docker)

---

## Estructura del Proyecto

## Requisitos

- **Docker**
- **Python 3.10**

---

## Instrucciones para Ejecutar el Proyecto

### Usando Docker

1. **Construir la imagen de Docker:**

    ```sh
    docker build -t prediccion-xgboost .
    ```

2. **Ejecutar el contenedor:**

    ```sh
    docker run -p 7860:7860 prediccion-xgboost
    ```

3. **Abrir el navegador** y acceder a [http://localhost:7860](http://localhost:7860) para interactuar con la interfaz de Gradio.

---

### Sin Docker

1. **Crear un entorno virtual:**

    ```sh
    python -m venv venv
    ```

2. **Activar el entorno virtual**:

   - En **Windows**:
     ```sh
     .\venv\Scripts\activate
     ```
   - En **macOS/Linux**:
     ```sh
     source venv/bin/activate
     ```

3. **Instalar las dependencias**:

    ```sh
    pip install -r app/requirements.txt
    ```

4. **Ejecutar la aplicación sin Docker**:

    ```sh
    python app/main.py
    ```

5. **Abrir el navegador** y acceder a [http://localhost:7860](http://localhost:7860) para utilizar la interfaz de Gradio.

---

### Ejecución alternativa con Docker

Si deseas montar un directorio específico en el contenedor para mantener datos o cambios locales, utiliza:

```sh
docker build -t final_data_science .
docker run -p 7860:7860 -v /ruta/a/tu/directorio:/app final_data_science
```


