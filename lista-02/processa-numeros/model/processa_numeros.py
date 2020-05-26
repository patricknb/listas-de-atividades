# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Definição de funções que processam listas contendo números inteiros.
# 

def soma(numeros):
    """Calcula a soma dos números.

    Se a lista estiver vazia então retorna None para indicar
    que o problema não tem solução.
    """
    soma = 0
    if len(numeros) == 0:
        return None
    else:
        for numeros in numeros:
            soma += numeros
        return soma


def em_posicoes_impares(numeros):
    """Obtém os números que estão em posições ímpares.

    Por exemplo, para a lista [20, 30, 40, 50] retorna [30, 50] pois são os
    números que etão nas posições 1 e 3.
    """
    i = 0
    resposta = []
    if len(numeros) == 0:
        return None
    for _ in numeros:
        if i % 2 != 0 and i != 0:
            resposta.append(numeros[i])
        i += 1
    return resposta


def primeiro_e_ultimo(numeros):
    """Obtém o primeiro e o último número da lista.

    Caso não haja pelo menos dois números retorna None para indicar que
    o problema não tem solução.
    """
    if len(numeros) < 2:
        return None
    else:
        resposta = []
        resposta.append(numeros[0])
        resposta.append(numeros[len(numeros) - 1])
        return resposta


def conta_ocorrencias(numeros, numero):
    """Conta quantas vezes o numero aparece na lista numeros.
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = 0
        for num in numeros:
            if num == numero:
                resposta += 1
        return resposta
    


def posicao_do_maior(numeros):
    """Encontra a posição da primeira ocorrência do maior número da lista.

    Se a lista está vazia então retorna None.
    """
    if len(numeros) == 0:
        return None
    else:
        maior_num = 0
        resposta = 0
        for i in range(len(numeros)):
            if maior_num < numeros[i]:
                maior_num = numeros[i]
                resposta = i
        return resposta


        

def maior(numeros):
    """Encontra o maior número na lista.

    Se a lista estaá vazia (não possui números) então retorna None para
    indicar que o problema não tem solução.
    """
    if len(numeros) == 0:
        return None
    else:
        maior_num = 0
        for numero in numeros:
            if numero > maior_num:
                maior_num = numero
        return maior_num
    


def qtd_acima_limite(numeros, limite):
    """Conta quantos números na lista são maiores que um número limite.
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = 0
        for numero in numeros:
            if numero > limite:
                resposta += 1
        return resposta


def media(numeros):
    """Calcula a média aritmética dos números na lista.

    Se a lista está vazia então retorna None para indicar que o problema não
    tem solução.
    """
    if len(numeros) == 0:
        return None
    else:
        m = 0
        for numero in numeros:
            m += numero
        return m/len(numeros)



def qtd_no_intervalo(numeros, lim_inf, lim_sup):
    """Conta quantos números estão dentro do intervalo [lim_inf, lim_sup]

    Por exemplo, para numeros [8, 23, 10, 9, 15] e limite inferior 8 e
    limite superior 16 retorna 4.
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = 0
        for numero in numeros:
            if numero >= lim_inf and numero <= lim_sup:
                resposta += 1
        return resposta


def multiplica_por_fator(numeros, fator):
    """Multiplica cada número da lista por um fator. O método não retorna nenhum dado.

    Por exemplo, para numeros [8, 12, 3] e fator 2 a lista deve ser
    alterada para [16, 24, 6]. 
    """
    for i in range(len(numeros)):
        numeros[i] = numeros[i] * fator
    pass

def multiplicado_por_fator(numeros, fator):
    """Obtém uma cópia dos números da lista multiplicados por um fator.

    Por exemplo, para numeros [8, 12, 3] e fator 2 o algoritmo deve retornar
    uma nova lista com os números [16, 24, 6] SEM ALTERAR a lista numeros.
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = numeros.copy()
        for i in range(len(resposta)):
            resposta[i] = resposta[i] * fator
        return resposta


def n_primeiros(numeros, n):
    """Obtém uma cópia dos n primeiros números da lista.

    Considera que n sempre é maior ou igual a zero.
    Se n for maior que a quantidade de números na lista então obtém uma
    cópia de todos os números.
    """
    if len(numeros) == 0:
        return None
    else:
        a = len(numeros) - 1
        resposta = numeros.copy()
        for i in range(a, -1, -1):
            if i > (n - 1):
                resposta.pop(i)
        return resposta


def copia(numeros):
    """Obtém uma cópia dos números. Não pode usar método copy.
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = []
        for numero in numeros:
            resposta.append(numero)
        return resposta

def no_intervalo(numeros, lim_inf, lim_sup):
    """Obtém os números que estão dentro do intervalo.

    Por exemplo, se a lista for formada pelos números
    [8, 2, 3, 12, 9] e o intervalo for de 3 a 8 deve
    retornar [8, 3] pois são os únicos números maiores ou
    iguais a 3 e menores ou iguais a 8.
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = []
        for i in range(len(numeros)):
            if numeros[i] >= lim_inf and numeros[i] <= lim_sup:
                resposta.append(numeros[i])
        return resposta



def una(numeros1, numeros2):
    """Obtém uma nova lista que contém todos os números das duas listas.
    """
    if len(numeros1) == 0 and len(numeros2) == 0:
        return None
    else:
        resposta = numeros1.copy() + numeros2.copy()
        return resposta


def pares(numeros):
    """Obtém os números pares presentes na lista numeros.
    """
    resposta = []
    for numero in numeros:
        if numero % 2 == 0:
            resposta.append(numero)
    return resposta


