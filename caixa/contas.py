class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo= 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)


    def resumo(self):
        print("CC numero: %s Saldo: %10.2f" %(self.numero,self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else
            print("Valor não suficiente")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print("Extrato CC n %s\n" % self.numero)
        for o in self.operacoes:
            print("%10s %10.2f\n" % (o[0], o[1]))
        print("\n   Saldo: %10.2f\n" %self.saldo)