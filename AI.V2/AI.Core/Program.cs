using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AI.Class_Library;

namespace AI.Core
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "AI.V2";

            Console.WriteLine("Hello there! \nWhat is your name?");
            string name = Console.ReadLine();

            if (VIPStatus.Check(name) == true)
            {
                Console.WriteLine("{0} is in the VIP list", name);
                AssignBotName.AssignVIP();
            }
            else
            {
                Console.WriteLine("{0} is not in the VIP list", name);
                AssignBotName.AssignNormal();
            }

            Console.ReadLine();
        }
    }
}
