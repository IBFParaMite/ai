using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AI.Class_Library
{
    public class Bot_Functions
    {
        private readonly Random random;

        public Bot_Functions()
        {
            random = new Random();
        }

        public string[] VIPBotNames = new string[]
        {
            "Hank",
            "Roberto",
            "Terrence"
        };

        public string[] NormalBotNames = new string[]
        {
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

        public Bot AssignBot(Bot bot, bool VIPStatus)
        {
            if (VIPStatus)
            {
                int responseCount = random.Next(VIPBotNames.Length);
                bot.Name = VIPBotNames[responseCount];

                return bot;
            }
            else
            {
                int responseCount = random.Next(NormalBotNames.Length);
                bot.Name = NormalBotNames[responseCount];

                return bot;
            }
        }

        public void Chat(User user)
        {
            Console.WriteLine("Hello there, {0}, how are you feeling today?", user.Name);
        }
    }
}
