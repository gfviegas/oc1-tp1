from instruction import instruction

def printHeader():
    print('****************************************************')
    print('*   SUPER MONTADOR MIPS - UFV Florestal            *')
    print('*  por: Bruno Marra (3029), Gustavo Viegas (3026)  *')
    print('****************************************************')

def processarEntrada(inputFile, outputFile):
    print('Lendo arquivo de entrada...')

    with open(inputFile) as input:
        lines = input.readlines()

    print('Arquivo lido! Processando entrada...')
    with open(outputFile, 'w') as output:
        output.truncate()
        for line in lines:
            inst = instruction(line.strip()) # Removendo whitespaces com strip
            if(inst.binary()):
                output.write(inst.binary() + '\n')

    print('Montagem feita com sucesso! O arquivo binário está disponivel em output.txt! \n')


if __name__ == "__main__":
    printHeader()
    processarEntrada('input.asm', 'output.txt')

    # EXEMPLOS:
    # inst2 = instruction('add $s1, $s2, $s3')
    # print(inst2.type())
    # print(inst2.op())
    # print(inst2.binary())
