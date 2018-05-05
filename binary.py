def toBin(number, length):
    """
    Converte um inteiro para binário, com complemento de dois

    Args:
        number (int): Inteiro a ser convertido
        length (int): Número de bits do binário retornado

    Returns:
        str: String formatada em binário com tamanho fixo e complemento de dois
    """
    binaryFormat = '0' + str(length) + 'b'
    return format(number if number >= 0 else ((1 << length) + number), binaryFormat)
