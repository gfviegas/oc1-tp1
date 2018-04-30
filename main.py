from instrucao import Instrucao

print('****************************************************')
print('*   SUPER MONTADOR MIPS - UFV Florestal            *')
print('*  por: Bruno Marra (3029), Gustavo Viegas (3026)  *')
print('****************************************************')

print('Lendo arquivo de entrada...')

with open('entrada.asm') as entrada:
    linhas = entrada.readlines()

print('Arquivo lido! Processando entrada...')
with open('saida.txt', 'w') as saida:
    saida.truncate()
    for linha in linhas:
        inst = Instrucao(linha.strip()) # Removendo whitespaces com strip
        if(inst.binario()):
            saida.write(inst.binario() + '\n')

print('Montagem feita com sucesso! O arquivo binário está disponivel em saida.txt! \n')

# EXEMPLOS:
# inst2 = Instrucao('addi $t0, $s0, 30')
# print(inst2.tipo())
# print(inst2.op())
# print(inst2.binario())
