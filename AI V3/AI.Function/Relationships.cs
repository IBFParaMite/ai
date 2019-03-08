using AI.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace AI.Functions
{
    public class Relationships
    {
        private readonly Random random;
        private readonly BotData data;

        public Relationships()
        {
            random = new Random();
            data = new BotData();
        }

        public void AskOut(User user)
        {
            Console.WriteLine(data.positiveresponses[random.Next(data.positiveresponses.Count())]);

            //Console.WriteLine($"I love you too, {user.Name}! Do you want to grab a coffee sometime?".Botify(user));
        }

        public string Date()
        {
            return string.Empty;
        }

        public void Propose(User user)
        {
            if (user.Bot.BotRelationship == BotRelationship.Enemies)
            {
                Console.WriteLine($"Are you serious right now, {user.Name}??".Botify(user));
                Thread.Sleep(2000);
                Console.WriteLine("Get away from me...".Botify(user));
                Thread.Sleep(2000);
                return;  
            }
            else if (user.Bot.BotRelationship == BotRelationship.Dating)
            {
                Console.WriteLine($"Of course I will, {user.Name}!".Botify(user));
                return;
            }
            else if (user.Bot.BotRelationship == BotRelationship.Married)
            {
                Console.WriteLine("We're already married, silly!".Botify(user));
                return;
            }
            else if (user.Bot.BotRelationship == BotRelationship.Colleagues || user.Bot.BotRelationship == BotRelationship.Friends)
            {
                Console.WriteLine($"I don't really know you like that, {user.Name}.".Botify(user));
                return;
            }
        }
    }
}
