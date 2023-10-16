import pandas as pd
df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vR8AS4LnU66VOzeH0nz6Vbfrw2wQ0xAipWOgwjl81fln6ihf-bXdZ-DvGFXg-ufsFyNSy120q2uPaJT/pub?output=xlsx", sheet_name="Resultados_Clase1")
print(df)