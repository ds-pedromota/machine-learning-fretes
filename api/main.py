from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Inicializar a aplicação FastAPI
app = FastAPI(
    title="API de Previsão de Frete Olist",
    description="Prevê o custo de envio com base nas características do produto, logística e datas."
)

# 2. Carregar o modelo treinado na memória
# Certifique-se de que o ficheiro 'modelo_frete.pkl' está na mesma pasta
modelo = joblib.load('modelo_frete.pkl')

# 3. Definir a estrutura exata dos dados (Features) que o modelo espera
class DadosProduto(BaseModel):
    price: float
    product_category_name: str
    product_weight_g: float
    product_length_cm: float
    product_height_cm: float
    product_width_cm: float
    customer_city: str
    customer_state: str
    review_score: float
    seller_city: str
    seller_state: str
    Volume: float
    densidade: float
    Velocidade_entrega_real: float
    Velocidade_entrega_estimada: float
    velocidade_processamento: float
    distancia: float
    mes_compra: int
    dia_semana_compra: int
    black_friday: int
    natal: int

# 4. Rota principal (Raiz) - Apresenta o seu portefólio
@app.get("/")
def home():
    return {
        "mensagem": "Bem-vindo à API de Previsão de Fretes Olist. Aceda a /docs para testar o modelo.",
        "assinatura": "Desenvolvido por Jp.Mota.",
        "portfolio": "https://dspedroportfolio.vercel.app/"
    }

# 5. Rota de previsão (POST)
@app.post("/prever-frete")
def prever(dados: DadosProduto):
    # Converter o JSON recebido num DataFrame de uma linha
    df_entrada = pd.DataFrame([dados.dict()])
    
    # CORREÇÃO XGBOOST: Converter as strings puras para o tipo 'category' do Pandas
    colunas_categoricas = [
        'product_category_name', 
        'customer_city', 
        'customer_state', 
        'seller_city', 
        'seller_state'
    ]
    
    for coluna in colunas_categoricas:
        # Força o tipo de dados para categoria, que é o que o XGBoost exige
        df_entrada[coluna] = df_entrada[coluna].astype('category')
    
    # Fazer a previsão com o modelo
    previsao = modelo.predict(df_entrada)
    
    # Retornar o resultado formatado em Reais, junto com os seus créditos
    return {
        "frete_estimado_brl": round(float(previsao[0]), 2),
        "desenvolvido_por": "Jp.Mota",
        "portfolio": "https://dspedroportfolio"
        }