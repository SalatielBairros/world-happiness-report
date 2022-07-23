# World Happines Report Regression Model

* [Badges](#badges)
* [Descrição do Projeto](#descrição-do-projeto)
* [Arquitetura do projeto](#arquitetura-do-projeto)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)

## BADGES

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## DESCRIÇÃO DO PROJETO

Um modelo de regressão do nível de felicidade no mundo. Utiliza os dados do [WHR 2021 dataset](https://worldhappiness.report/ed/2021/).

> Nota: Os dados utilizados não foram os do Kaggle. O dataset deles não constam os dados originais, apenas dados relativos.

## ARQUITETURA DO PROJETO

[Estrutura de pastas](https://github.com/SalatielBairros/world-happiness-report/blob/main/docs/Architecture.md)

## ACESSO AO PROJETO

>Nota: O container da API deve estar parado.

Na raiz do projeto o seguinte comando deve ser executado para a preparação do dataset:

```shell
# Version: 3.8
python3 src/data_preparation_commands.py
```
Após o dataset se gerado ele pode ser consumido pela API, para iniciar devemos digitar o seguinte comando tambem na raiz do projeto.

Obs: deve-se ter o Docker e Docker compose instalado.

```shell
docker-compose up
```

A documentação da API e gerada de maneira automática com o Swagger em `http://localhost:8002/docs`

```json
{
    "OriginalHistoricDataUrl": "https://github.com/SalatielBairros/world-happiness-report/raw/main/data/original/HistoricData.xls",
    "Data2021Url": "https://github.com/SalatielBairros/world-happiness-report/raw/main/data/original/Data_2021.xls"
}
```

## TECNOLOGIAS UTILIZADAS

* ``Python``
