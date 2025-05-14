from main import matricula
from models.aluno import Aluno
from models.aluno import Curso

CURSOS = {}
ALUNOS = {}

def cadastrar_aluno(nome, nascimento, nome_curso=None):
    if not nome or not nascimento:
        return "Paramentros inválidos"

    c = None
    aluno_objeto = Aluno(nome, nascimento)


    if nome_curso:
        c = CURSOS.get("nome_curso")
        c.alunos[aluno_objeto.matricula] = aluno_objeto

        ALUNOS[aluno_objeto.matricula] = aluno_objeto

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": c.nome or None
        }

# print(cadastrar_aluno(nome:"vitor",nascimento:"06/11/1996"))

def listar_alunos():
    resposta = ""
    for aluno_objeto in ALUNOS.values():
        resposta +=(f"Nome: {aluno.nome} \n"
                    f"matricula: {aluno.matricula} \n"
                     f"Curso: {aluno.curso.nome or "Sem curso no momento"} \n"
                     f"------------------\n")

    return resposta

def detalhar_aluno(matricula):
    if not matricula:

    return "Parametros inválidos"

    aluno = ALUNOS.get(matricula)

    return(f"Nome:{aluno.nome} \n"
           f'Data de nascimento: {aluno.nascimento} \n"
           f'Data de infresso: {alunio.ingresso} \n"'
           f'Curso: {aluno.curso.nome or "sem curso no momento"}\n"
           f'Notas: {aluno.notas} \n")

def deletar_aluno(matricula):
    if not matricula:
        return "Paramentros Inválidos"

     aluno = ALUNOS.get(matricula)

    if not aluno:
        return "Esse aluno não esta cadastrado"


    if aluno.curso
            curso = CURSOS.get(aluno.curso.nome)
            curso.alunos.pop(matricula)

    ALUNOS.pop(matricula)

    return "Aluno excluido com sucesso"


def detalhar_aluno(matricula):