class Database:
    def __init__(self, db_name='hotel.db'):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        import sqlite3
        self.connection = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS hospedes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL UNIQUE,
                    telefone TEXT NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS quartos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero INTEGER NOT NULL UNIQUE,
                    tipo TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'disponível'
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS reservas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    hospede_id INTEGER NOT NULL,
                    quarto_id INTEGER NOT NULL,
                    data_entrada TEXT NOT NULL,
                    data_saida TEXT NOT NULL,
                    FOREIGN KEY (hospede_id) REFERENCES hospedes (id),
                    FOREIGN KEY (quarto_id) REFERENCES quartos (id)
                )
            ''')

    def execute_query(self, query, params=()):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()

    def insert_hospede(self, hospede):
        with self.connection:
            self.connection.execute(
                "INSERT INTO hospedes (nome, cpf, telefone) VALUES (?, ?, ?)",
                (hospede.nome, hospede.cpf, hospede.telefone)
            )
            
    def insert_quarto(self, quarto):
        with self.connection:
            self.connection.execute(
                "INSERT INTO quartos (numero, tipo, status) VALUES (?, ?, ?)",
                (quarto.numero, quarto.tipo, "disponível")
            )

    def insert_reserva(self, reserva):
        with self.connection:
            self.connection.execute(
                "INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida) VALUES (?, ?, ?, ?)",
                (reserva.hospede_id, reserva.quarto_id, str(reserva.data_entrada), str(reserva.data_saida))
            )
            # Atualiza o status do quarto para 'ocupado'
            self.connection.execute(
                "UPDATE quartos SET status = 'ocupado' WHERE id = ?",
                (reserva.quarto_id,)
            )

    def fetch_hospedes(self):
        return self.execute_query("SELECT id, nome, cpf, telefone FROM hospedes")

    def fetch_quartos(self):
        return self.execute_query("SELECT id, numero, tipo, status FROM quartos")

    def fetch_reservas(self):
        return self.execute_query("""
            SELECT r.id, h.nome, q.numero, r.data_entrada, r.data_saida
            FROM reservas r
            JOIN hospedes h ON r.hospede_id = h.id
            JOIN quartos q ON r.quarto_id = q.id
        """)