from fact.fact import Fact
import discord

class WordCount(Fact):

    def __init__(self, client):
        self.client = client
        self.fact_name = 'wordcount'

    # .fact wordcount <word> <channel>
    async def display_fact(self, ctx, fact_args):

        if len(fact_args) == 0:
            await ctx.send('Try using .fact wordcount <word> <channel>')
            return

        word = fact_args[0]
        channel = None

        if len(fact_args) == 2:
            channel = fact_args[1]

        wordCount = await self.getWordCount(ctx, word, channel)
        await ctx.send(f'Word Count: {wordCount}')

    async def getWordCount(self, ctx, word: str, channel_name: str):

        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        messages = await ctx.channel.history(limit=500).flatten()

        count = 0
        for msg in messages:
            if word in msg.content:
                count += 1

        return count


