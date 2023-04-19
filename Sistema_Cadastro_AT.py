
# ---- Mini projeto feito na disciplina de linguagem PYTHON no curso de Analise e Desenvolvimento de Sistemas no INFNET ---- #
# ---- Usando apenas métodos que foram ensinados em aula ---- #


# --------- Sistema de cadastro --------- # 
# Lista com informações adicionadas previamente
nomes = ['Gabriela Silva', 'Ana Souza', 'João Antunes']
cpfs = [24434377523, 33292296161, 22755218100]
nascimentos = ["23/09/1994", "01/12/1995", "18/12/1989"]

#estrutura de repetição para acessar menu
while True:

  # menu para acessar sistema
  print("-- Sistema de cadastro --")
  print("Como podemos te ajudar?")
  print("-="*15)
  print("1.Inserir novo cadastro")
  print("2.Alterar CPF")
  print("3.Trocar sobrenomes")
  print("4.Remover cadastro")
  print("5.Listar todos os cadastros")
  print("6.Encerrar")
  print("-="*15)

  option = input("Escolha uma das opções: ")
  
  
  if option == '1':
    
      ID = input("Informe o ID do cadastro: ")
      # condicional para validar ID
      if ID != "" and (ID not in "0123456789" or  int(ID) > (len(nomes)+1) or int(ID) <=0 ) : 
        print("ID invalido.")
        continue
    
      nome = input("Informe o seu primeiro nome: ").capitalize()
      # condicional para validar o nome
      if not nome.isalpha():
        print("Nome inválido.")
        continue
           
      sobrenome = input("Informe o seu sobrenome: ").capitalize()
      # condicional para validar o sobrenome
      if not sobrenome.isalpha():
        print("Sobrenome inválido.")
        continue
      
      cpf = input("Informe o CPF: ")
      # condicional para validar o cpf
      if len(str(cpf)) !=11: #possui 11 numeros?
        print("CPF inválido")
        continue
                
      else:
        #codicional para validar se é composto por inteiros 
        for n in range(len(cpf)):
          if cpf[n] not in "0123456789":
            print("CPF inválido1")
            continue
        # condicional para avaliar se é cpf da região sudeste
        if cpf[8] in "6,7,8":
          print("Não aceitamos CPF da regiao sudeste")
          continue
          
        somaDig1 = int(cpf[0]) *10 + int(cpf[1]) *9 + int(cpf[2]) *8 + int(cpf[3]) *7 + int(cpf[4]) *6 + int(cpf[5]) *5 + int(cpf[6]) *4 + int(cpf[7]) *3 + int(cpf[8]) *2 # soma de codigo verificador 1
        digVerif1 = somaDig1 %11
        if digVerif1 == 0 or digVerif1 ==1:
          digVerif1 =0
        else:
          digVerif1 =  11- digVerif1
        somaDig2 = int(cpf[1]) *10 + int(cpf[2]) *9 + int(cpf[3]) *8 + int(cpf[4]) *7 + int(cpf[5]) *6 + int(cpf[6]) *5 + int(cpf[7]) *4 + int(cpf[8]) *3 + int(cpf[9]) *2 # soma de codigo verificador 2
        digVerif2 = somaDig2 % 11
        if  digVerif2 == 0 or digVerif2 ==1:
            digVerif2 =0
        else:
          digVerif2 = 11 - digVerif2
        # conficional para validar codigos verificadores de cpf
        if int(cpf[9]) != digVerif1 or int(cpf[10]) != digVerif2:
          print("CPF inválido")
          continue
                  
                
      nasc = input("Informe a data de nascimento: ") 
      # validação da data
      if len(nasc) != 10 or not nasc[:2].isdecimal or not nasc[3:5].isdecimal or not nasc[6:].isdecimal or nasc[2] != '/' and nasc[5] != '/' :
        print("Data inválida")
        continue
      # condicional que ira determinar local para adição de novo cadastro
      if ID == "": # sem id, adiciona no final da lista
        nomes.append(nome + " " + sobrenome)
        cpfs.append(cpf)
        nascimentos.append(nasc)
  
      else: #com id, adiciona na posição indicada
        id1 = int(ID) -1
        nomes.insert(id1, nome + " " + sobrenome)
        cpfs.insert(id1, cpf)
        nascimentos.insert(id1, nasc)
      print("-="*15)
      

  elif option =='2':
  
    ID = input("Informe o id do cadastro que quer alterar: ")
    # condicional para validar id
    if ID not in "0123456789" or ID == "" : 
      print("ID invalido")
      continue
    
    # condicional indicando qual posição do cadastro que sera alterado
    if int(ID) < (len(nomes)+1) and int(ID)>0: #caso ID exista na lista
      novoCpf = input("novo cpf: ")

      # condicional para validar o cpf
      if len(novoCpf) !=11: #possui 11 numeros?
        print("CPF inválido")
        continue
        
      
      #codicional para validar se é composto por inteiros 
      for n in range(len(novoCpf)):
        if novoCpf[n] not in "0123456789":
          print("CPF inválido1")
          continue
      # condicional para avaliar se é cpf da região sudeste
      if novoCpf[8] in "6,7,8":
        print("Não aceitamos CPF da regiao sudeste")
        continue
        
      somaDig1 = int(novoCpf[0]) *10 + int(novoCpf[1]) *9 + int(novoCpf[2]) *8 + int(novoCpf[3]) *7 + int(novoCpf[4]) *6 + int(novoCpf[5]) *5 + int(novoCpf[6]) *4 + int(novoCpf[7]) *3 + int(novoCpf[8]) *2 # soma de codigo verificador 1
      digVerif1 = somaDig1 %11
      if digVerif1 == 0 or digVerif1 ==1:
        digVerif1 =0
      else:
        digVerif1 =  11- digVerif1
      somaDig2 = int(novoCpf[1]) *10 + int(novoCpf[2]) *9 + int(novoCpf[3]) *8 + int(novoCpf[4]) *7 + int(novoCpf[5]) *6 + int(novoCpf[6]) *5 + int(novoCpf[7]) *4 + int(novoCpf[8]) *3 + int(novoCpf[9]) *2 # soma de codigo verificador 2
      digVerif2 = somaDig2 % 11
      if  digVerif2 == 0 or digVerif2 ==1:
          digVerif2 =0
      else:
        digVerif2 = 11 - digVerif2
      # conficional para validar codigos verificadores de novoCpf
      if int(novoCpf[9]) != digVerif1 or int(novoCpf[10]) != digVerif2:
        print("CPF inválido")
        continue
      
      cpfs[int(ID)-1] = novoCpf #troca a informação
      print("CPF atualizado com sucesso!")
      print("-="*15)
      
    else:
      print("-="*15)
      print("Não localizei este cadastro")
      print("-="*15)
     
   
  elif option =='3':
  
    ID1 = input("Informe o id do primeiro cadastro: ")
    # condicional para validar id
    if ID1 not in "0123456789" or ID1 == "" : 
      print("ID invalido")
      continue
    
    if int(ID1) < (len(nomes)+1) and int(ID1)>0:
      ID1 = int(ID1)
      ID1 -=1 #localiza a posição
      primeiroSobre = nomes[ID1] #seleciona apenas o item localizado no ID
      espaco1 = primeiroSobre.find(" ") #busca o espaço" "
      pn1 = nomes[ID1][:espaco1] #isola o nome com fatiamento
      sn1 = primeiroSobre[espaco1+1:] #isola o sobrenome com fatiamento
    else:
      print("-="*15)
      print("Não localizei este cadastro")
      print("-="*15)
      continue  
    
    ID2 = input("Informe o id do segundo cadastro: ")
    # condicional para validar id
    if ID2 not in "0123456789" or ID2 == "" : 

      print("ID invalido")
      continue
    
    if int(ID2) < (len(nomes)+1) and int(ID2)>0:
      ID2 = int(ID2)
      ID2 -=1 #localiza a posição
      segundoSobre = nomes[ID2] #seleciona apenas o item localizado no ID
      espaco2 = segundoSobre.find(" ") #busca o espaço" "
      pn2 = nomes[ID2][:espaco2] #isola o nome com fatiamento
      sn2 = segundoSobre[espaco2+1:] #isola o sobrenome com fatiamento

      # Troca de posição do ssobrenomes
      nomes[ID1]=(f'{pn1} {sn2}')
      nomes[ID2]=(f'{pn2} {sn1}')

      print("Troca de sobrenomes realizada com sucesso!")
      print("-="*15)

    else:
      print("-="*15)
      print("Não localizei este cadastro")
      print("-="*15)

  
  elif option =='4':
  
    ID = input("Informe o id do cadastro que quer remover: ")
    if ID not in "0123456789" or ID == "" : 
      print("ID invalido")
      continue
      
    # condicional indicando qual posição do cadastro que sera removido
    if int(ID) < (len(nomes)+1) and int(ID)>0:
      ID = int(ID)
      nomes.pop(ID-1)
      cpfs.pop(ID-1)
      nascimentos.pop(ID-1) 
      print("Cadastro removido com sucesso!")
      print("-="*15)

    else:
      print("-="*15)
      print("Não localizei este cadastro")
      print("-="*15)
      
  elif option =='5':

    print("Listagem de cadastros")
    print("-="*15)
    # Incrementando de acordo com a quantidade de cadastros fornecidos
    # Listando um cadastro por linha
  
    for n in range(len(nomes)):
      print(f"{n+1}", "Nome:", nomes[n], "CPF:", cpfs[n], "Data:", nascimentos[n])
    print("-="*15)
    
  elif option == '6':
      
      print("-="*15)
      print("--- Sistema encerrado! ---")
      print("-="*15)
      
      break
    
  else: # avalia se a opçõa existe no menu 
    print("Opção inválida! Tente novamente!")
    print("-="*15)
