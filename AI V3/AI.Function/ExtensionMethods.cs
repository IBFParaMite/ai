using AI.Data;
using System;
using System.Collections.Generic;
using System.Text;

namespace AI.Functions
{
    public static class ExtensionMethods
    {
        public static bool NameContains(this User user, string searchString)
        {
            return user.Name.ToLower().Contains(searchString.ToLower());
        }

        public static bool ContainsLower(this string s, string searchString)
        {
            return s.ToLower().Contains(searchString.ToLower());
        }

        public static string Botify(this string s, User user, bool firstLine = false)
        {
            StringBuilder botifiedString = new StringBuilder();

            if (!firstLine) botifiedString.Append("\n");

            if (user.Bot != null) botifiedString.Append($"{user.Bot.Name}: {s}");
            else botifiedString.Append($"System: {s}");

            return botifiedString.ToString();
        }

        public static void CheckVIP(this User user)
        {
            BotData data = new BotData();
            user.IsVIP = data.VIPUsers.Contains(user.Name);
        }

        public static void AssignBotRelationship(this Bot bot, User user)
        {
            if (user.IsVIP)
            {
                if (user.NameContains("jonas")) bot.BotRelationship = BotRelationship.Enemies;
                else if (user.NameContains("ancient") || user.NameContains("cameron")) bot.BotRelationship = BotRelationship.Friends;
            }
            else
            {
                bot.BotRelationship = BotRelationship.Colleagues;
            }
        }

        public static void AssignBot(this User user)
        {
            BotData data = new BotData();

            Random random = new Random();

            Bot bot = new Bot();

            if (user.IsVIP)
            {
                if (user.NameContains("cameron")) bot.Name = data.VIPBotNames[0];
                else if (user.NameContains("ancient")) bot.Name = data.VIPBotNames[1];
                else if (user.NameContains("jonas")) bot.Name = data.VIPBotNames[2];
            }
            else bot.Name = data.NormalBotNames[random.Next(data.NormalBotNames.Count)];

            bot.AssignBotRelationship(user);

            user.Bot = bot;
        }
    }
}
