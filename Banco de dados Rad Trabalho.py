import sqlite3

def iniciando_o_db():
    conn = sqlite3.connect('pontuacoes_dos_terceira_idade.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            nome TEXT PRIMARY KEY,
            jogo1 INT,
            jogo2 INT,
            jogo3 INT
        )
    ''')
    
    
    dados_dos_jogos = [
        ('Maria', 500, 1000, 700), ('Caio', 800, 1200, 900), ('Margarida', 1500, 2000, 3000), ('Armando', 1200, 900, 1100), ('Clotilde', 0, 0, 0), ('Francisco', 1000, 1000, 1000)
    ]
    cursor.executemany('INSERT OR IGNORE INTO usuarios VALUES (?, ?, ?, ?)', dados_dos_jogos)
    
    conn.commit()
    conn.close()

iniciando_o_db()