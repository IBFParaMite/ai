using System;
using AI.Class_Library;

namespace AI.Core
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "AI.V2";
            User user = new User();
            Bot bot = new Bot();
            Bot_Functions functions = new Bot_Functions();

            Console.WriteLine("Hello there! \nWhat is your name?");

            user.Name = Console.ReadLine();

            if (functions.CheckVIPStatus(user.Name))
            {
                Console.WriteLine("{0} is in the VIP list", user.Name);
                functions.AssignVIPBot(bot);
            }
            else
            {
                Console.WriteLine("{0} is not in the VIP list", user.Name);
                functions.AssignNormalBot(bot);
            }

            Console.WriteLine(bot.BotName);

            functions.Chat(user);

            Console.ReadLine();
        }
    }
}
