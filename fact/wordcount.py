from fact.fact import Fact

class WordCount(Fact):

    def __init__(self):
        self.fact_name = 'wordcount'

    async def display_fact(self, ctx):
        await ctx.send('Testing')
