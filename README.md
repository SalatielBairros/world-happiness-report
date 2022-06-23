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

[Estrutura de pastas](https://github.com/SalatielBairros/world-happiness-report/docs/Architecture.md)

## ACESSO AO PROJETO

>Nota: O container da API deve estar parado.

Na raiz do projeto o seguinte comando deve ser executado para a preparação do dataset:

```shell
# Version: 3.8
python3 src/data_preparation_commands.py
```

Para iniciar a API

```shell
sudo docker-compose up
```

## TECNOLOGIAS UTILIZADAS

* ``Python``
