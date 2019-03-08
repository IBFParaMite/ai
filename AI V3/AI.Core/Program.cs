using System;
using System.Threading.Tasks;
using AI.Data;
using AI.Functions;

namespace AI.Core
{
    public class Program
    {
        private User user;
        private readonly BotFunctions functions;
        private readonly GenericFunctions generic;

        public Program()
        {
            user = new User();
            functions = new BotFunctions();
            generic = new GenericFunctions();
        }

        public static void Main(string[] args)
        {
            Console.Title = "AI.V5";
            Program program = new Program();

            program.MainAsync().Wait();

            Console.ReadLine();
        }

        public async Task MainAsync()
        {
            Console.WriteLine("Hello there!".Botify(user, firstLine: true));
            Console.WriteLine("What is your name?".Botify(user));

            user.Name = generic.UserInput(user);
            user.CheckVIP();
            user.AssignBot();

            Console.WriteLine($"You are {user.Bot.BotRelationship} to me".Botify(user));

            await functions.Chat(user);
        }
    }
}
