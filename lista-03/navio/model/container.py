# --------------------------
# UFSC - CTC - INE - INE5663
# Exercício do Navio
# --------------------------
# Classe que representa um container.
#

class Container:
    '''Um container é caracterizado pelo seu código e pelo seu peso.
    '''
    def __init__(self, codigo, peso):
        self._CODIGO = codigo
        self._PESO = peso
        
    def codigo(self):
        '''Retorna o código do container.
        '''
        return self._CODIGO
    
    def peso(self):
        '''Retorna o peso do container.
        '''
        return self._PESO
    
    def __str__(self):
        '''Retorna uma string representando os dados container.
        '''
        return 'codigo:' + self._CODIGO + ' peso:' + str(self._PESO)
