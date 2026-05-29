import sys
import subprocess

def read_excel():
    try:
        import pandas as pd
        sheets = pd.read_excel("materials/Überblick web-site.xlsx", sheet_name=None)
        for name, sheet in sheets.items():
            print(f"--- Sheet: {name} ---")
            print(sheet.to_csv(index=False))
    except ImportError:
        print("Pandas not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "openpyxl", "--quiet"])
        import pandas as pd
        sheets = pd.read_excel("materials/Überblick web-site.xlsx", sheet_name=None)
        for name, sheet in sheets.items():
            print(f"--- Sheet: {name} ---")
            print(sheet.to_csv(index=False))

read_excel()
