from src.extract import Extract
from src.load import Load

ext = Extract()
ld = Load()

# br = ext.extract_country("Brazil")
# print(br)

it = ext.extract_country("Italy")
print(it)

# ld.create_sqlite_table(it, "universidades", "uni_Brazil")
ld.create_sqlite_table(it, "universidades", "uni_italy")