def duplica(numeros):
    """Duplica a ocorrência dos números presentes na lista.

    Por exemplo, para a lista [3, 12, 4] retorna [3, 3, 12, 12, 4, 4]
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = []
        for numero in numeros:
            for _ in range(2):
                resposta.append(numero)
        return resposta

def possui_par(numeros):
    """Verifica se a lista possui pelo menos um número par.
    """
    if len(numeros) == 0:
        return False
    else:
        for numero in numeros:
            if numero % 2 == 0:
                return True
        return False



def primeira_posicao_de_numero(numeros, numero):
    """Obtém a primeira posição de um número na lista numeros.

    Por exemplo, para numeros [7, 12, 8, 2, 12] e numero 12 retorna 1. Se o
    número não aparece na lista deve retornar None.
    """
    if len(numeros) == 0:
        return None
    else:
        for i in range(len(numeros)):
            if numero == numeros[i]:
                return i
        return None

def posicoes_de_numero(numeros, numero):
    """Obtém as posições de um número na lista de números.

    Por exemplo, para numeros [12, 3, 9, 12, 6] e numero 12 retorna [0, 3]
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = []
        for i in range(len(numeros)):
            if numero == numeros[i]:
                resposta.append(i)
        return resposta


def sem_repeticoes(numeros):
    """Verifica se a lista não contém números repetidos.

    Retorna True se não tiver números repetidos e False caso contrário.
    """
    if len(numeros) == 0:
        return True
    else:
        repeticoes = 0
        for i in range(len(numeros)):
            for j in range(len(numeros)):
                if numeros[i] == numeros[j] and i != j:
                    repeticoes += 1
        return repeticoes == 0

    


def remove_ocorrencias(numeros, numero):
    """Retorna uma nova lista sem as ocorrências de um número.

    Por exemplo, para numeros [1, 4, 8, 4] e numero 4 retorna [1, 8]
    """
    if len(numeros) == 0:
        return None
    else:
        resposta = numeros.copy()
        for i in range(len(numeros)):
            if numero == numeros[i]:
                resposta.pop(i)
        return resposta


def substitui_ocorrencias(numeros, numero, substituto):
    """Substitui todas as ocorrências de um número por outro número.

    Altera a lista numeros e não retorna nada.
    """
    for i in range(len(numeros)):
        if numeros[i] == numero:
            numeros[i] = substituto
    pass

def substitui_primeira_ocorrencia(numeros, numero, substituto):
    """Substitui a primeira ocorrência de um número por outro número.

    Altera a lista numeros e não retorna nada.
    """
    for i in range(len(numeros)):
        if numeros[i] == numero:
            numeros[i] = substituto
            pass

def substitui_ultima_ocorrencia(numeros, numero, substituto):
    """Substitui a última ocorrência de um número por outro número.
    
    Altera a lista numeros e não retorna nada.
    Dica: percorra a lista de trás para frente
    """
    for i in range((len(numeros) - 1), -1, -1):
        if numeros[i] == numero:
            numeros[i] = substituto
            pass

def inverte(numeros):
    """Retorna nova lista com números em posições invertidas.

    Por exemplo: para numeros [3, 7, 1, 2] retorna a nova lista [2, 1, 7, 3]
    """
    resposta = []
    a = len(numeros) - 1
    for i in range(a, -1, -1):
        resposta.append(numeros[i])
    return resposta


def soma_pos_pares_pos_impares(numeros):
    """Calcula a soma dos números em posições pares e em posições ímpares.

    Retorna uma lista de tamanho 2 onde o primeiro número contém a soma dos
    números em posições pares (0, 2, 4, etc) e o segundo a soma dos números em posições
    ímpares (1, 3, 5, etc). Se a lista de números tiver menos de dois números então o método
    retorna None para indicar que o problema não tem solução.
    """
    if len(numeros) == 0:
        return None
    else:
        imp = 0
        par = 0
        resposta = []
        for i in range(len(numeros)):
            if i % 2 == 0 or i == 0:
                par += numeros[i]
            else:
                imp += numeros[i]
        resposta.append(par)
        resposta.append(imp)
        return resposta


def das_posicoes(numeros, posicoes):
    """Obtém os números que estão em diversas posições.

    Considera que a lista das posicoes, quando não está vazia,
    sempre contém posições válidas.
    """
    if len(numeros) == 0 or len(posicoes) == 0:
        return None
    else:
        resposta = []
        for i in posicoes:
            resposta.append(numeros[i])
    return resposta


def parte(numeros, pos, qtd):
    """Obtém uma parte da lista de números.

    O parâmetro pos indica a posição onde inicia a parte. O parâmetro qtd
    indica quantos números devem ser incluídos na parte. Se a posição 
    for maior ou igual a quantidade de números
    então retorna uma lista vazia. Se a quantidade de números desejada for
    maior que a quantidade de números existentes a partir da posição pos 
    então retorna todos números existentes a partir de pos.

    Exemplo: considere os números [6, 3, 4, 1, 2].
    Se a quantidade for 2 e a posição for 1 então retorna [3, 4].
    Se a quantidade for 3 e a posição for 4 então retorna [2].
    Se a quantidade for 2 e a posição for 9 então retorna []
    """
    for i in range(len(numeros)):
        if i < pos:
            numeros.pop(i)
    for j in range(len(numeros) - 1, -1, -1):
        if qtd < len(numeros):
            numeros.pop(j)
    return numeros

    
