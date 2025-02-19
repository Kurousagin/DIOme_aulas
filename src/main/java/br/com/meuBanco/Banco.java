package br.com.meuBanco;

public class Banco {
    public static void main(String[] args) {
        ContaCorrente cc = new ContaCorrente("Carlos", 100);
        ContaPoupanca cp = new ContaPoupanca("Ana", 50);

        cc.sacar(120);
        cp.sacar(30);
        cp.sacar(50);
    }
}
