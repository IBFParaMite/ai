using System;
using System.Collections.Generic;
using System.Text;
using AI.Data;

namespace AI.Functions
{
    public class GenericFunctions
    {
        public string UserInput(User user)
        {
            if (user.Name != null) Console.Write($"{user.Name}: ");
            else Console.Write("User: ");

            string userInput = Console.ReadLine();

            return userInput;
        }
    }
}
