using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AI.Class_Library
{
    public class Relationships
    {
        private readonly Random random;

        private readonly List<string> positiveresponses = new List<string>()
        {
            "Of course I will!",
            "Are you kidding me? Yes!",
            "I've been waiting for you to ask me for a long time! Yes!",
            ""
        };

        private readonly List<string> negativeresponses = new List<string>()
        {
            "I don't know if I feel the same way",
            "We don't really know each other...",
            "I don't think so",
        };

        public Relationships()
        {
            random = new Random();
        }

        public void AskOut()
        {
            string reponse = Response();
        }

        public string Response()
        {
            int responseCount = random.Next(positiveresponses.Count());
            string botresponse = positiveresponses[responseCount];

            return botresponse;
        }

        public string Date()
        {
            return string.Empty;
        }
    }
}
