#crie um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 
#- quantidade de notas - a maior nota - a menor nota - a média da turma - a situação(opcional) - docstrigs

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    dicio = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n)/len(n)}

    if sit == True:
        if dicio['media'] >= 7:
            dicio['situacao'] = 'Boa'
        elif dicio['media'] >= 5:
            dicio['situacao'] = 'Razoável'
        else:
            dicio['situacao'] = 'Ruim'
    return dicio


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
#resp = notas(5, 5, 5, 5, sit=True)
#resp = notas(5, 7, sit=False)
print(resp)
#help(notas)
