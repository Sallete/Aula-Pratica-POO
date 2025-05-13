from app.logica_sistema import cadastrar_aluno, listar_alunos

comando = ""

while comando !="sair":
      comando = input(f"Escolha uma opção: \n"
                      f"1) Cadastrar Aluno \n"
                      f"2) Listar Alunos \n"
                      f"Digite 'sair para sair do sistema \n")

#CADASTRA ALUNOS
      match comando:
          case "1":
              nome = input ("Informe o nome do aluno:")
              nascimento = input("Informe a data de nascimento do aluno:")
              curso = input("Informe o curso do aluno se tiver, se não deixe vazio:")

              print(cadastrar_aluno(nome,nascimento,curso))

# LISTAR ALUNOS
          case "2":
            print(listar_alunos())

          case "3":
              print("Saindo do Sistema.")
