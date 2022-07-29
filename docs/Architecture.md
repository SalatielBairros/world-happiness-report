# ARQUITETURA DO PROJETO

```markdown
├── = Representa uma pasta no projeto

└── = Representa um arquivo

|├── analisys
|├── app
|├── assets
|├── data_augmentation
|├── data_combination
|├── data_ingestion
|├── data_preparation
|├── docs
|├── enviroment
|├── feature_engineering
|├── lib
|├── models
|├── repository
|├── services
|├── sh
|├── views
```

## **ANALISYS**

```markdown
|├── analisys
```

- Responsável pela parte da pré-analise dos datasets
- A nível de analise é utilizado os Jupyter Notebooks

## **APP**

```markdown
|├── app
```

- Comtém a lógica da REST API

## **ASSETS**

```markdown
|├── assets
```

- Recursos consumidos para analises como imagem, estilos entre outros.

## **DATA AUGMENTATION**

```markdown
|├── data_augmentation
```

- Lógicas utilizadas para artificialmente aumentar o tamanho do dataset de treino a partir de um dataset existente.

## **DATA COMBINATION**

```markdown
|├── data_combination
```

- Higienização do dataset.

## **DATA INGESTION**

```markdown
|├── data_ingestion
```

- Cria um pipeline para criar o dataset

## **DATA PREPARATION**

```markdown
| ├── data_preparation
```

- Responsável pela normalização e padronização de datasets da aplicação

## **DOCS**

```markdown
|├── docs
```

- Documentações gerais do projeto

## **ENVIROMENTS**

```markdown
|├── enviroments
```

- Valores que serão constantes no processo
- Valores variaveis no projeto

## **FEATURE ENGINEERING**

```markdown
|├── feature_engineering
```

- Processo responsável por pegar dados brutos e os transformar em recursos que podem ser usados ​​para criar um modelo preditivo usando aprendizado de máquina ou modelagem estatística, como aprendizado profundo.

## **LIB**

```markdown
| ├── lib
```

- Scripts genéricos para utilização em toda aplicação

## **MODELS**

```markdown
| ├── models
```

- Modelos de Machine Learning

## **REPOSITORY**

```markdown
| ├── repository
```

- Getters e Setters do projeto

## **SERVICES**

```markdown
| ├── services
```

- Funções especificas do projeto

## **SH**

```markdown
| ├── sh
```

- Scripts de automação do projeto

## **VIEWS**

```markdown
| ├── views
```

- Views geradas pelo Pandas Profiling
