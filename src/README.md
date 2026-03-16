# ETL_UNI

## Descrição

ETL_UNI é um projeto de pipeline ETL (Extract, Transform, Load) que coleta dados de universidades de diferentes países a partir da API pública [Hipolabs](http://universities.hipolabs.com) e os armazena em um banco de dados SQLite local.

## Como funciona

O pipeline é dividido em três etapas:

- **Extract** — consulta a API e retorna uma lista de universidades filtradas por país
- **Load** — recebe os dados extraídos e os insere em uma tabela no banco de dados SQLite
- **Main** — orquestra as etapas, chamando a extração e a carga para cada país desejado