def registerValue(reg):
    """
    Retorna o valor numérico do registrador fornecido

    Args:
        reg (str): Registrador a ser analisado (ex: $s0, $t1..)

    Returns:
        int: Valor numérico do registrador fornecido
    """
    if (reg == '$zero'):
        return 0 # '000000'

    lastBit = int(reg[2])
    sumFactor = 16 if (reg[1] == 's') else 8

    return lastBit + sumFactor
