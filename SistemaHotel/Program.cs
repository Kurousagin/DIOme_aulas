using System.Text;
using SistemaHotel.Models;

Console.OutputEncoding = Encoding.UTF8;


List<Pessoa> hospedes = new List<Pessoa>();
Console.WriteLine("Digite o nome dos Hóspedes");
Pessoa p1 = new Pessoa(Console.ReadLine());
Pessoa p2 = new Pessoa(Console.ReadLine());
Pessoa p3 = new Pessoa(Console.ReadLine());

hospedes.Add(p1);
hospedes.Add(p2);
hospedes.Add(p3);


Suite suite = new Suite(tipoSuite: "Premium", capacidade: 5, valorDiaria: 30);

Console.WriteLine("Quantos dias pretende reservar?");
Reserva reserva = new Reserva(diasReservados: System.Convert.ToInt32(Console.ReadLine()));
reserva.CadastrarSuite(suite);
reserva.CadastrarHospedes(hospedes);


Console.WriteLine($"Hóspedes: {reserva.ObterQuantidadeHospedes()}");
Console.WriteLine($"Valor diária: {reserva.CalcularValorDiaria()}");