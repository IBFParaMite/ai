using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AI.StoryTimeAPI.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace AI.StoryTimeAPI.Controllers
{
    [Route("api/story")]
    [ApiController]
    public class StoryController : Controller
    {
        private readonly StoryContext _context;

        public StoryController(StoryContext context)
        {
            _context = context;

            if (_context.StoryItems.Count() == 0)
            {
                _context.StoryItems.Add(new StoryItem { Name = "abc" });
                _context.SaveChanges();
            }
        }

        // GET: api/Story
        [HttpGet]
        public async Task<ActionResult<IEnumerable<StoryItem>>> GetStoryItems()
        {
            return await _context.StoryItems.ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<StoryItem>> GetStoryItem(long id)
        {
            var storyItem = await _context.StoryItems.FindAsync(id);

            if (storyItem == null) return NotFound();

            return storyItem;
        }
    }
}
