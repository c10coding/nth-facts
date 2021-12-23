from fact.fact import Fact

class WordCount(Fact):

    def __init__(self, client):
        self.client = client
        self.fact_name = 'wordcount'

    async def display_fact(self, ctx, fact_args):
        for channel_name in fact_args:
            channel = self.client.get_channel(channel_name)
            if channel == None:
                continue
            await ctx.send(channel.position)

        await ctx.send('Testing')