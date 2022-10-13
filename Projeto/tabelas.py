from datetime import date
from datetime import time
from time import sleep
from cores import Cores
from tabulate import tabulate

def inserir(tabela, conn, obj):
  c = conn.cursor()
  if tabela == 'JAZIGOS':
    c.execute("INSERT INTO JAZIGOS (local, tamanho, qtdSepulturas, sepOcupadas, nomeFamilia) VALUES (?,?,?,?,?);", obj)
    conn.commit()
  elif tabela == 'OBITOS':
    c.execute("INSERT INTO OBITOS (nome, dataObito, cpf, cidade, cartorio, livro, folha, termo, medico, crm) VALUES (?,?,?,?,?,?,?,?,?,?);", obj)
    conn.commit()
  elif tabela == 'SEPULTAMENTOS':
    c.execute("INSERT INTO SEPULTAMENTOS (nome, dataSepultamento, horarioEnterro, funeraria, responsavel, local, idobito) VALUES (?,?,?,?,?,?,?);", obj)
    conn.commit()
  elif tabela == 'USUARIOS':
    c.execute("INSERT INTO USUARIOS (nome, senha, nivel) VALUES (?,?,?);", obj)
    conn.commit()
  print(f"\n{Cores.BOLD}{Cores.GREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}")
  sleep(2)

def atualizar(tabela, conn, obj):
  c = conn.cursor()
  x = 0
  valido = False
  registros = pesquisar(tabela, conn)
  if registros:
    x = int(input(f"{Cores.BOLD}{Cores.LIGHTMAGENTA}\nIndique qual id a atualizar: {Cores.ENDC}"))
    valido = id_valido(tabela, conn, x)

  if tabela == 'JAZIGOS' and valido:
    nome = input(f"{Cores.YELLOW}Nome da Família: {Cores.ENDC}")
    local = input(f"{Cores.YELLOW}Local: {Cores.ENDC}")
    tamanho = int(input(f"{Cores.YELLOW}Tamanho: {Cores.ENDC}"))
    qtdSepulturas = int(input(f"{Cores.YELLOW}Quantidade de sepulturas: {Cores.ENDC}"))
    sepultOcupadas = int(input(f"{Cores.YELLOW}Sepulturas Ocupadas: {Cores.ENDC}"))
    values = (local.upper(), tamanho, qtdSepulturas, sepultOcupadas, nome.upper(), x)
    c.execute("UPDATE JAZIGOS SET local=?, tamanho=?, qtdSepulturas=?, sepOcupadas=?, nomeFamilia=? WHERE idjazigo=?;", values)
    conn.commit()

  elif tabela == 'OBITOS' and valido:
    nome = input(f"{Cores.YELLOW}Nome: {Cores.ENDC}")
    dia = int(input(f"{Cores.YELLOW}Dia (DD): {Cores.ENDC}"))
    mes = int(input(f"{Cores.YELLOW}Mês (MM): {Cores.ENDC}"))
    ano = int(input(f"{Cores.YELLOW}Ano (AAAA): {Cores.ENDC}"))
    data = date(ano, mes, dia)
    cpf = input(f"{Cores.YELLOW}CPF: {Cores.ENDC}")
    cidade = input(f"{Cores.YELLOW}Cidade: {Cores.ENDC}")
    cartorio = input(f"{Cores.YELLOW}Cartório: {Cores.ENDC}")
    livro = int(input(f"{Cores.YELLOW}Livro: {Cores.ENDC}"))
    folha = int(input(f"{Cores.YELLOW}Folha: {Cores.ENDC}"))
    termo = int(input(f"{Cores.YELLOW}Termo: {Cores.ENDC}"))
    medico = input(f"{Cores.YELLOW}Médico: {Cores.ENDC}")
    crm = int(input(f"{Cores.YELLOW}CRM: {Cores.ENDC}"))
    values = (nome.upper(), data, cpf, cidade.upper(), cartorio.upper(), livro, folha, termo, medico.upper(), crm, x)
    c.execute("UPDATE OBITOS SET nome=?, dataObito=?, cpf=?, cidade=?, cartorio=?, livro=?, folha=?, termo=?, medico=?, crm=? WHERE idobito=?;", values)
    conn.commit()

  elif tabela == 'SEPULTAMENTOS' and valido:
    nome = input(f"{Cores.YELLOW}Nome: {Cores.ENDC}")
    dia = int(input(f"{Cores.YELLOW}Dia (DD): {Cores.ENDC}"))
    mes = int(input(f"{Cores.YELLOW}Mês (MM): {Cores.ENDC}"))
    ano = int(input(f"{Cores.YELLOW}Ano (AAAA): {Cores.ENDC}"))
    data = date(ano, mes, dia)
    h = int(input(f"{Cores.YELLOW}Horário do enterro (HH): {Cores.ENDC}"))
    m = int(input(f"{Cores.YELLOW}Horário do enterro (MM): {Cores.ENDC}"))
    hora = time(hour=h, minute=m).isoformat(timespec='minutes')
    funeraria = input(f"{Cores.YELLOW}Funerária: {Cores.ENDC}")
    responsavel = input(f"{Cores.YELLOW}Responsável: {Cores.ENDC}")
    local = input(f"{Cores.YELLOW}Local: {Cores.ENDC}")
    values = (nome.upper(), data, hora, funeraria.upper(), responsavel.upper(), local.upper(), x)
    c.execute("UPDATE SEPULTAMENTOS SET nome=?, dataSepultamento=?, horarioEnterro=?, funeraria=?, responsavel=?, local=? WHERE idsepultamento=?;", values)
    conn.commit()

  elif tabela == 'USUARIOS' and valido:
    nome = input(f"{Cores.YELLOW}Nome: {Cores.ENDC}")
    senha = input(f"{Cores.YELLOW}Senha: {Cores.ENDC}")
    nivel = int(input(f"{Cores.YELLOW}Adm?\n\n0 - Não\n1 - Sim: {Cores.ENDC}"))
    values = (nome.upper(), senha, nivel, x)
    c.execute("UPDATE USUARIOS SET nome=?, senha=?, nivel=? WHERE idusuario=?;", values)
    conn.commit()

  if valido: print(f"{Cores.BOLD}{Cores.GREEN}\nAtualização com sucesso em {tabela}.{Cores.ENDC}")

