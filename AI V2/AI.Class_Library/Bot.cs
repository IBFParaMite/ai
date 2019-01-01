using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AI.Class_Library
{
    public class Bot
    {
        public string BotName { get; set; }

        public string[] BotRelationships = new string[]
        {
            "Married",
            "Dating",
            "Friends",
            "Colleagues",
            "Associates",
            "Enemies"
        };
    }
}
