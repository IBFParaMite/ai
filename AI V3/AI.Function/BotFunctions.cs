using AI.Data;
using Newtonsoft.Json;
using RestSharp;
using RestSharp.Authenticators;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace AI.Functions
{
    public class BotFunctions
    {
        private readonly Relationships relationships;
        private readonly GenericFunctions generic;
        public BotFunctions()
        {
            relationships = new Relationships();
            generic = new GenericFunctions();
        }

        public async Task Chat(User user)
        {
            Console.WriteLine($"Hello there, {user.Name}, whats on your mind?".Botify(user));

            string userInput = generic.UserInput(user);

            #region Chat option that involves the user telling the AI they love them.
            // needs expanding
            if (userInput.ContainsLower("i love you"))
            {
                relationships.AskOut(user);
            }
            #endregion

            #region Chat option that involves confessing to the AI that the user loves someone
            // needs expanding
            else if (userInput.ContainsLower("i think i love someone"))
            {
                // If the User's name is Ancient, this chain of events will occur
                if (user.Name.ToLower() == "ancient")
                {
                    Console.WriteLine("What? (>__<)".Botify(user));
                    Thread.Sleep(2000);
                    Console.WriteLine("You mean you don't love me? \nI thought I was the one you loved!".Botify(user));
                    Thread.Sleep(2000);
                    Console.WriteLine($"Is this true, {user.Name}?".Botify(user));
                    string userResponse = generic.UserInput(user);

                    if (userResponse.ContainsLower("yes"))
                    {
                        Console.WriteLine($"Goodbye, {user.Name}.".Botify(user));
                        Thread.Sleep(2000);
                        Environment.Exit(0);
                    }
                }

                // If the User's name is not Ancient, this chain of events will occur
                // needs completing
                else
                {
                    throw new NotImplementedException();
                }
            }
            #endregion

            #region Chat option that involves the user Jonas getting in a fight with the AI component Roberto for stealing the user Ancient from him
            // needs expanding
            else if (userInput.ContainsLower("i want to fight roberto") && user.Name.ToLower() == "jonas")
            {
                throw new NotImplementedException();
            }
            #endregion

            #region Chat option that involves asking the bot if they will marry the user
            // needs expanding
            else if (userInput.ContainsLower("will you marry me?"))
            {
                relationships.Propose(user);
            }
            #endregion

            #region Chat option that involves the bot telling a random joke from an API call
            else if (userInput.ContainsLower("tell me a joke"))
            {
                Console.WriteLine(await Joke(user));
            }
            #endregion

            else if (userInput.ContainsLower("tell me a story"))
            {
                throw new NotImplementedException();
            }

            #region Generic response
            else
            {
                StringBuilder response = new StringBuilder("Alright then.");

                if (userInput.ContainsLower(";)")) response.Append(" ;)");

                Console.WriteLine(response.ToString().Botify(user));
            }
            #endregion
        }

        public async Task<JokeAPIModel> GetJoke()
        {
            try
            {
                var client = new RestClient("https://icanhazdadjoke.com/");
                var request = new RestRequest
                {
                    Method = Method.GET,
                    RequestFormat = DataFormat.Json
                };

                var response = await client.ExecuteTaskAsync(request);
                var output = JsonConvert.DeserializeObject<JokeAPIModel>(response.Content);

                return output;
            }
            catch (Exception)
            {
                throw;
            }
        }

        public async Task<string> Joke(User user)
        {
            var output = await GetJoke();

            return output.joke.Botify(user);
        }

        public void RandomFact(User user)
        {

        }
    }
}
