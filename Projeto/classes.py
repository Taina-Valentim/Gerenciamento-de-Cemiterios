from datetime import date
from datetime import time
from cores import Cores
import tabelas

def classe(tabela, conn, opc, adm):
  class Jazigo:

    def __init__(self, local, tamanho, quantidadeDeSepulturas, sepulturasOcupadas, nomeDaFamilia, obj):
      self.local = local
      self.tamanho = tamanho
      self.quantidadeDeSepulturas = quantidadeDeSepulturas
      self.sepulturasOcupadas = sepulturasOcupadas
      self.nomeDaFamilia = nomeDaFamilia
      self.obj = obj

    def adicionar_jazigo(self):
      self.local = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nLocal: {Cores.ENDC}")
      self.tamanho = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nTamanho: {Cores.ENDC}")
      self.quantidadeDeSepulturas = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nQuantidade de Sepulturas: {Cores.ENDC}")
      self.sepulturasOcupadas = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nSepulturas Ocupadas: {Cores.ENDC}")
      self.nomeDaFamilia = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nNome da Familia: {Cores.ENDC}")
      self.obj = (self.local.upper(), self.tamanho, self.quantidadeDeSepulturas, self.sepulturasOcupadas, self.nomeDaFamilia.upper())
      tabelas.inserir(tabela, conn, self.obj)

    def atualizar_jazigo(self):
      if adm:
        tabelas.atualizar(tabela, conn, self.obj)
      else:
        print(f"\n{Cores.BOLD}{Cores.LIGHTGRAY}Você não tem permissão para operar neste nível{Cores.ENDC}")

    def excluir_jazigo(self):
      if adm:
        tabelas.excluir(tabela, conn)
      else:
        print(f"\n{Cores.BOLD}{Cores.LIGHTGRAY}Você não tem permissão para operar neste nível{Cores.ENDC}")

  class Obito:

    def __init__(self, nome, dataObito, cpf, cidade, cartorio, livro, folha, termo, medico, crm, obj):
      self.nome = nome
      self.dataObito = dataObito
      self.cpf = cpf
      self.cidade = cidade
      self.cartorio = cartorio
      self.livro = livro
      self.folha = folha
      self.termo = termo
      self.medico = medico
      self.crm = crm
      self.obj = obj
      
    def adicionar_obito(self):
      self.nome = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nNome: {Cores.ENDC}")
      dia = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nDia (DD): {Cores.ENDC}"))
      mes = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nMês (MM): {Cores.ENDC}"))
      ano = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nAno (AAAA): {Cores.ENDC}"))
      self.dataObito = date(ano, mes, dia)
      self.cpf = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nCPF: {Cores.ENDC}")
      self.cidade = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nCidade: {Cores.ENDC}")
      self.cartorio = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nCartório: {Cores.ENDC}")
      self.livro = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nLivro: {Cores.ENDC}")
      self.folha = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nFolha: {Cores.ENDC}")
      self.termo = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nTermo: {Cores.ENDC}")
      self.medico = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nMédico: {Cores.ENDC}")
      self.crm = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nCRM: {Cores.ENDC}")
      self.obj = (
        self.nome.upper(), self.dataObito, self.cpf, self.cidade.upper(), self.cartorio.upper(),
        self.livro, self.folha, self.termo, self.medico.upper(), self.crm
        )
      tabelas.inserir(tabela, conn, self.obj)

    def atualizar_obito(self):
      if adm:
        tabelas.atualizar(tabela, conn, self.obj)
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nVocê não tem permissão para operar neste nível{Cores.ENDC}")

    def excluir_obito(self):
      if adm:
        tabelas.excluir(tabela, conn)
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nVocê não tem permissão para operar neste nível{Cores.ENDC}")

  class Sepultamento:

    def __init__(self, nome, dataSepultamento, horarioEnterro, funeraria, responsavel, localSepultamento, idobito, obj):
      self.nome = nome
      self.dataSepultamento = dataSepultamento
      self.horarioEnterro = horarioEnterro
      self.funeraria = funeraria
      self.responsavel = responsavel
      self.localSepultamento = localSepultamento
      self.idobito = idobito
      self.obj = obj

    def adicionar_sepultamento(self):
      self.idobito = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nID do óbito: {Cores.ENDC}")
      self.nome = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nNome: {Cores.ENDC}")
      dia = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nDia (DD): {Cores.ENDC}"))
      mes = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nMês (MM): {Cores.ENDC}"))
      ano = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nAno (AAAA): {Cores.ENDC}"))
      self.dataSepultamento = date(ano, mes, dia)
      h = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nHorário do enterro (HH): {Cores.ENDC}"))
      m = int(input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nHorário do enterro (MM): {Cores.ENDC}"))
      self.horarioEnterro = time(hour=h, minute=m).isoformat(timespec='minutes')
      self.funeraria = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nFunerária: {Cores.ENDC}")
      self.responsavel = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nResponsável: {Cores.ENDC}")
      self.localSepultamento = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nLocal do sepultamento: {Cores.ENDC}")
      self.obj = (self.nome.upper(), self.dataSepultamento, self.horarioEnterro, self.funeraria.upper(), self.responsavel.upper(), self.localSepultamento.upper(), self.idobito)
      tabelas.inserir(tabela, conn, self.obj)

    def atualizar_sepultamento(self):
      if adm:
        tabelas.atualizar(tabela, conn, self.obj)
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nVocê não tem permissão para operar neste nível{Cores.ENDC}")

    def excluir_sepultamento(self):
      if adm:
        tabelas.excluir(tabela, conn)
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nVocê não tem permissão para operar neste nível{Cores.ENDC}")

  class Usuario:

    def __init__(self, nome, senha, nivel, obj):
      self.nome = nome
      self.senha = senha
      self.nivel = nivel
      self.obj = obj

    def adicionar_usuario(self):
      self.nome = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nNome: {Cores.ENDC}")
      self.senha = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nSenha: {Cores.ENDC}")
      opc = input(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nO usuário será administrador: (S/N){Cores.ENDC}")
      if opc.upper() == 'S': self.nivel = True
      else: self.nivel = False
      self.obj = (self.nome.upper(), self.senha, self.nivel)
      tabelas.inserir(tabela, conn, self.obj)

    def atualizar_usuario(self):
      if adm:
        tabelas.atualizar(tabela, conn, self.obj)
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nVocê não tem permissão para operar neste nível{Cores.ENDC}")

    def excluir_usuario(self):
      if adm:
        tabelas.excluir(tabela, conn)
      else:
        print(f"{Cores.BOLD}{Cores.LIGHTGRAY}\nVocê não tem permissão para operar neste nível{Cores.ENDC}")

  novoJazigo = Jazigo('',0,0,0,'',())
  novoObito = Obito('',0,0,'','',0,0,0,'',0,())
  novoSepultamento = Sepultamento('',0,0,'','','',0,())
  novoUsuario = Usuario('','',0,())

  if tabela == 'JAZIGOS':
    if opc == 1: novoJazigo.adicionar_jazigo()
    elif opc == 2: novoJazigo.atualizar_jazigo()
    elif opc == 3: novoJazigo.excluir_jazigo()
    elif opc == 4: tabelas.pesquisar(tabela, conn)
    elif opc == 5: tabelas.pesquisarUnico(tabela,conn)

  elif tabela == 'OBITOS':
    if opc == 1: novoObito.adicionar_obito()
    elif opc == 2: novoObito.atualizar_obito()
    elif opc == 3: novoObito.excluir_obito()
    elif opc == 4: tabelas.pesquisar(tabela, conn)
    elif opc == 5: tabelas.pesquisarUnico(tabela,conn)
    else: pass

  elif tabela == 'SEPULTAMENTOS':
    if opc == 1: novoSepultamento.adicionar_sepultamento()
    elif opc == 2: novoSepultamento.atualizar_sepultamento()
    elif opc == 3: novoSepultamento.excluir_sepultamento()
    elif opc == 4: tabelas.pesquisar(tabela, conn)
    elif opc == 5: tabelas.pesquisarUnico(tabela,conn)
    else: pass

  elif tabela == 'USUARIOS' and adm:
    if opc == 1: novoUsuario.adicionar_usuario()
    elif opc == 2: novoUsuario.atualizar_usuario()
    elif opc == 3: novoUsuario.excluir_usuario()
    elif opc == 4: tabelas.pesquisar(tabela, conn)
    elif opc == 5: tabelas.pesquisarUnico(tabela,conn)
  