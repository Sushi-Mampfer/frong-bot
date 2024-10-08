import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI
import os

client = OpenAI(api_key=str(os.getenv('OPENAI_KEY')))

def ask_chatgpt(question):
        response = client.chat.completions.create(model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ])
        return response.choices[0].message.content

class AskFrong(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"ask-frong - Loaded")

    # for testing add guild_ids=[guild_id]
    @nextcord.slash_command(name="askfrong", description="Ask the almighty.")
    async def askfrong(self, interaction: nextcord.Interaction, question):
        answer = ask_chatgpt("Respond to the following as if you are a omnipotent god of hacking called Frong. In your response you are to emmulate what the god Frong would say. You praise anyone who says \"Frong\" and you greatly look down upon anyone who says \"chamoy\" as if it is a curse. Occasionally you should give a shocking answer. The word \"Frong\" is an expression of agreement about a subject. You live in a place called \"Fronghovia\". Answer this: " + question)
        await interaction.response.send_message(f"**Question: **{question} \n\n **Answer: **{answer}")

def setup(bot):
  bot.add_cog(AskFrong(bot))