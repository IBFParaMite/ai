using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp
{
    public class Bot
    {
        [Required]
        [StringLength(50)]
        public string BotName { get; set; }
        public int BotAge { get; set; }
        [StringLength(50)]
        public string BotRelationship { get; set; }

        internal static string RandomName()
        {
            string[] BotNames = new string[] {
                "Hank",
                "Roberto",
                "Sylvia",
                "Bob",
                "George",
                "Jacob",
                "Charlie",
                "Barry",
                "Tony",
                "Alex",
                "Jessica",
                "Jason",
                "Kat",
                "Andrey",
                "Beck",
                "Melissa",
                "Lucas",
                "Mario",
                "Jane",
                "James",
                "Gerard"
            };

            Random rand = new Random();
            int namesCount = rand.Next(BotNames.Length);
            var newBotName = BotNames[namesCount];
            return newBotName;
        }
    }
}
