package br.com.meuBanco;

public class ContaCorrente extends Conta {
    public ContaCorrente(String titular, double saldoInicial) {
        super(titular, saldoInicial);
    }

    @Override
    public boolean sacar(double valor) {
        if (saldo >= valor) {
            saldo -= valor;
            System.out.println("Saque de " + valor + " realizado com sucesso.");
            return true;
        } else {
            System.out.println("Erro: Saldo insuficiente para saque de " + valor);
            return false;
        }
    }
}
