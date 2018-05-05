# Campos do Mips
- TIPO R ->  OP(6 bits) - RS(5 bits) - RT(5 bits) - RD(5 bits) - SHAMT(5 bits) - FUNCT(6 bits)
- TIPO I ->  OP(6 bits) - RS(5 bits) - RT(5 bits) - CONST(16 bits)
- TIPO 'P' -> Pseudo instruções (viram instruções tipo R e tipo I)

# Partes da Instrução
- OP: Operação básica da instrução, tradicionalmente chamada de opcode
- RS: Registrador do primeiro operando de origem
- RT: Registrador do segundo operando de origem
- RD: Registrador do operando de destino
- SHAMT: “Shift amount”, quantidade de deslocamento
- FUNCT: Função. Seleciona variante específica da operação. Código de função.
- CONST: Constante ou endereço

# Ordem Comandos
-  'add':  ['op', 'rd', 'rs', 'rt'],
-  'sub':  ['op', 'rd', 'rs', 'rt'],
-  'and':  ['op', 'rd', 'rs', 'rt'],
-  'or':   ['op', 'rd', 'rs', 'rt'],
-  'ori':  ['op', 'rt', 'rs', 'const'],
-  'nor':  ['op', 'rd', 'rs', 'rt'],
-  'sll':  ['op', 'rd', 'rt', 'shamt'],
-  'srl':  ['op', 'rd', 'rt', 'shamt'],
-  'addi':  ['op', 'rt', 'rs', 'const'],
-  'andi':  ['op', 'rt', 'rs', 'const'],

# Pseudo Instruções
-  'move' ['op', 'rd', 'rs'],
-  'clear' ['op', 'rd']

# Registardores Mips
- $zero = 0
- $t0...$t7 = 8-15
- $s0...$s7 = 16-23
