import gradio as gr
import xgboost as xgb
import pandas as pd

model = xgb.Booster()
model.load_model('models/Modelo_2.bst')

model_columns = [
    'rfc_cliente', 'rfc_deudor', 'id_division_deudor', 'tipo_cliente', 'giro_cliente', 
    'id_division_documento', 'num_zona', 'pedido', 'id_c_deudor', 'id_c_cliente', 
    'contra_recibo', 'id_c_anomalia', 'status', 'id_c_moneda', 'id_c_tipo_localidad', 
    'id_c_ruta', 'importe_documento', 'saldo_documento', 'dias_credito', 'num_visitas', 
    'fecha_recibida_aeesa', 'fecha_reprogramacion', 'fecha_revision', 'fecha_inserta', 
    'fecha_deposito', 'fecha_anomalia'
]

def realizar_prediccion(file):
    input_df = pd.read_csv(file.name)

    for col in input_df.select_dtypes(include=['object']).columns:
        input_df[col] = input_df[col].astype('category')

    input_df = input_df[model_columns]
    input_df = input_df.fillna(0)

    dmatrix = xgb.DMatrix(input_df, enable_categorical=True)
    prediccion = model.predict(dmatrix)
    return prediccion.tolist()

interfaz = gr.Interface(
    fn=realizar_prediccion,
    inputs=gr.inputs.File(label="Sube tu archivo CSV"),
    outputs="text",
    title="Modelo de Predicción",
    description="Aplicación para predecir resultados utilizando un modelo de XGBoost"
)

interfaz.launch()

