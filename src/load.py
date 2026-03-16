import sqlite3

class Load:
    """
    Classe responsável por carregar os dados das universidades
    em um banco de dados SQLite.
    """

    def __init__(self):
        pass

    def create_sqlite_table(self, universities_list, db_name, table_name):
        """
        Cria uma tabela no banco de dados SQLite (se não existir) e
        insere os dados das universidades.

        Args:
            universities_list (list): Lista de dicionários com dados das universidades.
            db_name (str): Nome do arquivo do banco de dados (sem extensão).
            table_name (str): Nome da tabela onde os dados serão inseridos.
        """

        # Cria o banco de dados (ou conecta se já existir) e abre a conexão
        con = sqlite3.connect(f"{db_name}.db")
        c = con.cursor()

        # Cria a tabela caso ela ainda não exista no banco de dados
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name}
                (
                id       INTEGER PRIMARY KEY,
                name     TEXT,
                country  TEXT,
                state_province TEXT,
                web_pages      TEXT,
                domains        TEXT
                );
        """)

        # Itera sobre a lista de universidades e insere cada registro na tabela
        for university in universities_list:
            c.execute(
                f"""INSERT INTO {table_name} (name, country, state_province, web_pages, domains)
                VALUES (?,?,?,?,?);""",
                (
                    university.get("name"),
                    university.get("country"),
                    university.get("state-province"),
                    # Converte a lista de web_pages em uma string separada por vírgula
                    ", ".join(university.get("web_pages", [])),
                    # Converte a lista de domains em uma string separada por vírgula
                    ", ".join(university.get("domains", [])),
                ),
            )

        # Confirma (commit) todas as inserções no banco de dados
        con.commit()

        # Encerra a conexão com o banco de dados
        con.close()
