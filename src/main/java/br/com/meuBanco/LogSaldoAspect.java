package br.com.meuBanco;

import org.aspectj.lang.annotation.*;

@Aspect
public class LogSaldoAspect {

    @Before("execution(* br.com.meuBanco.Conta.sacar(..)) && args(valor)")
    public void verificarSaldo(double valor) {
        System.out.println("[LOG] Tentando sacar: R$ " + valor);
    }

    @AfterReturning(pointcut = "execution(* br.com.meuBanco.Conta.sacar(..))", returning = "resultado")
    public void verificarResultado(boolean resultado) {
        if (!resultado) {
            System.out.println("[ERRO] Saldo insuficiente para saque!");
        }
    }
}
