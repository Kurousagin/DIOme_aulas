using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Csharpier.models
{
    public class venda
    {


    

        private List<string> produto = new List<string>();


        public void adicionarProduto()
        {

            Console.WriteLine("Digite o nome do produto: \n ");
            string prod = Console.ReadLine();
            produto.Add(prod);

        }
        public void Venda(){
            Console.WriteLine("Digite o SKU para adicionar a quantidade:");

            string sku = Console.ReadLine();

            if(produto.Any(x => x.ToUpper() == sku.ToUpper())){
                Console.WriteLine("Digite a quantidade");
                int quantidade = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine($"SKU: {sku} Quantidade: {quantidade}");

            }
        }

        public void exibeProdutos()
        {
            if (produto.Any())
            {
                Console.WriteLine("Os produtos disponiveis são:");
                foreach (string produtos in produto)
                {
                    Console.WriteLine(produtos);
                }
            }
            else
            {
                Console.WriteLine("Não há produtos Disponiveis");
            }

        }

   


    }
}