def pesquisar(tabela, conn):
  c = conn.cursor()
  dados = []
  registros = False
  
  if tabela == 'JAZIGOS':
    c.execute("SELECT * FROM JAZIGOS;")
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'LOCAL', 'TAMANHO', 'QUANTIDADE DE SEPULTURAS', 'SEPULTURAS OCUPADAS', f'NOME DA FAMÍLIA{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3]), str(resultado[item][4]), str(resultado[item][5])]
        dados.append(dados_item)
      print(tabulate(dados, headers))
      registros = True
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'OBITOS':
    c.execute("SELECT * FROM OBITOS;")
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'NOME', 'DATA DO ÓBITO', 'CPF', 'CIDADE', 'CARTÓRIO', 'LIVRO', 'FOLHA', 'TERMO', 'MÉDICO', f'CRM{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3]), str(resultado[item][4]), str(resultado[item][5]), str(resultado[item][6]), str(resultado[item][7]), str(resultado[item][8]), str(resultado[item][9]), str(resultado[item][10])]
        dados.append(dados_item)
      print(tabulate(dados, headers))
      registros = True
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'SEPULTAMENTOS':
    c.execute("SELECT * FROM SEPULTAMENTOS INNER JOIN OBITOS ON OBITOS.idobito == SEPULTAMENTOS.idsepultamento;")
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'NOME', 'DATA DO SEPULTAMENTO', 'HORA DO ENTERRO', 'FUNERÁRIA', 'RESPONSÁVEL', f'LOCAL DO SEPULTAMENTO{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3]), str(resultado[item][4]), str(resultado[item][5]), str(resultado[item][6]),]
        dados.append(dados_item)
      print(tabulate(dados, headers))
      registros = True
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'USUARIOS':
    c.execute("SELECT * FROM USUARIOS;")
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'NOME', 'SENHA', f'NÍVEL DE OPERAÇÃO{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3])]
        dados.append(dados_item)
      print(tabulate(dados, headers))
      registros = True
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  print(f"{Cores.BOLD}{Cores.GREEN}\nPesquisa realizada com sucesso em {tabela}.{Cores.ENDC}")
  input(f"{Cores.BOLD}{Cores.LIGHTBLUE}\nPressione ENTER para continuar ...{Cores.ENDC}")
  return registros

