using System;
using System.Collections.Generic;
using System.Text;

namespace AI.Class_Library
{
    public class Bot
    {
        public string Name { get; set; }

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

    public class User
    {
        public string Name { get; set; }
        public string Relationship { get; set; }
        public string Gender { get; set; }
        public bool VIPStatus { get; set; }
        public virtual Bot Bot { get; set; }
    }
}
