from xmlrpc.server import SimpleXMLRPCServer
class RPC:
    methods = ['isValid', 'calc'] #nome dos metodos
    operators = {
        '+':'+',
        '-': '-',
        '*':'*',
        '/':'/'
    }
    def __init__(self, direction, port):
        #estabelecendo a conexão com o servidor
        self.server = SimpleXMLRPCServer((direction, port), allow_none=True)

        for method in self.methods:
            self.server.register_function(getattr(self, method))


    def isValid(self, oper):
        return oper in self.operators 

    def calc(self, a, b, oper):
        c = 0
        if  oper == self.operators['+']:
            c = a+b
        elif oper == self.operators['-']:
            c = a-b
        elif oper == self.operators ['*']:
            c = a*b
        elif oper == self.operators ['/']:
            c = a/b
        else:
            return 'operação não é válida'
        return c

    def run (self):
        self.server.serve_forever()
        print ('Servidor Iniciado')

if __name__ == '__main__':
    rpc = RPC('', 20064)
    print ('Iniciando o Servidor...')
    rpc.run()