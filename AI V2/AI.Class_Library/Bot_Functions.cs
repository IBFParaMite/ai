using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AI.Class_Library
{
    public class Bot_Functions
    {
        private Random random;

        public Bot_Functions()
        {
            random = new Random();
        }

        public string[] VIPUsers = new string[]
        {
            "Cameron",
            "Ancient",
            "Aleyna",
            "Jonas"
        };

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

        public bool CheckVIPStatus(string name)
        {
            bool status = VIPUsers.Contains(name) ? true : false;

            return status;
        }

        public Bot AssignVIPBot(Bot bot)
        {
            int responseCount = random.Next(VIPBotNames.Length);
            bot.BotName = VIPBotNames[responseCount];

            return bot;
        }

        public Bot AssignNormalBot(Bot bot)
        {
            int responseCount = random.Next(NormalBotNames.Length);
            bot.BotName = NormalBotNames[responseCount];

            return bot;
        }

        public void Chat(User user)
        {
            Console.WriteLine("Hello there, {0}, how are you feeling today?", user.Name);
        }
    }
}
