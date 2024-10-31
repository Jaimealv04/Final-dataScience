FROM python:3.10-slim

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir pandas==1.5.3 numpy==1.23.5 seaborn==0.12.2 matplotlib==3.7.1 xgboost==1.7.6 scikit-learn==1.2.2 gradio==2.3.6
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "app.py"]
