# Dicionário de dados

A base utilizada é a planilha municipal mensal do Instituto de Segurança Pública do Rio de Janeiro (ISP-RJ).

## Campos de identificação e localização
- `fmun_cod`: código identificador do município.
- `fmun`: nome do município.
- `ano`: ano de referência.
- `mes`: mês de referência.
- `mes_ano`: referência mensal, quando fornecida.
- `regiao`: região de agrupamento utilizada na base.

## Indicadores
A planilha contém indicadores de diferentes naturezas, como homicídio doloso (`hom_doloso`), latrocínio (`latrocinio`), mortes por intervenção de agente do Estado (`hom_por_interv_policial`), roubo de rua (`roubo_rua`), roubo de veículo (`roubo_veiculo`), roubo de carga (`roubo_carga`), estupro (`estupro`), furto (`outros_furtos`) e totais agregados como `total_roubos`, `total_furtos` e `registro_ocorrencias`.

## Observações
- Os nomes das colunas são padronizados para letras minúsculas pelo ETL.
- A unidade de observação é o registro municipal mensal.
- Valores ausentes não são automaticamente substituídos por zero, pois ausência pode ter significado distinto de inexistência de ocorrências.
- `registro_ocorrencias` representa registros contabilizados pela fonte, não necessariamente vítimas únicas.
- A interpretação de cada indicador deve respeitar as definições e notas metodológicas do ISP-RJ.

## Fonte
https://www.ispdados.rj.gov.br/SN/SN2026--ano-base-2025-.html
