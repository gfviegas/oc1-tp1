# Registardores Mips
# $zero = 0
# $t0...$t7 = 8-15
# $s0...$s7 = 16-23

def binarioRegistrador(reg):
    if (reg == '$zero'):
        return 0 # '000000'

    ultimoBit = int(reg[2])
    fatorSoma = 16 if (reg[1] == 's') else 8

    return ultimoBit + fatorSoma
