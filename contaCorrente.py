class Conta():
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo algo...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    pass

    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor