using System;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp
{
    public class Person
    {
        [Required]
        [StringLength(50)]
        public string FirstName { get; set; }
        [StringLength(50)]
        public string LastName { get; set; }
        public int Age { get; set; }
        public bool Sex { get; set; }
        [StringLength(50)]
        public string Gender { get; set; }

        internal void Hail()
        {
            Console.WriteLine("\nHail!");
        }
    }
}
