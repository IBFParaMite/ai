using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AI.StoryTimeAPI.Models
{
    public class StoryItem
    {
        public long Id { get; set; }
        public string Name { get; set; }
        public string Story { get; set; }
        public bool IsComplete { get; set; }
    }
}
