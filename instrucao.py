# Campos do Mips
# TIPO R ->  OP(6 bits) - RS(5 bits) - RT(5 bits) - RD(5 bits) - SHAMT(5 bits) - FUNCT(6 bits)
# TIPO I ->  OP(6 bits) - RS(5 bits) - RT(5 bits) - CONST(16 bits)
#
# OP: Operação básica da instrução, tradicionalmente chamada de opcode
# RS: Registrador do primeiro operando de origem
# RT: Registrador do segundo operando de origem
# RD: Registrador do operando de destino
# SHAMT: “Shift amount”, quantidade de deslocamento
# FUNCT: Função. Seleciona variante específica da operação. Código de função.
# CONST: Constante ou endereço
#
# Ordem Comandos
#  'add':  ['op', 'rd', 'rs', 'rt'],
#  'sub':  ['op', 'rd', 'rs', 'rt'],
#  'and':  ['op', 'rd', 'rs', 'rt'],
#  'or':   ['op', 'rd', 'rs', 'rt'],
#  'nor':  ['op', 'rd', 'rs', 'rt'],
#  'sll':  ['op', 'rd', 'rt', 'shamt'],
#  'srl':  ['op', 'rd', 'rt', 'shamt'],
#  'addi':  ['op', 'rt', 'rs', 'const'],
#  'andi':  ['op', 'rt', 'rs', 'const']

from registrador import binarioRegistrador

class Instrucao(object):
    def __init__(self, instrucao):
        self.comandos = instrucao.lower().replace(',', '').split()

    def tipo(self):
        return {
            'add': 'r',
            'sub': 'r',
            'and': 'r',
            'or': 'r',
            'nor': 'r',
            'addi': 'i',
            'andi': 'i',
            'sll': 'r',
            'srl': 'r'
        }[self.comandos[0]]

    def op(self):
        if (self.tipo() == 'r'):
            return 0    # '000000'

        return {
            'addi': 8,  # '001000'
            'andi': 12  # '001100'
        }[self.comandos[0]]

    def funct(self):
        return {
            'add':  32, # '100000'
            'sub':  34, # '100010'
            'and':  36, # '100100'
            'or':   37, # '100101'
            'nor':  39, # '100111'
            'sll':  0,  # '000000'
            'srl':  2   # '000010'
        }[self.comandos[0]]

    def binario(self):
        op = '{0:06b}'.format(self.op())

        # O rs é o terceiro nos comandos a seguir, e no SLL, SRL, ele é zero sempre
        if (self.comandos[0] in ['add', 'sub', 'and', 'or', 'nor', 'addi', 'andi']):
            rs = '{0:05b}'.format(binarioRegistrador(self.comandos[2]))
        else:
            rs = '{0:05b}'.format(0)

        # O rt é o quarto nos comandos a seguir
        if (self.comandos[0] in ['add', 'sub', 'and', 'or', 'nor']):
            rt = '{0:05b}'.format(binarioRegistrador(self.comandos[3]))
        elif (self.comandos[0] in ['sll', 'srl']):
            rt = '{0:05b}'.format(binarioRegistrador(self.comandos[2])) # É o terceiro nos comandos a seguir
        else:
            rt = '{0:05b}'.format(binarioRegistrador(self.comandos[1])) # E o segundo nos do tipo I

        if (self.tipo() == 'r'):
            # O rd é sempre o segundo, no tipo R
            rd = '{0:05b}'.format(binarioRegistrador(self.comandos[1]))

            # O shamt é o quarto nos SLL e SRL, e 0 nos restante
            if (self.comandos[0] in ['sll', 'srl']):
                shamt = '{0:05b}'.format(binarioRegistrador(self.comandos[3]))
            else:
                shamt = '{0:05b}'.format(0)

            funct = '{0:06b}'.format(self.funct())
            return op + rs + rt + rd + shamt + funct
        else:
            const = '{0:016b}'.format(int(self.comandos[3]))
            return op + rs + rt + const
