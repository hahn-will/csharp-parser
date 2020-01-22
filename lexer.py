import ply.lex as lex

states = (('wordstate', 'exclusive'),
          )

tokens = (
    'WORD',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'LSQUARE',
    'RSQUARE',
    'LANGLE',
    'RANGLE',
    'STARTWORD',
    'SEMICOLON'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = R'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LANGLE = r'\<'
t_RANGLE = r'\>'
t_SEMICOLON = r';'

def t_STARTWORD(t):
    r'[a-zA-Z][^ \t\r\n]'
    t.value = str(t.value)
    t.lexer.begin('wordstate')

def t_wordstate_WORD(t):
    r'[a-zA-Z0-9_]+'
    t.value = str(t.value)
    t.lexer.begin('INITIAL')

t_ignore = ' \t\r\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])


def t_wordstate_error(t):  # Special error handler for state 'bar'
    pass

lexer = lex.lex()

data = '''
public class test {
    public int test {get; set;}
}
'''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)