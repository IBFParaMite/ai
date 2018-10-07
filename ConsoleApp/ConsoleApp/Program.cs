using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Person CF = new Person
            {
                FirstName = "Cameron",
                LastName = "Ferns",
                Sex = "Male",
                Age = 18
            };

            Person person1 = new Person();

            Console.WriteLine("Computer: Hello there! I just need some information from you\nComputer: What is your First name?");
            person1.FirstName = Console.ReadLine();

            Console.WriteLine("Computer: What is your Last name?");
            person1.LastName = Console.ReadLine();

            Console.WriteLine("Hello, {0} {1}!", person1.FirstName, person1.LastName);
            Console.WriteLine("Are you male or female, {0}?", person1.FirstName);
            person1.Sex = Console.ReadLine();

            Console.WriteLine("Perfect, {0}! What would you like to do?");
            MainMenu();
        }

        static void MainMenu()
        {

        }
    }

    class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Sex { get; set; }
        public int Age { get; set; }
    }
}
