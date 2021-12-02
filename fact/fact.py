class Fact:

    fact_name = ""

    def __init__(self, fact_name):
        self.fact_name = fact_name

    async def display_fact(self, ctx):
        await ctx.send('This fact has not set up yet!')
