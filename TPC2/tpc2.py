import sys


def calcula(string):
    soma=0
    on=True
    i=0
    for a in string:
        if(a == 'o' or a == 'O') and (string[i + 1] == 'n' or string[i + 1] == 'N'):
            on=True
        if (a=='o' or a=='O') and (string[i+1]=='f' or string[i+1] == 'F') and (string[i+2]=='f' or string[i+2] == 'F'):
            on=False
        if a.isdigit() and on:
            soma=soma+int(a)
        if a == '=':
            print(soma)
            res=0
        i+=1
    print (soma)

if __name__ == '__main__':
    for line in sys.stdin:
        if line== "exit":
            break
        calcula(line)