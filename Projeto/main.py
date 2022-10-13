import classes
import sqlite3
from sqlite3 import Error
from time import sleep
import bd
import tabelas
from cores import Cores

def menu():
  print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.BLACK}╔════════════••••••════════════╗{Cores.ENDC}")
  print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.RED}   GERENCIAMENTO DE CEMITÉRIO   {Cores.ENDC}")
  print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.BLACK}╚════════════••••••════════════╝{Cores.ENDC}")
  print("\n\n\n")
  print(f"\t\t\t\t\t{Cores.BOLD}{Cores.BLUE}1 - Jazigos")
  print("\n\t\t\t\t\t2 - Óbitos")
  print("\n\t\t\t\t\t3 - Sepultamentos")
  print(f"\n\t\t\t\t\t4 - Segurança{Cores.ENDC}")
  print(f"\n\t\t\t\t\t{Cores.BOLD}{Cores.LIGHTRED}0 - Logoff{Cores.ENDC}")
  opcao = input("\n\t\t\t\tEscolha uma opção do menu: ")
  valido = valida_entrada(4,opcao)
  if valido: return int(opcao)
  else: return 10

def submenu(tabela):
  print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.BLACK}╔════════════••••••════════════╗{Cores.ENDC}")
  if tabela == 'JAZIGOS': print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.RED}            {tabela}             {Cores.ENDC}")
  if tabela == 'OBITOS': print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.RED}             {tabela}             {Cores.ENDC}")
  if tabela == 'SEPULTAMENTOS': print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.RED}          {tabela}         {Cores.ENDC}")
  if tabela == 'USUARIOS': print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.RED}            {tabela}            {Cores.ENDC}")
  print(f"\t\t\t{Cores.BACKGROUNDWHITE}{Cores.BOLD}{Cores.BLACK}╚════════════••••••════════════╝{Cores.ENDC}")
  print("\n\n\n")
  print(f"\t\t\t{Cores.BOLD}{Cores.CYAN}1 - Registrar {tabela}")
  print(f"\n\t\t\t2 - Atualizar {tabela}")
  print(f"\n\t\t\t3 - Excluir {tabela}")
  print(f"\n\t\t\t4 - Mostrar todos os {tabela}")
  print(f"\n\t\t\t5 - Buscar um único {tabela}{Cores.BOLD}")
  print(f"\n\t\t\t{Cores.LIGHTRED}0 - Voltar{Cores.ENDC}")
  opcaoSub = input("\n\t\t\tEscolha uma opção do menu: ")
  valido = valida_entrada(5,opcaoSub)
  if valido: return int(opcaoSub)
  else: return 10

def criar_conexao(banco):
	conn = None
	try:
		conn = sqlite3.connect(banco)
		print(f'{Cores.DIM}{Cores.LIGHTYELLOW}Versão: {sqlite3.sqlite_version}{Cores.ENDC}')
		return conn
	except Error as e:
		print(e)

def limpar():
    import os
    from time import sleep
    def screen_clear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')
    sleep(1)
    screen_clear()

def valida_entrada(max, opc):
  for i in range(max+1):
    if opc == str(i): return True
  return False

if __name__ == '__main__':
  limpar()
  banco = input(f"{Cores.BOLD}Informe o nome do banco: {Cores.ENDC}")
  conn = criar_conexao(banco)

  bd.criar_tabelas(banco)
  sleep(2)
  input(f"{Cores.BOLD}{Cores.LIGHTBLUE}... Pressione ENTER para continuar ...{Cores.ENDC}")
  limpar()
  c = conn.cursor()
  
  #abaixo eu adiciono o primeiro usuario para o primeiro login (se este usuario ainda nao exitir, para evitar repetiçao de registro)
  #então, na primeira execução do programa, o login deve ser TAINA e a senha deve ser 1980
  #no login não há diferença entre maiúsculas e minúsculas, mas na senha sim
  usuario_existe = tabelas.pesquisa_login('TAINA', '1980', conn)
  if not usuario_existe: c.execute("INSERT INTO USUARIOS (nome, senha, nivel) VALUES ('TAINA','1980',1);")
  conn.commit()

  while True:
    limpar()
    op = input(f"\n{Cores.BOLD}{Cores.LIGHTGREEN}1 - Login\n\n{Cores.LIGHTRED}\n0 - Sair{Cores.ENDC}\n\n")
    valido = valida_entrada(1,op)
    if valido: op = int(op)
    limpar()
    if op == 0:
      conn.close() 
      break
    if op != 1:
      print(f"{Cores.DIM}{Cores.BOLD}{Cores.LIGHTRED}Opção Inválida!{Cores.ENDC}\n\n")
      continue
    while True:
      limpar()
      nome = input(f"\n\n\t{Cores.BOLD}Login: {Cores.ENDC}")
      senha = input(f"\n\t{Cores.BOLD}Senha: {Cores.ENDC}")
      usuario_existe = tabelas.pesquisa_login(nome, senha, conn)
      adm = tabelas.adm_valido(nome, senha, conn)
      limpar()
      
      if usuario_existe: break
      print(f'{Cores.BOLD}{Cores.BACKGROUNDLIGHTRED}{Cores.BLACK}  Problema ao logar, verifique seus dados e tente novamente!  {Cores.ENDC}')
      sleep(2)

    opcao = menu()
    while opcao != 0 and usuario_existe:
      limpar()
      if opcao == 1:
        tabela = 'JAZIGOS'
      elif opcao == 2:
        tabela = 'OBITOS'
      elif opcao == 3:
        tabela = 'SEPULTAMENTOS'
      elif opcao == 4:
        tabela = 'USUARIOS'
      else:
        print(f'{Cores.BOLD}{Cores.LIGHTRED}Opção inválida!{Cores.ENDC}')
        limpar()
        opcao = menu()
        continue

      opcaosub = submenu(tabela)
      limpar()
      while opcaosub != 0:
        if opcaosub >= 1 and opcaosub <= 5: classes.classe(tabela,conn,opcaosub, adm)
        else: print(f'{Cores.BOLD}{Cores.LIGHTRED}Opção inválida!{Cores.ENDC}')
        limpar()
        opcaosub = submenu(tabela)
        limpar()
      opcao = menu()
      limpar()
