def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, incicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    turma = dict()

    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n)/len(n)
    if sit:
        if turma['média'] >= 7:
           turma['situação'] = 'Boa'
        elif turma['média'] >= 5:
            turma['situação'] = 'Razoável'
        elif turma['média'] < 5:
            turma['situação'] = 'Ruim'
    return turma


# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)

