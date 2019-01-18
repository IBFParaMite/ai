using System;
using AI.Class_Library;

namespace AI.Core
{
    class Program
    {
        private Bot bot;
        private User user;
        private Bot_Functions functions; 

        public Program()
        {
            bot = new Bot();
            
            functions = new Bot_Functions();
        }

        public void BotInitialize()
        {
            Console.WriteLine("Hello there! \nWhat is your name?");
            user = new User
            {
                Name = Console.ReadLine(),
                Bot = functions.AssignBot(bot, user.VIPStatus)
            };

            functions.Chat(user);
        }

        static void Main(string[] args)
        {
            Console.Title = "AI.V2";
            Program program = new Program();

            program.BotInitialize();
            
            Console.ReadLine();
        }
    }
}
