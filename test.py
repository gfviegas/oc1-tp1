import unittest

from main import proccessAssemblyFile
from binary import toBin
from register import registerValue
from instruction import instruction

class MainTest(unittest.TestCase):
    randomInst = instruction('add $s2, $s0, $s1') # add, tipo R
    randomInst2 = instruction('addi $t3, $t2, -243') # addi, tipo I
    randomInst3 = instruction('move $s0, $s1') # move, tipo P

    def test_conversaoBinario(self):
        x = toBin(5, 4)
        self.assertEqual('0101', x)

    def test_conversaoBinarioNegativo(self):
        # Testa o complemento de 2
        x = toBin(-5, 4)
        self.assertEqual('1011', x)

    def test_registerZero(self):
        self.assertEqual(registerValue('$zero'), 0)

    def test_registerS(self):
        self.assertEqual(registerValue('$s0'), 16)
        self.assertEqual(registerValue('$s1'), 17)
        self.assertEqual(registerValue('$s5'), 21)
        self.assertEqual(registerValue('$s7'), 23)

    def test_registerT(self):
        self.assertEqual(registerValue('$t0'), 8)
        self.assertEqual(registerValue('$t1'), 9)
        self.assertEqual(registerValue('$t5'), 13)
        self.assertEqual(registerValue('$t7'), 15)

    def test_commandsAvailable(self):
        self.assertEqual(type(self.randomInst.availableCommands()).__name__, 'list')
        self.assertTrue(len(self.randomInst.availableCommands()) > 8)

    def test_instructionType(self):
        self.assertEqual(type(self.randomInst.type()).__name__, 'str')
        self.assertEqual(self.randomInst.type(), 'r')
        self.assertEqual(self.randomInst2.type(), 'i')
        self.assertEqual(self.randomInst3.type(), 'p')

    def test_instructionOp(self):
        self.assertEqual(type(self.randomInst.op()).__name__, 'int')
        self.assertEqual(self.randomInst.op(), 0)
        self.assertEqual(self.randomInst2.op(), 8)

    def test_instructionFunct(self):
        self.assertEqual(type(self.randomInst.funct()).__name__, 'int')
        self.assertEqual(self.randomInst.funct(), 32)
        self.assertRaises(KeyError, self.randomInst2.funct)

    def test_instructionPseudo(self):
        self.assertEqual(type(self.randomInst3.pseudo()).__name__, 'str')
        self.assertEqual(self.randomInst3.pseudo(), 'add')
        self.assertRaises(KeyError, self.randomInst.pseudo)
        self.assertRaises(KeyError, self.randomInst2.pseudo)

    def test_binario(self):
        self.assertEqual(type(self.randomInst.binary()).__name__, 'str')
        self.assertEqual(len(self.randomInst2.binary()), 32)

        self.assertEqual(self.randomInst.binary(), '00000010000100011001000000100000')
        self.assertEqual(self.randomInst2.binary(), '00100001010010111111111100001101')

    def test_main(self):
        proccessAssemblyFile('tests/input.asm', 'tests/generatedOutput.txt')
        with open('tests/generatedOutput.txt') as generatedOutput:
            generatedOutputLines = generatedOutput.readlines()
        with open('tests/expectedOutput.txt') as expectedOutput:
            expectedOutputLines = expectedOutput.readlines()
        self.assertEqual(generatedOutputLines, expectedOutputLines)

if __name__ == '__main__':
    unittest.main()
