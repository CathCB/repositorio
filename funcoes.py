'''
    Funçao: contarStringsMenorCinco
    param: lista de strings
    
'''
def contarStringsMenorCinco(lista):
    """ conta strings na lista com tamanho < 5 """
    cont = 0
    # percorre a lista inteira
    for s in lista:
        tam = len(s) #pega tamaho da string
        if tam < 5:  # se o tamanho for menor que 5
            cont += 1

    return cont

'''
    Funçao: somarInteirosPares
    param: lista de inteiros
    
'''
def somarInteirosPares(lista):
    """ soma todos os pares """
    soma = 0
    # percorre a lista inteira
    for i in lista:
        if i%2 == 0:  # se for par
            soma += i

    return soma

'''
    Funçao: contarStringsAtePalavra
    param: lista de strings
    param: palavra a ser procurada
    
'''
def contarStringsAtePalavra(lista, palavra):
    """ conta strings na lista ate encontrar palavra """
    cont = 0
    # percorre a lista inteira
    for s in lista:
        cont += 1
        if s == palavra:  # se achar a palavra sai
            break

    return cont

'''
    Funçao: troca
    param: s string de palavras
    param: velho - string anterior
    param: novo - string a ser trocado
    
'''
def troca(s, velho, novo):
    sAnt = s.split()
    sAtual=""
    for palavra in sAnt:
        if palavra == velho:
            sAtual = sAtual + novo + " "
        else:    
            sAtual = sAtual + palavra + " "

    return sAtual
