class Fact:

    client = None
    fact_name = ""

    def __init__(self, client, fact_name):
        self.client = client
        self.fact_name = fact_name

    async def display_fact(self, ctx, fact_args):
        await ctx.send('This fact has not set up yet!')

    def __str__(self):
        return self.fact_name
