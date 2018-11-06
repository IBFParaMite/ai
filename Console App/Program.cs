using Console_App.Bot_Functions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Console_App
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "AI";

            Console.WriteLine("Computer: Hello there! I just need some information from you\nComputer: What is your First name?");
            string name = Console.ReadLine();

            if (name.ToLower().Equals("ancient"))
            {
                Bot bot = new Bot
                {
                    BotName = "Roberto",
                    BotRelationship = "Married",
                };

                Person person = new Person
                {
                    FirstName = "Ancient",
                    Age = 17,
                    Sex = true,
                    Gender = "Apache / Banana"
                };

                person.Hail();

                MainMenu(person, bot);
            }
            else
            {
                Person person = new Person
                {
                    FirstName = name,
                };

                Bot bot = new Bot
                {
                    BotName = Bot.RandomName(),
                    BotRelationship = "Friends",
                };

                person.Yeet();

                Console.WriteLine("Computer: What is your Last name, {0}?", person.FirstName);
                person.LastName = Console.ReadLine();

                string personFullName = person.FirstName + " " + person.LastName;

                Console.WriteLine("Hello, {0}!", personFullName);

                MainMenu(person, bot);
            }
        }

        public static void MainMenu(Person person, Bot bot)
        {
            Console.WriteLine("\nHello, {0}! What would you like to do?", person.FirstName);
            Console.WriteLine("Option A | Greet \nOption B | Change user \nOption C | Chat \nOption D | Trivia \nOption E | Story \nOption F | Relationship status \nOption G| Jokes \nOption X | Exit Program");

            bool valid = false;

            while (valid == false)
            {
                Console.WriteLine("\nPlease select an option:");
                string option = Console.ReadLine().ToLower();

                if (option == "a") { valid = true; Greet(person, bot); }
                else if (option == "b") { valid = true; ChangeUser(person); }
                else if (option == "c") { valid = true; Chat(person); }
                else if (option == "d") { valid = true; Trivia(person); }
                else if (option == "e") { valid = true; Story(person); }
                else if (option == "f") { valid = true; RelationshipStatus(person, bot); }
                else if (option == "g") { valid = true; Jokes(person, bot); }
                else if (option == "h") { valid = true; Flirting(person); }
                else if (option == "i") { valid = true; ClearMemory(person); }
                else if (option == "x") { valid = true; Environment.Exit(0); }
                else { valid = false; Console.WriteLine("System: Error, please try again"); }
            }
        }

        private static void EndSubProgram(string emotion, Person person, Bot bot)
        {
            if (emotion == "sad") { Console.WriteLine("\n(T_T)"); }
            else if (emotion == "happy") { Console.WriteLine("\n( ^w^)"); }
            else if (emotion == "neutral") { Console.WriteLine("\n(o-o)"); }

            Console.WriteLine("Would you like to return to the main menu, {0}? (yes/no)", person.FirstName);
            string response = Console.ReadLine().ToLower();

            if (response == "yes" || response == "y") { MainMenu(person, bot); }
            else if (response == "no" || response == "n") { Environment.Exit(0); }
        }

        private static void ClearMemory(Person person)
        {
            throw new NotImplementedException();
        }

        private static void Flirting(Person person)
        {
            throw new NotImplementedException();
        }

        private static void Jokes(Person person, Bot bot)
        {

            Console.WriteLine("\n{0}", RandomJoke.Joke());
            EndSubProgram("happy", person, bot);
        }

        private static void RelationshipStatus(Person person, Bot bot)
        {
            Console.WriteLine("\nFinding the relationship status between you and the bot...");

            if (bot.BotRelationship != null)
            {
                Console.WriteLine("\nThe relationship between {0} and {1} is {2}", person.FirstName, bot.BotName, bot.BotRelationship);
                EndSubProgram("neutral", person, bot);
            }
            else { throw new NullReferenceException(); }
        }

        private static void Story(Person person)
        {
            throw new NotImplementedException();
        }

        private static void Trivia(Person person)
        {
            throw new NotImplementedException();
        }

        private static void Chat(Person person)
        {
            throw new NotImplementedException();
        }

        private static void ChangeUser(Person person)
        {
            throw new NotImplementedException();
        }

        private static void Greet(Person person, Bot bot)
        {
            EndSubProgram("happy", person, bot);
        }

        public static void BotFight(Person person, Bot bot)
        {
            if (person.FirstName == "Ancient")
            {
                throw new NotImplementedException();
            }
        }
    }
}
