import ply.lex as lex

tokens = (
'COMMENT',
'MULTICOMMENT',
'FUNCTION_INIT',
'FUNCTION',
'PROGRAM_INIT',
'VARIABLE_INIT',
'VARIABLE_OP',
'CYCLE',
'CHAVETAOPEN',
'CHAVETACLOSE',
'PAROPEN',
'PARCLOSE'
)

t_COMMENT = r'//(.*)\n'
t_MULTICOMMENT = r'\/\*(.*?|\n)*\*\/'
t_FUNCTION_INIT = r'function ([^{]*)'
t_FUNCTION = r'[a-zA-Z0-9]*\(([a-zA-Z0-9, \(\)]*)\);*'
t_PROGRAM_INIT = r'program ([^{]*)'
t_VARIABLE_INIT = r'(int|double|float|char)\ (.*)'
t_VARIABLE_OP = r'[a-zA-Z0-9]*\ *=\ *(.*);'
t_CYCLE = r'(while|for)\ ([^{]*)'
t_CHAVETAOPEN = r'\{'
t_CHAVETACLOSE = r'\}'
t_PAROPEN = r'\('
t_PARCLOSE = r'\)'
t_ignore = "\n \t"

def t_error(t):
    print(f"Carater invalido -> {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

arquivo = open('exemplo1.txt', 'r')
conteudo = arquivo.read()
arquivo.close()


lexer.input(conteudo)

while tok := lexer.token():
    print(tok)