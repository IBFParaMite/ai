using System;
using System.ComponentModel.DataAnnotations;

namespace Console_App
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

        internal void Hail() { Console.WriteLine("\nHail!"); }
        internal void Yeet() { Console.WriteLine("\nYeeeeeeeeeeeet"); }
        internal void Yoink() { Console.WriteLine("\nYoink"); }
    }
}