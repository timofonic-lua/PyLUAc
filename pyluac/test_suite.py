'''
PyLUAc Test suite
'''
import unittest

from pyluac.lexer import lexer

class PyLUAcLexerTest(unittest.TestCase):
    '''
    PyLUAc Lexer test class
    '''

    def test_basic(self):
        data = 'print("It\'s Never Lupus!")'
        lexer.input(data)

        tokens = list(lexer)
        self.assertEqual([tok.type for tok in tokens],
            ['ID', '(', 'STRING', ')'])

    def test_indentation(self):
        data = 'one\n    two\n    three\n        four\n\n    five\n'
        lexer.input(data)

        tokens = list(lexer)
        self.assertEqual([tok.type for tok in tokens],
            ['ID', 'INDENT', 'ID', 'ID', 'INDENT', 'ID', 'DEDENT', 'ID', 'DEDENT'])

        
    

if __name__ == '__main__':
    unittest.main()

