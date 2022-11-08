import discord
from discord import Interaction
from discord.ext import commands
import urllib.request
import json
import os
import asyncio
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
        #view = DropdownView()
        view = Buttons2()
        #await button.response.edit_message(view=view)

        await button.response.edit_message(view=DropdownView())
        # await button.response.send_message(view=view,ephemeral=True)



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
    Dropdown.index=  Buttons.index = Buttons2.index = Buttons3.index = INDEX
    view = Buttons()
    await ctx.send("", view=view)

"""class Dropdown(discord.ui.Select):
    def __init__(self, *, timeout=180):
        selecoptions = [
            discord.SelectOption(label="Download PNG",description=""),
            discord.SelectOption(label="Download SVG",description=""),
            discord.SelectOption(label="Download Circular",description=""),
            discord.SelectOption(label="Download Metadata",description="")
        ]
        super().__init__(placeholder="Download Links",min_values=1,max_values=1,options=selecoptions)

        async def callback(self, interaction: discord.Interaction):
            if(self.values[0]=="Download PNG"):
                await interaction.response.send_message("Thank you")
            else:
                await interaction.response.send_message("Thank you2")
class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())"""
class Dropdown(discord.ui.Select):
    def Index(self, index):
        self.index = index
    def __init__(self):
        options = [
            discord.SelectOption(label="Download PNG",description=""),
            discord.SelectOption(label="Download SVG",description=""),
            discord.SelectOption(label="Download Circular",description=""),
            discord.SelectOption(label="Download Metadata",description=""),
            discord.SelectOption(label="Metadata Information",description=""),
            discord.SelectOption(label="Custom Download",description="")
        ]

        super().__init__(placeholder='Download image...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        if(self.values[0]=="Download PNG"):
            embed = discord.Embed(title="PNG DOWNLOAD",url="https://api.oddblox.io/api/png/"+self.index)
            await interaction.response.edit_message(embed=embed)
        elif(self.values[0]=="Download SVG"):
            embed = discord.Embed(title="SVG DOWNLOAD:",url="https://api.oddblox.io/api/svg/"+self.index)
            await interaction.response.edit_message(embed=embed)
        elif(self.values[0]=="Download Circular"):
            embed = discord.Embed(title="CIRCULAR DOWNLOAD:",url="https://api.oddblox.io/api/circular/"+self.index)
            await interaction.response.edit_message(embed=embed)
        else:
            embed = discord.Embed(title="TESTING ERROR - 404",url="https://api.oddblox.io/api/circular/"+self.index)
            await interaction.response.edit_message(embed=embed)


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())
@client.command()
async def button(ctx):
    view = Buttons()
    view.add_item(discord.ui.Button(label="Download PNG", style=discord.ButtonStyle.link,
                                    url="https://api.oddblox.io/api/png/192"))
    await ctx.send("ther", view=view)
@client.command()
async def dropdowntest(ctx):
    view = DropdownView()
    await ctx.send("", view=view)


client.run(os.environ['SECRET'])