def pesquisarUnico(tabela, conn):
  c = conn.cursor()
  dados = []
  if tabela == 'JAZIGOS':
    nome = input(f"{Cores.BOLD}{Cores.LIGHTMAGENTA}Nome da Família: {Cores.ENDC}").upper()
    c.execute("SELECT * FROM JAZIGOS WHERE nomeFamilia like (?);", ('%'+nome+'%', ))
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'LOCAL', 'TAMANHO', 'QUANTIDADE DE SEPULTURAS', 'SEPULTURAS OCUPADAS', f'NOME DA FAMÍLIA{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3]), str(resultado[item][4]), str(resultado[item][5])]
        dados.append(dados_item)
      print(tabulate(dados, headers))
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\n Não foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'OBITOS':
    nome = input(f"{Cores.BOLD}{Cores.LIGHTMAGENTA}Informe o nome a pesquisar: {Cores.ENDC}").upper()
    c.execute("SELECT * FROM OBITOS WHERE nome like (?);", ('%'+nome+'%', ))
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'NOME', 'DATA DO ÓBITO', 'CPF', 'CIDADE', 'CARTÓRIO', 'LIVRO', 'FOLHA', 'TERMO', 'MÉDICO', f'CRM{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3]), str(resultado[item][4]), str(resultado[item][5]), str(resultado[item][6]), str(resultado[item][7]), str(resultado[item][8]), str(resultado[item][9]), str(resultado[item][10])]
        dados.append(dados_item)
      print(tabulate(dados, headers))
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'SEPULTAMENTOS':
    nome = input(f"{Cores.BOLD}{Cores.LIGHTMAGENTA}Informe o nome a pesquisar: {Cores.ENDC}").upper()
    c.execute("SELECT * FROM SEPULTAMENTOS WHERE nome like (?);", ('%'+nome+'%', ))
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'NOME', 'DATA DO SEPULTAMENTO', 'HORA DO ENTERRO', 'FUNERÁRIA', 'RESPONSÁVEL', f'LOCAL DO SEPULTAMENTO{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3]), str(resultado[item][4]), str(resultado[item][5]), str(resultado[item][6]),]
        dados.append(dados_item)
      print(tabulate(dados, headers))
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'USUARIOS':
    nome = input(f"{Cores.BOLD}{Cores.LIGHTMAGENTA}Informe o nome a pesquisar: {Cores.ENDC}").upper()
    c.execute("SELECT * FROM USUARIOS WHERE nome like (?);", ('%'+nome+'%', ))
    resultado = c.fetchall()
    if resultado:
      headers = [f'{Cores.BOLD}{Cores.LIGHTCYAN}Rowid', 'ID', 'NOME', 'SENHA', f'NÍVEL DE OPERAÇÃO{Cores.ENDC}']
      for item in range(len(resultado)):
        dados_item = [str(item), str(resultado[item][0]), str(resultado[item][1]), str(resultado[item][2]), str(resultado[item][3])]
        dados.append(dados_item)
      print(tabulate(dados, headers))
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}Não foram encontrados registros.{Cores.ENDC}")

  print(f"{Cores.BOLD}{Cores.GREEN}\nPesquisa realizada com sucesso em {tabela}.{Cores.ENDC}")
  input(f"{Cores.BOLD}{Cores.LIGHTBLUE}\nPressione ENTER para continuar ...{Cores.ENDC}")

def excluir(tabela, conn):
  c = conn.cursor()
  valido = False
  x = 0
  registros = pesquisar(tabela, conn)
  if registros:
    x = int(input(f"{Cores.BOLD}{Cores.LIGHTMAGENTA}\nIndique qual id a atualizar: {Cores.ENDC}"))
    valido = id_valido(tabela, conn, x)
  values = (x,)
  if tabela == 'JAZIGOS' and valido: c.execute("DELETE FROM JAZIGOS WHERE idjazigo=?", values)
  elif tabela == 'OBITOS' and valido: c.execute("DELETE FROM OBITOS WHERE idobito=?", values)
  elif tabela == 'SEPULTAMENTOS' and valido: c.execute("DELETE FROM SEPULTAMENTOS WHERE idsepultamento=?", values)
  elif tabela == 'USUARIOS' and valido: c.execute("DELETE FROM USUARIOS WHERE idusuario=?", values)
  if valido: print(f"{Cores.BOLD}{Cores.GREEN}\nExclusão com sucesso em {tabela}.{Cores.ENDC}")

def id_valido(tabela, conn, id):
  c = conn.cursor()

  if tabela == 'JAZIGOS':
    c.execute("SELECT * FROM JAZIGOS;")
    resultado = c.fetchall()
    if resultado:
      for item in range(len(resultado)):
        if resultado[item][0] == id: return True
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTRED}\nID não encontrado.{Cores.ENDC}")
        return False
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'OBITOS':
    c.execute("SELECT * FROM OBITOS;")
    resultado = c.fetchall()
    if resultado:
      for item in range(len(resultado)):
        if resultado[item][0] == id: return True
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTRED}\nID não encontrado.{Cores.ENDC}")
        return False
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'SEPULTAMENTOS':
    c.execute("SELECT * FROM SEPULTAMENTOS;")
    resultado = c.fetchall()
    if resultado:
      for item in range(len(resultado)):
        if resultado[item][0] == id: return True
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTRED}\nID não encontrado.{Cores.ENDC}")
        return False
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

  elif tabela == 'USUARIOS':
    c.execute("SELECT * FROM USUARIOS;")
    resultado = c.fetchall()
    if resultado:
      for item in range(len(resultado)):
        if resultado[item][0] == id: return True
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTRED}\nID não encontrado.{Cores.ENDC}")
        return False
    else:
      print(f"{Cores.BOLD}{Cores.LIGHTRED}\nNão foram encontrados registros.{Cores.ENDC}")

def adm_valido(nom, sen, conn):
  c = conn.cursor()
  c.execute("SELECT * FROM USUARIOS;")
  resultado = c.fetchall()

  for item in range(len(resultado)):
    if resultado[item][1] == nom.upper() and resultado[item][2] == sen and resultado[item][3] == 1: return True
  return False

def pesquisa_login(nom, sen, conn):
  c = conn.cursor()
  c.execute("SELECT * FROM USUARIOS;")
  resultado = c.fetchall()

  for item in range(len(resultado)):
    if resultado[item][1] == nom.upper() and resultado[item][2] == sen: return True
  return False