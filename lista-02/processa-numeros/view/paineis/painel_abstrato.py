# --------------------------
# UFSC - CTC - INE - INE5603
# Exercício Processa Números
# --------------------------
# Classe que descreve o comportamento padrão de todo tipo de painel

from abc import ABC, abstractmethod

class PainelAbstrato(ABC):
    def __init__(self, titulo):
        self._titulo = titulo

    def execute(self):
        titulo = '- - - - {} - - - - '.format(self._titulo)
        outraVez = True
        while outraVez:
            print(titulo)
            self.interaja()
            outraVez = 's' == input('Executar outra vez? [s/n] :')
        print('- - - - Fim')

    @abstractmethod
    def interaja(self):
        pass

    def _leiaints(self, msg='Digite os números separados por vírgula ou enter para nenhum número: '):
        leu = False
        while not leu:
            snums = input(msg)
            if snums == '':
                leu = True
                nums = []
            else:
                snums = snums.split(',')
                nums = []
                try:
                    for snum in snums:
                        nums.append(int(snum))
                    leu = True
                except ValueError:
                    print('Digite apenas números!')
        return nums

    def _leia3int(self):
        n1 = self._leia_int('Primeiro número: ')
        n2 = self._leia_int('Segundo número: ')
        n3 = self._leia_int('Terceiro número: ')
        return (n1, n2, n3)

    def _leia2int(self):
        n1 = self._leia_int('Primeiro número: ')
        n2 = self._leia_int('Segundo número: ')
        return (n1, n2)

    def _leia1int(self, msg='Digite um número: '):
        return self._leia_int(msg)

    def _leia_int(self, msg):
        leu = False
        while not leu:
            try:
                numero = int(input(msg))
                leu = True
            except ValueError:
                print('Erro! Você deve digitar um número inteiro.')

        return numero

