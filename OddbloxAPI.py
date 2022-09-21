import discord
from discord.ext import commands
import urllib.request
import json

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    def Index(self, index):
        self.index = index

    @discord.ui.button(label="Download Menu", style=discord.ButtonStyle.green)
    async def blurple_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        interaction.style = discord.ButtonStyle.green
        interaction.disabled = True
        view = Buttons2()
        view.add_item(discord.ui.Button(label="Download PNG", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/png/"+self.index))
        view.add_item(discord.ui.Button(label="Download SVG", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/image/"+self.index))
        view.add_item(discord.ui.Button(label="Download Circular", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/circular/"+self.index))
        view.add_item(discord.ui.Button(label="Download Metadata", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/" + self.index))
        # await button.response.send_message(view=view,ephemeral=True)
        await button.response.edit_message(view=view)



# await button.response.edit_message(content=f"This is an edited button response!",view=self)
class Buttons2(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    def Index(self, index):
        self.index = index
    @discord.ui.button(label="Back", style=discord.ButtonStyle.red)
    async def blurple_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        interaction.style = discord.ButtonStyle.green
        view = Buttons()
        await button.response.edit_message(embed=None,view=view)
    @discord.ui.button(label="Attributes", style=discord.ButtonStyle.gray)
    async def blurple_button2(self, button2: discord.ui.Button, interaction: discord.Interaction):
        interaction.style = discord.ButtonStyle.green

    # await button.response.send_message(view=view,ephemeral=True)
        view = Buttons3()
        url = "https://api.oddblox.io/api/"+self.index
        uf = urllib.request.urlopen(url)
        html = uf.read()
        x = json.loads(html)
        y = x["description"]
        embed = discord.Embed(title="Oddblox #"+self.index + " Attributes", url="https://api.oddblox.io/api/png/"+self.index,color=0xFF5733)
        #embed.add_field(name='\u200b', value='Attributes', inline=True)
        print(x["attributes"][0])
        embed.add_field(name="ColorWave", value=x["attributes"][0]["value"], inline=True)
        embed.add_field(name="Foundation", value=x["attributes"][1]["value"], inline=True)
        embed.add_field(name="Unification", value=x["attributes"][2]["value"], inline=False)
        embed.add_field(name="EquidistantForm", value=x["attributes"][3]["value"], inline=True)
        embed.add_field(name="Interruption", value=x["attributes"][4]["value"], inline=True)
        embed.add_field(name="Focal", value=x["attributes"][5]["value"], inline=False)
        embed.add_field(name="Offset", value=x["attributes"][6]["value"], inline=True)
        embed.add_field(name="Expression", value=x["attributes"][7]["value"], inline=True)
        await button2.response.edit_message(embed=embed,view=view)
    # interaction.style=discord.ButtonStyle.green
    # await button.response.send_message(view=view,ephemeral=True)

class Buttons3(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
    def Index(self, index):
        self.index = index
    @discord.ui.button(label="Back", style=discord.ButtonStyle.red)
    async def blurple_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        interaction.style = discord.ButtonStyle.green
        view = Buttons2()
        view.add_item(discord.ui.Button(label="Download PNG", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/png/"+self.index))
        view.add_item(discord.ui.Button(label="Download SVG", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/image/"+self.index))
        view.add_item(discord.ui.Button(label="Download Circular", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/circular/"+self.index))
        view.add_item(discord.ui.Button(label="Download Metadata", style=discord.ButtonStyle.link,
                                        url="https://api.oddblox.io/api/" + self.index))
        await button.response.edit_message(embed=None,view=view)
    # await button.response.send_message(view=view,ephemeral=True)




@client.command()
async def oddblox(ctx, INDEX):
    url = "https://api.oddblox.io/api/" + INDEX
    uf = urllib.request.urlopen(url)
    html = uf.read()
    x = json.loads(html)
    y = x["description"]
    embed = discord.Embed(title="Oddblox #" + INDEX, url=url, description=y, color=0xFF5733)
    embed.set_thumbnail(url="https://api.oddblox.io/api/png/" + INDEX)
    await ctx.message.delete()
    await ctx.send(embed=embed)
    Buttons.index = Buttons2.index = Buttons3.index = INDEX
    view = Buttons()
    await ctx.send("", view=view)


@client.command()
async def button(ctx):
    view = Buttons()
    view.add_item(discord.ui.Button(label="Download PNG", style=discord.ButtonStyle.link,
                                    url="https://api.oddblox.io/api/png/192"))
    await ctx.send("ther", view=view)


client.run("MTAyMTIxMzczNTYxMzkwMjg0OA.GvMaHT.cMB-AW3c34leypSqlaadanIow2tMWS8zer4E6A")