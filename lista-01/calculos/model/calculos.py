# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício calculos
# --------------------------
# Definição das funções que realizam cálculos diversos.



def media_de_tres_numeros(n1, n2, n3):
    """Calcula a média de três números.
    """
    return (n1 + n2 + n3)/3


def soma_de_tres_numeros(n1, n2, n3):
    """Calcula a soma de três números.
    """
    return n1 + n2 + n3


def par(n):
    """Verifica se um número é par.

    Retorna True se for par ou False caso contrário.
    Dica: a expressão 5 % 3 vale 2 pois 2 é o resto da divisão de 5 por 3.
    """
    if n % 2 == 0:
        return True
    else:
        return False

def menor_de_tres_numeros(n1, n2, n3):
    """Encontra o menor de três números.
    """
    menor = n1
    if menor > n2:
        menor = n2
    if menor > n3:
        menor = n3
    return menor



def maior_que(n1, n2):
    """Verifica se o primeiro número é maior que segundo número.

    Retorna True se n1 for maior que n2 ou False caso contrário.
    """
    if n1 > n2:
        return True
    else:
        return False


def divisivel_por(n1, n2):
    """Verifica se o primeiro número é divisível pelo segundo número.

    Retorna True se n1 for divisível por n2 ou False caso contrário.
    Observação: considera que n1 sempre é maior ou igual a zero e que
    n2 sempre é maior que zero.
    """
    if n1 % n2 == 0:
        return True
    else:
        return False


def multiplica(n1, n2):
    """Multiplica dois números maiores ou iguais a zero.

    Atenção: seu algoritmo não pode usar o símbolo '*'.
    """
    m = 0
    while n1 > 0:
        m += n2
        n1 -= 1
    return m

def divide(n1, n2):
    """Faz a divisão inteira do primeiro número pelo segundo número.

    Retorna o resultado da divisão inteira de n1 por n2.
    Exemplo: divide(8,5) retorna 1. O mesmo que 8 // 5.
    Considera que n1 sempre será maior ou igual a zero e que n2
    sempre será maior que zero.
    Atenção: seu algoritmo não pode usar o símbolo '//'.
    """
    return int(n1 / n2)

def bissexto(ano):
    """Verifica se um ano é bissexto.

    Retorna True se ano for bissexto ou False caso contrário.
    Definição de ano bissexto:
    Um ano é bissexto se for divisível por 400 ou então
    se for divisível por 4 e, ao mesmo tempo, não for divisível por 100.
    """
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False


def mdc(n1, n2):
    """Calcula o Máximo Divisor Comum entre dois números inteiros positivos.

    Dica: Utilize o Método das Divisões Sucessivas. Veja o método em
    http://www.mundoeducacao.com/matematica/mdc-divisoes-sucessivas.htm
    """
    if n1 > n2:
        loop = n2
        while loop > 0:
            if n1 % loop == 0 and n2 % loop == 0:
                return loop
            else:
                loop -= 1
    else:
        loop = n1
        while loop > 0:
            if n2 % loop == 0 and n1 % loop == 0:
                return loop
            else:
                loop -= 1


def soma_dos_divisores(n):
    """Calcula a soma dos divisores de um número inteiro maior que zero.

    Dica: a metade de n é n // 2.
    """
    soma = 1 + n
    d = n/2
    while d > 1:
        if n % d == 0:
            soma += d
        d -= 1
    return soma


def amigos(n1, n2):
    """Verifica se dois números inteiros positivos são amigos.

    Retorna True se números são amigos ou False caso contrário.
    Dica: Números Amigos: http://www.matematica.br/historia/namigos.html
    """
    d1 = n1 / 2
    d2 = n2 / 2
    somad1 = 0
    somad2 = 0
    while d1 > 0:
        if n1 % d1 == 0:
            somad1 += d1
        d1 -= 1
    while d2 > 0:
        if n2 % d2 == 0:
            somad2 += d2
        d2 -= 1
    if somad1 == n2 and somad2 == n1:
        return True
    else:
        return False


def primo(n):
    """Verifica se número é primo.
    
    Considera que n sempre é maior que 1.
    Retorna True se n for primo ou False caso contrário.
    """
    num = n - 1
    while num > 1:
        if n % num == 0:
            return False
        num -= 1
    if num == 1 or n == 1 or n == 2 or n == 3:
        return True



def composto(n):
    """Verifica se um número é composto.

    Considera que n sempre é maior que 1.
    Retorna True se n for número composto ou False caso contrário.
    Definição: um número é composto se possui mais de dois divisores.
    """
    num = n - 1
    while num > 1:
        if n % num == 0:
            return True
        num -= 1
    if num == 1:
        return False

