import os
restaurants = [{'Nome':'Bobs', 'Categoria':'Fastfood', 'Ativo':False},
               {'Nome':'GordoLanches', 'Categoria':'Lanche', 'Ativo':True},
               {'Nome':'GilmarDasMarmitex', 'Categoria':'PratoFeito', 'Ativo':True},

               ]
             
def exibir_nome_programa():
      '''
      Esta função é usada para a exibição do titulo do aplicativo na tela principal
      juntamente com o menu de opções.
      '''
      print("""
      s
      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
            """)

def back_to_menu():
      '''
      Esta função é utilizada para sempre retornar à tela inicial sempre que 
      uma tecla for digitada. Neste caso, sempre que é finalizada uma ação.
      
      Exemplo: Restaurante registrado - back_to_menu.
      
      '''
      input('\n Digite uma tecla para voltar ao menu ')
      main()
      

def opcao_invalida():
      '''
      Esta função é utilizada quando qualquer opção fora das estabelecidas pelo
      app são usadas.
      Exemplo: Escolha uma opção:
      Resposta: 9
      opcao_invalida
      '''
      print('Opção invalida!\n')
      back_to_menu()

def show_subtitle(texto):
      '''
      Usada para se adaptar aos subtitulos das opções, alterações tambem são aplicadas em todos os subtitulos.
      
      Texto: Se adapta ao texto escrito em cada pagina.
      '''
      os.system('cls')
      line = '*' * (len(texto))
      print(line)
      print(texto)
      print(line)

def register_new_restaurant():
      
      '''
      Função utilizada para registro de novos restaurantes.
      Dados de entrada: Nome, Categoria, Ativo.
      Processo: Registrar o restaurante baseado nos dados fornecidos na lista de restaurantes.
      Dados de saida: informações do novo restaurante exibidas na lista de restaurantes.
      '''
      show_subtitle('Cadastro de novos restaurantes')
      print()
      name_of_restaurant = input('Digite o nome do restaurante que deseja cadastrar: ')
      category = input(f'Digite a categoria do restaurante {name_of_restaurant}: ')
      data_of_restaurant = {'Nome':name_of_restaurant, 'Categoria':category, 'Ativo':False}
      restaurants.append(data_of_restaurant)
      print(f'O restaurante {name_of_restaurant} foi cadastrado com sucesso')
      back_to_menu()

def show_list_of_restaurant():
      '''
      Utilizada para a exibição de todos os restaurantes registrados no sistema, com seus respectivos dados.
      '''
      show_subtitle('Restaurantes registrados: ')
      
      print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
      print('______________________|||____________________|||___________')
      for restaurant in restaurants:
            name_restaurant = restaurant['Nome']
            category = restaurant['Categoria']
            status ='Ativo'if restaurant['Ativo'] else 'Desativado'
            print(f'- {name_restaurant.ljust(20)} | {category.ljust(20)} | {status} ')
                                    
      back_to_menu()
            
def change_state():
      '''
      Usado para a alteração de estado ativo ou desativado.
      Dados de entrada: Nome do restaurante
      Processo: Identificar se o restaurante existe e caso exista, alterar seu estado atual para o oposto.
      Dados de saida: Alteração do estado do restaurante.
      '''
      show_subtitle('Alternando estado do restaurante')        
      name_restaurant = input('Digite o nome do restaurante que deseja alterar o estado: ')
      finded_restaurant = False
      
      for restaurant in restaurants:
            if name_restaurant == restaurant['Nome']:
                  finded_restaurant = True
                  restaurant['Ativo'] = not restaurant['Ativo']      
                  mensagem = f'O restaurante{name_restaurant} foi ativado com sucesso' if restaurant['Ativo'] else f'O restaurante {name_restaurant} foi desativado com sucesso'
                  print(mensagem)
                  if not finded_restaurant:
                        print('O restaurante não foi encontrado.')  
                        
      back_to_menu()
            
def exibir_opcoes():
      '''
      Exibição das opções na tela principal para a navegação dentro do aplicativo.
      '''
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair \n')

def finalizar_app():
      '''
      Usado para finalizar o aplicativo, selecionando a opção quatro no menu de opções.
      '''
      show_subtitle('Finalizando app.')
      
def escolher_opcoes():
      '''
      Registro de resposta do usuario e o que fazer com o dado entregue.
      Dados de entrada: Opção 1
      Processo: Usar dado fornecido e checar qual função executar.
      Dado de saida: Função register_new_restaurant executada.
      '''
      try:
            opcao_escolhida = int(input('Escolha uma opção: ')) 
            print(f'Voce escolheu a opção {opcao_escolhida}')
            match opcao_escolhida:
                  case 1:
                        register_new_restaurant()
                  case 2:
                        show_list_of_restaurant()
                  case 3:
                        change_state()
                  case 4:
                        finalizar_app()
                  case _:
                        opcao_invalida()

      except:
            opcao_invalida()
      

def main():
      '''
      Tela principal, onde todas as funções que compoem a mesma ficam armazenadas,
      como se fosse uma função para definir a tela principal e seus elementos.
      '''
      os.system('cls')
      exibir_nome_programa()
      exibir_opcoes()
      escolher_opcoes()

if __name__ == "__main__":
   main()
