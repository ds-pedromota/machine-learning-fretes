```markdown
# 🚀 Previsão de Custos de Frete para E-commerce (End-to-End)

Este projeto de Ciência de Dados resolve um problema de negócio real no setor do e-commerce: a dependência de APIs externas (como a dos Correios) para o cálculo do custo de envio. 

Através da utilização de dados históricos, desenvolvi um modelo de *Machine Learning* capaz de prever o valor do frete com base nas características do produto, logística e sazonalidade, culminando no *deploy* de uma API REST pronta para ser integrada em aplicações de *front-end* ou sistemas de gestão.

## 🎯 O Problema e a Solução
* **Problema:** Empreendedores de e-commerce enfrentam dificuldades em prever custos de envio quando os serviços postais falham ou estão indisponíveis, afetando a conversão de vendas.
* **Solução:** Uma API baseada num modelo preditivo treinado com dados da Olist, que calcula o valor do frete instantaneamente a partir das dimensões do pacote e da localização do cliente/vendedor.

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem:** Python
* **Análise e Tratamento de Dados:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn, XGBoost, LightGBM, CatBoost, Optuna (para otimização de hiperparâmetros)
* **Engenharia de Software / Deploy:** FastAPI, Uvicorn, Pydantic, Joblib

## 🧠 Arquitetura do Projeto
O projeto está dividido em duas fases principais:

1. **Exploração e Modelagem (Jupyter Notebook):**
   - Extração de múltiplos *datasets* do [Kaggle Brazilian E-commerce by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
   - Limpeza de dados nulos e tratamento de *outliers*.
   - **Feature Engineering:** Criação de variáveis cruciais como `Volume`, `Densidade` e cálculo de `Distância` (em km) entre o vendedor e o cliente, além de variáveis temporais (`black_friday`, `natal`).
   - Validação cruzada com `KFold` para garantir a robustez do modelo.

2. **Deploy da API (FastAPI):**
   - Estruturação de um endpoint `POST /prever-frete` para receber os dados via JSON.
   - Tratamento dinâmico de tipos de dados (conversão de *strings* para categorias compatíveis com o XGBoost).
   - Retorno do valor final em Reais (BRL).

## 📊 Principais Resultados (Métricas)
Durante a validação cruzada do modelo final, obtivemos uma performance estável com as seguintes métricas médias:
* **MAE (Erro Médio Absoluto):** ~ 5.70
* **MSE (Erro Quadrático Médio):** ~ 121.50
* **R² (Coeficiente de Determinação):** ~ 0.52

*(Nota: O R² de 0.52 é um ponto de partida sólido considerando a alta variabilidade dos custos logísticos no Brasil, havendo espaço para melhorias futuras com a inclusão de dados de transportadoras privadas).*

## 💻 Como executar o projeto localmente

1. Clone o repositório:
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)

```

2. Entre na diretoria da API:

```bash
cd api

```

3. Instale as dependências necessárias:

```bash
pip install fastapi uvicorn pandas joblib xgboost

```

4. Inicie o servidor local:

```bash
uvicorn main:app --reload

```

5. Aceda à documentação interativa (Swagger) no seu navegador para testar o modelo:
👉 **https://www.google.com/search?q=http://127.0.0.1:8000/docs**

## 👨‍💻 Autor

**Desenvolvido por Jp.Mota** Para saber mais sobre o meu trabalho e outros projetos onde uno o desenvolvimento de sistemas à ciência de dados, visite o meu portefólio:

🌐 [https://dspedroportfolio.vercel.app/](https://dspedroportfolio.vercel.app/)

```

