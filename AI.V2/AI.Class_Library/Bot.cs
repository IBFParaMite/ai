using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AI.Class_Library
{
    class Bot
    {
        public string BotName { get; set; }

        public List<string> BotRelationships = new List<string>()
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
