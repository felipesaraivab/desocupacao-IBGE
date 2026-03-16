from src.extract import Extract
from src.load import Load

# Instancia os objetos de extração e carga
ext = Extract()
ld = Load()

# Extrai a lista de universidades do Brasil e exibe no console
br = ext.extract_country("Brazil")
print(br)

# Extrai a lista de universidades da Itália e exibe no console
it = ext.extract_country("Italy")
print(it)

# Carrega os dados do Brasil na tabela "uni_Brazil" do banco "universidades"
ld.create_sqlite_table(br, "universidades", "uni_Brazil")

# Carrega os dados da Itália na tabela "uni_italy" do banco "universidades"
ld.create_sqlite_table(it, "universidades", "uni_italy")