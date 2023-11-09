using System;
using Csharpier.models;
using Newtonsoft.Json;
//Lê Json
//  string arquivo = File.ReadAllText("Vendas.Json");
//   List<Vendajs> listaVenda = JsonConvert.DeserializeObject<List<Vendajs>>(arquivo);

//  foreach (Vendajs venda in listaVenda)
//  {
//      Console.WriteLine($"ID: {venda.Id}, Produto: {venda.Produto}, Preco:{venda.Preco},"+
//      $" Data: {venda.Datavenda.ToString("dd/MM/yyyy")}, {(venda.desconto.HasValue ? $"Desconto de : {venda.desconto}" : "")} ");
//  }

//cria Json 


//

// string serializado = JsonConvert.SerializeObject(Listavendas, Formatting.Indented);
// File.WriteAllText("Vendas.Json", serializado);
// Console.WriteLine(serializado);



// venda v1 = new venda();

// string opcao = string.Empty;
// bool exibirMenu = true;

// while (exibirMenu)
// {
//     Console.Clear();
//     Console.WriteLine("Digite o numero da opção desejada: \n");
//     Console.WriteLine("1 - Cadastrar SKU");
//     Console.WriteLine("2 - Exibir SKU's");
//     Console.WriteLine("3 - Adicionar quantidade de SKU's");
//     Console.WriteLine("4 - SAIR");

//     switch (Console.ReadLine())
//     {
//         case "1":
//             v1.adicionarProduto();
//             break;
//         case "2":
//             v1.exibeProdutos();
//             break;
//         case "3":
//             v1.Venda();
//             break;
//         case "4":
//             exibirMenu = false;
//             break;

//         default:
//             Console.WriteLine("Opção inválida");
//             break;
//     }
//     Console.WriteLine("Pressione ENTER para continuar");
//     Console.ReadLine();
// }
// Console.WriteLine("Programa encerrado");




// bool? desejareceber = true;

// if(desejareceber.HasValue && desejareceber.Value){
//     Console.WriteLine("Usuario optou por receber o email");
// }
// else{
//     Console.WriteLine("Usuario optou por não responder");

// }
