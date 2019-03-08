using System;
using System.Collections.Generic;
using System.Text;

namespace AI.Data
{
    public class Bot
    {
        public string Name { get; set; }
        public BotRelationship BotRelationship { get; set; }
    }

    public class User
    {
        public string Name { get; set; }
        public string Gender { get; set; }
        public bool IsVIP { get; set; }
        public virtual Bot Bot { get; set; }
    }
}
