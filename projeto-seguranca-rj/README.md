# Análise Temporal e Espacial da Criminalidade no Estado do Rio de Janeiro (2014–2026)

Projeto acadêmico da disciplina Linguagem de Programação — Sistemas de Informação, UniLaSalle.

## Objetivo
Explorar a evolução temporal e a distribuição municipal/regional dos registros de ocorrências disponibilizados pelo Instituto de Segurança Pública do Estado do Rio de Janeiro (ISP-RJ).

## Perguntas de pesquisa
- **RQ1:** Como evoluíram os registros de ocorrências entre 2014 e 2025?
- **RQ2:** Quais municípios concentram os maiores totais de registros no período analisado?
- **RQ3:** Como os registros se distribuem entre as regiões do estado?

## Fonte dos dados
Instituto de Segurança Pública do Rio de Janeiro (ISP-RJ):  
https://www.ispdados.rj.gov.br/SN/SN2026--ano-base-2025-.html

Coloque a planilha oficial `BaseMunicipioMensal.xlsx` em `data/raw/`.

## Como reproduzir
```bash
pip install -r requirements.txt
python src/etl.py
```

O ETL gera `data/processed/isp_rj_processed.csv`.

## Cuidados de interpretação
- 2026 contém somente janeiro a setembro na base utilizada; por isso, não deve ser comparado diretamente com anos completos.
- Os números são contagens absolutas de registros/ocorrências, não taxas por população.
- Registros de ocorrência não equivalem necessariamente a vítimas únicas.
- Valores ausentes devem ser interpretados conforme o indicador e a documentação oficial.

## Estrutura
```text
data/
  raw/
  processed/
  data_dictionary.md
notebooks/
  analise_exploratoria.ipynb
src/
  __init__.py
  etl.py
docs/
  index.html
requirements.txt
README.md
LICENSE
.gitignore
```

## Princípios FAIR
Os dados têm sua fonte identificada, os arquivos e variáveis são documentados, e o processamento é realizado por script reproduzível. Consulte as condições de uso e atribuição da fonte oficial antes de redistribuir a planilha original.
