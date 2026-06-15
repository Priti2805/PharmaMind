import pandas as pd


def export_to_excel(data, filename):

    df = pd.DataFrame(data)

    df.to_excel(
        filename,
        index=False
    )

    print(
        f"\nExcel file saved: {filename}"
    )