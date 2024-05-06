def maior_de_50(lista):
    count = 0 
    for l in lista:
        if l['idade'] > 50:
            count += 1

    return count

def mais_2000(lista):
    count = 0 
    total_registros = len(lista)
    
    for l in lista:
        if float(l['salario']) > 2000:
            count += 1

    x = count * 100/total_registros

    return (count, x, total_registros)

def maior_salario(lista, maior=None):
    """
    maior: é o maior salário para fim de comparação
    se usuário quiser saber o 2 maior por exemplo
    precisa passar o salário maior que o segundo
    """
    pessoa = None 
    for l in lista:
        if maior:
            if pessoa == None:
                pessoa = l
            elif float(l['salario']) > float(pessoa['salario']) and float(l['salario']) < maior:
                pessoa = l
        else:
            if pessoa == None:
                pessoa = l 
            elif float(l['salario']) > float(pessoa['salario']): 
                pessoa = l 

    return pessoa

def media_profissoes(lista):
    profissoes = {}
    for l in lista:
        if l['profissao'] not in profissoes:
            soma = float(l['salario'])
            media = float(l['salario'])
            dado = {"qtd":1, "soma": soma, "media": media }
            profissoes[l['profissao']] = dado

        else:
            qtd = profissoes[l['profissao']]['qtd'] + 1
            soma += float(l['salario'])
            media = soma/qtd
            dado = {"qtd": qtd, "soma": soma, "media": media }
            profissoes[l['profissao']] = dado

    return profissoes
    

def formato_moeda(valor):
    valor = "R$ {:.2f}".format(valor)
    valor = valor.replace(".", ",")
    return f"{valor}"

def filtrar(lista, salario_de=None, sexo=None):
    """
    Retorna uma nova lista somente com quem ganha mais de 2000
    sexo: Masculino ou Feminino
    """
    nova_lista = []
    for l in lista:
        if salario_de and float(l["salario"]) > salario_de:
            nova_lista.append(l)
        elif sexo and l["sexo"] == sexo:
            nova_lista.append(l)

    return nova_lista 

def maior_2000_sexo(lista, sexo='Masculino'):
    """
    lista: lista de dados
    sexo: sexo F ou M
    Para não ficar complexo é melhor fazer um filtro
    """
    lista = filtrar(lista, salario_de=2000)
    lista = filtrar(lista, sexo=sexo)
    menor_idade=0
    maior_idade = 0
    for l in lista:
        if menor_idade == 0:
            menor_idade = l["idade"]
        elif l['idade'] < menor_idade:
            menor_idade = l['idade']  
        if maior_idade == 0:
            maior_idade = l["idade"]
        elif l['idade'] > maior_idade:
            maior_idade = l['idade']
    return (menor_idade, maior_idade)