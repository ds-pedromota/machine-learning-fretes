```markdown
# Previsão de Custos de Frete (End-to-End)
*Da coleta de dados ao deploy da API REST*
```
<p>Projeto:</p>
<a href="https://colab.research.google.com/drive/1iMlZkeInbe6lCX9TETwLYcfTq8XP2qPb?usp=sharing" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" width="200"/>
</a>

<p>
  <p>Tecnologias usadas:</p>
  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-44B78B?style=for-the-badge)
![Missingno](https://img.shields.io/badge/Missingno-5C5C5C?style=for-the-badge)
![Summarytools](https://img.shields.io/badge/Summarytools-5C5C5C?style=for-the-badge)

![GeoPy](https://img.shields.io/badge/GeoPy-1E88E5?style=for-the-badge)
![Category Encoders](https://img.shields.io/badge/Category_Encoders-1E88E5?style=for-the-badge)

![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-172B4D?style=for-the-badge)
![LightGBM](https://img.shields.io/badge/LightGBM-F37626?style=for-the-badge)
![CatBoost](https://img.shields.io/badge/CatBoost-FFC000?style=for-the-badge&logoColor=black)

![Optuna](https://img.shields.io/badge/Optuna-4B8BBE?style=for-the-badge)
</p>

---
---
```
## O Problema e a Solução

* **Problema:** Empreendedores de e-commerce enfrentam dificuldades em prever custos de envio quando os serviços postais (como a API dos Correios) apresentam instabilidade ou indisponibilidade, o que afeta diretamente a conversão de vendas e a operação logística.
* **Solução:** Desenvolvimento de uma API baseada em um modelo preditivo treinado com dados reais da Olist. A aplicação é capaz de calcular o valor do frete de forma independente, utilizando variáveis como dimensões do pacote, categoria do produto e localização.

## Arquitetura do Projeto

O projeto documenta todo o pipeline de dados, estruturado nas seguintes etapas:

### 1. Exploração e Modelagem (Jupyter Notebook)
- Extração e unificação de múltiplos datasets do Kaggle Brazilian E-commerce by Olist.
- Limpeza de dados, tratamento de valores nulos e remoção de outliers nas variáveis de preço e frete.
- **Feature Engineering:** Cálculo numérico de Volume, Densidade e Distância (em km) entre vendedor e cliente, além da criação de variáveis temporais/sazonais (Black Friday, Natal).
- Treinamento de modelos de regressão (XGBoost, LightGBM, CatBoost) com otimização de hiperparâmetros e validação cruzada (KFold).

### 2. Deploy e Engenharia de Software (FastAPI)
- Construção de uma interface de comunicação via endpoint POST (`/prever-frete`).
- Implementação de validação rigorosa de payload utilizando Pydantic.
- Conversão dinâmica de tipagem de dados no back-end (casting de strings para representações categóricas do Pandas) para compatibilidade em tempo de execução com o modelo XGBoost serializado.

## Principais Resultados (Métricas)

A validação cruzada do modelo final (5 folds) apresentou estabilidade preditiva com as seguintes médias:
* **MAE (Erro Médio Absoluto):** ~ 5.71
* **MSE (Erro Quadrático Médio):** ~ 121.56
* **R² (Coeficiente de Determinação):** ~ 0.52

*Nota técnica: O R² de 0.52 estabelece um baseline aceitável para o escopo do projeto, justificado pela alta volatilidade logística e pelas diferentes políticas de precificação das transportadoras atuantes no mercado brasileiro.*

---

## Como executar o projeto localmente

**1. Clone o repositório e acesse a raiz da API:**
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd api

```

**2. Instale as dependências necessárias:**

```bash
pip install fastapi uvicorn pandas joblib xgboost pydantic

```

**3. Inicie o servidor ASGI localmente:**

```bash
uvicorn main:app --reload

```

**4. Teste a requisição no navegador (via Swagger UI):**
Acesse `http://127.0.0.1:8000/docs` e utilize o payload JSON abaixo no endpoint POST para validar a inferência do modelo:

```json
{
  "price": 120.50,
  "product_category_name": "cama_mesa_banho",
  "product_weight_g": 2000.0,
  "product_length_cm": 30.0,
  "product_height_cm": 20.0,
  "product_width_cm": 20.0,
  "customer_city": "sao paulo",
  "customer_state": "SP",
  "review_score": 4.5,
  "seller_city": "rio de janeiro",
  "seller_state": "RJ",
  "Volume": 12000.0,
  "densidade": 0.166,
  "Velocidade_entrega_real": 6.0,
  "Velocidade_entrega_estimada": 12.0,
  "velocidade_processamento": 1.0,
  "distancia": 430.5,
  "mes_compra": 11,
  "dia_semana_compra": 4,
  "black_friday": 1,
  "natal": 0
}

```

---

## Autor

**Desenvolvido por Jp.Mota**

Para analisar o código-fonte de outros projetos que integram desenvolvimento de sistemas e ciência de dados, acesse o portfólio:
[Acessar Portfólio](https://dspedroportfolio.vercel.app/)