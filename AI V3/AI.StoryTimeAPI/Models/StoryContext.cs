using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AI.StoryTimeAPI.Models
{
    public class StoryContext : DbContext
    {
        public StoryContext(DbContextOptions<StoryContext> options)
            :base(options)
        {               
        }

        public DbSet<StoryItem> StoryItems { get; set; }
    }
}
