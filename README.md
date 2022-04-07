# World Happines Report Regression Model

* [Badges](#badges)
* [Descrição do Projeto](#descrição-do-projeto)
* [Arquitetura do projeto](#arquitetura-do-projeto)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)

## BADGES

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## DESCRIÇÃO DO PROJETO

A regression model to predict the happiness level of the world. It uses the [WHR 2021 dataset](https://worldhappiness.report/ed/2021/).

> Note that the data used is not from Kaggle, because Kaggle's dataset does not have the original data, only the relative data.

## ARQUITETURA DO PROJETO

```
├── = Representa uma pasta no projeto

└── = Representa um arquivo

|├── analisys
|├── data
|├── docs
|├── src
| ├── data_preparation
| ├── lib
```

### **ANALISYS**

```
|├── analisys
```
- Responsável pela parte da pré-analise dos datasets
- A nível de analise é utilizado os Jupyter Notebooks

### **DATA**

```
|├── data
```
- Diretório destinado aos datasets

### **DOCS**

```
|├── docs
```
- Documentações do projeto

### **SRC**

```
|├── src
```
- Contém os arquivos de lógica do projeto

### **DATA PREPARATION**

```
| ├── data_preparation
```
- Responsável pela normalização e padronização de datasets da aplicação

### **lib**

```
| ├── lib
```
- Scripts genéricos para utilização em toda aplicação

## ACESSO AO PROJETO

Na raiz do projeto o seguinte comando deve ser executado para a preparação do dataset:

```shell
# Version: 3.8
python3 src/data_preparation_commands.py
```

## TECNOLOGIAS UTILIZADAS

- ``Python``
