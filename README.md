```markdown
# 🚚 Previsão de Custos de Frete (End-to-End)
*Da coleta de dados ao deploy da API REST*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)

---

## 🎯 O Problema e a Solução

* **Problema:** Empreendedores de e-commerce enfrentam dificuldades em prever custos de envio quando os serviços postais (como a API dos Correios) falham ou estão indisponíveis, afetando a conversão de vendas.
* **Solução:** Uma API baseada num modelo preditivo de *Machine Learning* treinado com dados reais da Olist, capaz de calcular o valor do frete instantaneamente a partir das dimensões do pacote e da localização.

## 🧠 Arquitetura do Projeto
O projeto foi construído cobrindo todo o ciclo de vida dos dados:

### 1. Exploração e Modelagem (Jupyter Notebook)
- Extração e unificação de múltiplos *datasets* do [Kaggle Brazilian E-commerce by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
- Tratamento de nulos e remoção de *outliers* de preço e frete.
- **Feature Engineering:** Cálculo de `Volume`, `Densidade`, `Distância` (em km) entre vendedor e cliente, e variáveis sazonais (`black_friday`, `natal`).
- Treino e validação cruzada (`KFold`) utilizando algoritmos avançados (XGBoost, LightGBM, CatBoost).

### 2. Deploy e Engenharia de Software (FastAPI)
- Construção de um endpoint `POST /prever-frete`.
- Conversão dinâmica e validação rigorosa de *features* (tipagem de dados e conversão para categorias do Pandas exigidas pelo modelo).

## 📊 Principais Resultados (Métricas)
A validação cruzada em 5 *folds* apresentou uma performance consistente do modelo, obtendo as seguintes médias:
* **MAE (Erro Médio Absoluto):** ~ 5.71
* **MSE (Erro Quadrático Médio):** ~ 121.56
* **R² (Coeficiente de Determinação):** ~ 0.52

> *Nota: O R² de 0.52 é um baseline sólido, considerando a alta volatilidade e as diferentes políticas de preços das transportadoras no Brasil.*

---

## 💻 Como executar o projeto localmente

**1. Clone o repositório e entre na pasta da API:**
```bash
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd api

```

**2. Instale as dependências:**

```bash
pip install fastapi uvicorn pandas joblib xgboost pydantic

```

**3. Inicie o servidor local:**

```bash
uvicorn main:app --reload

```

**4. Teste no navegador (Swagger UI):**
Acesse `http://127.0.0.1:8000/docs` e utilize o JSON abaixo no endpoint **POST** para testar a previsão:

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

## 👨‍💻 Autor

**Desenvolvido por Jp.Mota**

Acompanhe o meu portfólio para ver mais projetos onde a engenharia de sistemas encontra a ciência de dados:
🌐 [Acessar Portfólio](https://dspedroportfolio.vercel.app/)