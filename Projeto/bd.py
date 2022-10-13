import sqlite3
from sqlite3 import Error
from cores import Cores

def criar_tabelas(banco):
  conn = sqlite3.connect(banco)
  c = conn.cursor()

  try:
    c.execute("""
      CREATE TABLE IF NOT EXISTS JAZIGOS (
        idjazigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                local TEXT NOT NULL,
                tamanho INTEGER NOT NULL,
                qtdSepulturas INTEGER NOT NULL,
                sepOcupadas INTEGER NOT NULL,
                nomeFamilia TEXT NOT NULL
        );
        """)

    c.execute("""
      CREATE TABLE IF NOT EXISTS OBITOS (
          idobito INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                dataObito DATE NOT NULL,
                cpf VARCHAR(11) NOT NULL UNIQUE,
                cidade TEXT NOT NULL,
                cartorio TEXT NOT NULL,
                livro INTEGER NOT NULL,
                folha INTEGER NOT NULL,
                termo INTEGER NOT NULL,
                medico TEXT NOT NULL,
                crm INTEGER NOT NULL
        );
        """)

    c.execute("""
      CREATE TABLE IF NOT EXISTS SEPULTAMENTOS (
          idsepultamento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                dataSepultamento DATE NOT NULL,
                horarioEnterro TIME NOT NULL,
                funeraria TEXT NOT NULL,
                responsavel TEXT NOT NULL,
                local TEXT NOT NULL,
                idobito INT NOT NULL,
                CONSTRAINT fk_OBITOS FOREIGN KEY (idobito) REFERENCES OBITOS (idobito)
        );
        """)

    c.execute("""
      CREATE TABLE IF NOT EXISTS USUARIOS (
          idusuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                senha TEXT NOT NULL,
                nivel TINYINT(1) NOT NULL
        );
        """)

    return print(f"{Cores.BOLD}{Cores.LIGHTGREEN}Tabelas criadas com sucesso!{Cores.ENDC}")
  
  except Error as e:
      print(e)

