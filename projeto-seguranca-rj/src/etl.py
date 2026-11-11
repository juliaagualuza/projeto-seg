"""ETL da base municipal mensal do ISP-RJ.

Uso:
    python src/etl.py

Entrada:
    data/raw/BaseMunicipioMensal.xlsx

Saída:
    data/processed/isp_rj_processed.csv
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "BaseMunicipioMensal.xlsx"
OUTPUT_DIR = ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "isp_rj_processed.csv"


def run_pipeline() -> pd.DataFrame:
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Planilha não encontrada: {RAW_FILE}\n"
            "Baixe a base oficial do ISP-RJ e salve com esse nome em data/raw/."
        )

    df = pd.read_excel(RAW_FILE)
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    rows_before = len(df)
    df = df.drop_duplicates().copy()
    duplicates_removed = rows_before - len(df)

    # Padroniza campos textuais, quando existentes.
    for column in ("fmun", "regiao", "fase"):
        if column in df.columns:
            df[column] = df[column].astype("string").str.strip()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print("ETL concluído.")
    print(f"Linhas lidas: {rows_before}")
    print(f"Duplicatas removidas: {duplicates_removed}")
    print(f"Linhas finais: {len(df)}")
    print(f"Colunas: {len(df.columns)}")
    print(f"Arquivo gerado: {OUTPUT_FILE}")
    return df


if __name__ == "__main__":
    run_pipeline()
