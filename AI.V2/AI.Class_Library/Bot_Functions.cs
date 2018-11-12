using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AI.Class_Library
{
    public class EndSubProgram
    {

    }

    public class VIPStatus
    {
        public static bool Check(string name)
        {
            if (VIPUsers.Contains(name))
            {
                return true;
            }
            else
            {
                return false;
            }    
        }

        public static List<string> VIPUsers = new List<string>()
        {
            "Cameron",
            "Ancient",
            "Aleyna",
            "Jonas"
        };
    }

    public class AssignBotName
    {
        public static void AssignVIP()
        {
            Bot bot = new Bot
            {
                //BotName =
            };
            Random random = new Random();
        }

        public static void AssignNormal()
        {

        }

        public static List<string> VIPBotNames = new List<string>()
        {
            "Hank",
            "Roberto",
            "Terrence"
        };

        public static List<string> NormalBotNames = new List<string>()
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
    }
}
