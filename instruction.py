from register import registerValue
from binary import toBin

class instruction(object):
    def __init__(self, instruction):
        self.commands = instruction.lower().replace(',', '').split()

    def availableCommands(self):
        """ Retorna uma lista com os comandos disponíveis/suportados pelo programa. """
        return ['add', 'sub', 'and', 'clear', 'or', 'ori', 'move', 'nor', 'addi', 'andi','sll', 'srl']

    def type(self):
        """
        Retorna o tipo da instrução

        Returns:
            str: Letra representando o tipo da instrução, que pode ser R, I ou P (Pseudo).

        Raises:
            KeyError: Se o comando da instrução não for suportado pelo programa (vide self.availableCommands)
        """

        return {
            'add': 'r',
            'sub': 'r',
            'and': 'r',
            'clear': 'p',
            'or': 'r',
            'ori': 'i',
            'move': 'p',
            'nor': 'r',
            'addi': 'i',
            'andi': 'i',
            'sll': 'r',
            'srl': 'r'
        }[self.commands[0]]

    def op(self):
        """
        Retorna o OP Code da instrução

        Returns:
            int: Valor numérico do OP da instrução

        Raises:
            KeyError: Se o comando da instrução for do tipo I e não for suportado pelo programa (vide self.availableCommands)
        """
        if (self.type() == 'r' or self.type() == 'p'):
            return 0    # '000000'

        return {
            'addi': 8,  # '001000'
            'andi': 12,  # '001100'
            'ori':  13 # '001101'
        }[self.commands[0]]

    def funct(self):
        """
        Retorna o funct da instrução

        Returns:
            int: Valor numérico do FUNCT da instrução

        Raises:
            KeyError: Se o comando da instrução não for suportado pelo programa (vide self.availableCommands) ou não possuir FUNCT (tipo I || P)
        """
        return {
            'add':  32, # '100000'
            'sub':  34, # '100010'
            'and':  36, # '100100'
            'or':   37, # '100101'
            'nor':  39, # '100111'
            'sll':  0,  # '000000'
            'srl':  2   # '000010'
        }[self.commands[0]]

    def pseudo(self):
        """
        Mapeia pseudo-instruções à suas instruções devidas

        Returns:
            str: Comando correspondente à pseudo-instrução

        Raises:
            KeyError: Se o comando da instrução não for do tipo P ou não for suportado pelo programa (vide self.availableCommands)
        """
        return {
            'move': 'add',
            'clear': 'add'
        }[self.commands[0]]

    def binary(self):
        """
        Calcula o valor binário final de uma instrução, considerando todos os aspectos da instrução

        Returns:
            str: Sequência binária da instrução
        """

        # confere se comando existe
        if(not self.commands[0] in self.availableCommands()):
            print("Comando '" + self.commands[0] + "' não encontrado")
            return 0

        # verifica se é uma das pseudo instruções e completa parâmetros
        if(self.type() == 'p'):
            if(self.commands[0] == 'clear'):
                self.commands.append('$zero')
            self.commands[0] = self.pseudo()
            self.commands.append('$zero')

        op = toBin(self.op(), 6)

        # O rs é o terceiro nos comandos a seguir, e no SLL, SRL, ele é zero sempre
        if (self.commands[0] in ['add', 'sub', 'and', 'or', 'nor', 'addi', 'andi']):
            rs = toBin(registerValue(self.commands[2]), 5)
        else:
            rs = toBin(0, 5)

        # O rt é o quarto nos comandos a seguir
        if (self.commands[0] in ['add', 'sub', 'and', 'or', 'nor']):
            rt = toBin(registerValue(self.commands[3]), 5)
        elif (self.commands[0] in ['sll', 'srl']):
            rt = toBin(registerValue(self.commands[2]), 5) # É o terceiro nos comandos a seguir
        else:
            rt = toBin(registerValue(self.commands[1]), 5) # E o segundo nos do tipo I

        if (self.type() == 'r' or self.type() == 'p'):
            # O rd é sempre o segundo, no tipo R
            rd = toBin(registerValue(self.commands[1]), 5)

            # O shamt é o quarto nos SLL e SRL, e 0 nos restante
            if (self.commands[0] in ['sll', 'srl']):
                shamt = toBin(int(self.commands[3]), 5)
            else:
                shamt = toBin(0, 5)

            funct = toBin(self.funct(), 6)
            return op + rs + rt + rd + shamt + funct
        else:
            const = toBin(int(self.commands[3]), 16)
            return op + rs + rt + const
