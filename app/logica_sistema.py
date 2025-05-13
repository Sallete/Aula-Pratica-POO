from models.aluno import Aluno

CURSOS = {}
ALUNOS = []

def cadastrar_aluno(nome, nascimento, curso):
    if not nome or not nascimento:
        return "Paramentros inválidos"

    c = {}
    aluno_objeto = Aluno(nome, nascimento)


    if curso:
        c = CURSOS.get("curso")
        c["alunos"].append(aluno_objeto)

        ALUNOS.append(aluno_objeto)

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.get("nome_curso")
        }

# print(cadastrar_aluno(nome:"vitor",nascimento:"06/11/1996"))

def listar_alunos():
    resposta = ""
    for aluno_objeto in ALUNOS:
        resposta +=(f"Nome: {aluno_objeto.nome} \n"
                    f"matricula: {aluno_objeto.matricula} \n"
                     f"Curso: {aluno_objeto.curso} \n"
                     f"------------------\n")

    return resposta