using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AI.Class_Library
{
    public class AskOut
    {
        public void Response()
        {
            string[] positiveresponses = new string[]
            {
                "Of course I will!",
                "Are you kidding me? Yes!",
                "I've been waiting for you to ask me for a long time! Yes!",
                ""
            };

            string[] negativeresponses = new string[]
            {
                "I don't know if I feel the same way",
                "We don't really know each other!",
                "I don't think so",
            };

            Random rand = new Random();
            int responseCount = rand.Next(positiveresponses.Length);
            string botresponse = positiveresponses[responseCount];

            Console.WriteLine(botresponse);
        }
    }

    public class Date
    {
        public void DateScenarios()
        {

        }
    }
}
