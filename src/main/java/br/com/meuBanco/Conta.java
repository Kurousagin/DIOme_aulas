package br.com.meuBanco;

public abstract class Conta {
    protected double saldo;
    protected String titular;

    public Conta(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public abstract boolean sacar(double valor);
}
