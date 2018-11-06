using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Console_App.Bot_Functions
{
    public class RandomJoke
    {
        public static string Joke()
        {
            string[] jokes = new string[] {
                "why does a golfer have 2 pairs of pants? In case they get a hole in one",
                "What did the snowman ask the other snowman? Do you smell carrot?",
                "What did the janitor say when he jumped out of the closet? Supplies!",
                "What did Kim Jong Un said when his father died? His Korea is over.",
                "My grandad has the heart of a lion and a life ban from the zoo",
                "Why are ghost banned from the liquor stores? They would steal all the boos",
            };

            Random random = new Random();
            int jokeCount = random.Next(jokes.Length);
            var randomJoke = jokes[jokeCount];

            return randomJoke;
        }
    }
}
