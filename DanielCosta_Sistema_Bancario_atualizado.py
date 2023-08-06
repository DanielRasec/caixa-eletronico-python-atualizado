# @DanielRasec
from datetime import datetime
# Criação de usuários
usuarios = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: CPF já cadastrado.")
            return
    
    # Aqui faremos a verificação de idade
    data_nascimento_obj = datetime.strptime(data_nascimento, "%d/%m/%Y")
    idade = (datetime.now() - data_nascimento_obj).days // 365
    
    if idade < 18:
        print("Erro: Desculpe, você não pode abrir uma conta pois não atingiu a idade mínima de 18 anos.")
        return
    
    usuarios.append(novo_usuario)
    print("Usuário criado, Parabéns por fazer parte do nosso time.")

class Conta:
    numero_conta = 1

    def __init__(self, tipo, usuario):
        self.tipo = tipo
        self.agencia = "0001"
        self.numero = Conta.numero_conta
        Conta.numero_conta += 1
        self.saldo = 0
        self.usuario = usuario
        self.extrato = ""

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Erro: Valor inválido.")

# Abaixo a verificação da seleção desejada do usuário para o menu
# Também o menu atualizado
contas = []

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    menu = """
    [u] Criar Usuário
    [c] Criar Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu)
        if opcao == "u":
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço (Logradouro, Número, Bairro, Cidade, UF): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == "c":
            cpf = input("CPF do usuário: ")
            usuario_encontrado = None
            for usuario in usuarios:
                if usuario["cpf"] == cpf:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                tipo_conta = input("Tipo de conta (corrente/poupança): ")
                if tipo_conta == "corrente" or tipo_conta == "poupança":
                    nova_conta = Conta(tipo=tipo_conta, usuario=usuario_encontrado)
                    contas.append(nova_conta)
                    print(f"Conta {tipo_conta} criada com sucesso para {usuario_encontrado['nome']}.")
                else:
                    print("Erro: Tipo de conta inválida.")
            else:
                print("Erro: Cliente não encontrado.")
        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite em valores R$.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido por dia = 3.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
