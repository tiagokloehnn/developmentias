import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurar o escopo e as credenciais
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('caminho/para/seu/arquivo.json', scope)
client = gspread.authorize(creds)

# Abrir a planilha pelo ID ou pelo nome
# Você pode encontrar o ID da planilha na URL, que é a parte após `/d/` e antes de `/edit`
spreadsheet = client.open_by_key('1m-WgJRGVXwKHEY7cCfG1Cp8Xdg2oUIrXE4-Y_OukTS8')
# Ou você pode usar:
# spreadsheet = client.open("Nome da Sua Planilha")

# Selecionar uma aba específica
sheet = spreadsheet.sheet1  # ou use .worksheet('Nome da aba')

# Ler dados
data = sheet.get_all_records()
print(data)

# Adicionar uma nova linha
new_row = ["Valor1", "Valor2", "Valor3"]
sheet.append_row(new_row)

# Atualizar uma célula
sheet.update_cell(1, 1, "Novo Valor")  # Atualiza a célula A1
