using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace Csharpier.models
{
    public class Vendajs
    {
        public int Id { get; set; }
        [JsonProperty("Nome_Produto")]
        public string Produto { get; set; }
        public decimal Preco { get; set; }
        public decimal? desconto { get; set; }
        public DateTime Datavenda { get; set; }
    }
}