import discord
import asyncio
from discord.ext import commands
import random
from random import choice
import urllib
import requests
import io
import aiohttp


client = commands.Bot(command_prefix = "/")
client.remove_command('help')


#playing
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=' /help'))
    

#8 ball game
@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is deadly.',
                 'Yes, definitely.',
                 'No.',
                 'No, you nonce.',
                 'No, you sick f****.',
                 'Yes, yes and yes.',
                 'Get a life.',
                 'Ask better questions, you moron.',
                 'YES',
                 'Obviously',
                 'The answer is YES',
                 'Ofcourse',
                 'I do not care.']
    embed = discord.Embed(title=f'❓ {question} ❓', description=f'Answer: {random.choice(responses)} ', colour=discord.Colour.blue())
    await ctx.send(embed=embed)


#joke
@client.command()
async def joke(ctx):
    urlil = f'https://official-joke-api.appspot.com/random_joke'
    async with aiohttp.ClientSession() as session:
        async with session.get(urlil) as r:
            if r.status == 200:
                js = await r.json()
                ml = js["setup"]
                pl = js["punchline"]
                embed = discord.Embed(title=' 😭 Joke 😭 ', description=f"{ml}\n{pl}", colour=discord.Colour.green())
                await ctx.send(embed=embed)


#meme
@client.command()
async def meme(ctx):
    urll = "https://meme-api.herokuapp.com/gimme"
    res = requests.get(urll)
    dataa = res.json()
    urlll = dataa['url']
    async with aiohttp.ClientSession() as session:
        async with session.get(urlll) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'cool_image.png'))


#D size
@client.command(aliases = ["pp size"])
async def ppsize(ctx, *, member: discord.Member = None):
    member = member or ctx.author
    responses = ['8=D',
                 '8===D',
                 '8=========D',
                 '8===============D',
                 'Error, no dick found.' ]
    await ctx.send(f"{member.mention}'s pp size is\n{random.choice(responses)}")


#insults
@client.command()
async def insult(ctx, *, member: discord.Member = None):
    member = member or ctx.author
    responsess = ['Don’t you get tired of putting make up on two faces every morning?',
                 'The smartest thing that ever came out of your mouth was a penis. ',
                 'It’s a shame you can’t Photoshop your personality.',
                 'Calm down. Take a deep breath and then hold it for about twenty minutes',
                 'You have more faces than Mount Rushmore.',
                 'You should wear a condom on your head. If you’re going to be a dick, you might as well dress like one. ',
                 'My middle finger gets a boner every time I see you.',
                 'Get a life sucker.',
                 'If I had a face like yours I’d sue my parents.',
                 'I’d smack you, but that would be animal abuse.',
                 'I keep thinking you can’t get any dumber and you keep proving me wrong.',
                 'I will explain and I will use small words so that you will be sure to understand, you warthog-faced buffoon.',
                 'Your mom told you that you could become anything. Yet you still chose to become a disappointment.',
                 'Even Bob Ross would call you a mistake.',
                 'I could give you a penny for your thoughts and would get change back.']
    await ctx.send(f'{member.mention}\n {random.choice(responsess)}')


#weather
@client.command()
async def weather(ctx, *, city):
    city = city
    urlil = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=f8e10f057f4c41611cc2075f28cd3f2d&units=metric'
    async with aiohttp.ClientSession() as session:
        async with session.get(urlil) as r:
            if r.status == 200:
                js = await r.json()
                tempp = js['main']['temp']
                desc = js['weather'][0]["description"]
                count = js['sys']['country']
                tmax = js['main']['temp_max']
                tmin = js['main']['temp_min']
                hum = js['main']['humidity']
                pres = js['wind']['speed']
                embed = discord.Embed(title=f'⛅ Weather details of {city} ⛅', description=f'Country: {count}', colour=discord.Colour.blue())
                embed.add_field(name='Temperature:', value=f'{tempp}° Celsius', inline=False)
                embed.add_field(name='Description:', value=f'{desc}', inline=True)
                embed.add_field(name='Max temp:', value=f'{tmax}° Celsius', inline=False)
                embed.add_field(name="Min temp:", value=f'{tmin}° Celsius', inline=True)
                embed.add_field(name="Humidity:", value=f'{hum}', inline=False)
                embed.add_field(name="Pressure:", value=f'{pres} Pa', inline=True)
                await ctx.send(embed=embed)


#quote
@client.command()
async def quote(ctx):
    responses = ['Live as if you were to die tomorrow. Learn as if you were to live forever. -Mahatma Gandhi.',
                 'That which does not kill us makes us stronger. -Friedrich Nietzsche.',
                 'Be who you are and say what you feel, because those who mind don’t matter and those who matter don’t mind. – Bernard M. Baruch',
                 'We must not allow other people’s limited perceptions to define us. – Virginia Satir.',
                 'Do what you can, with what you have, where you are. – Theodore Roosevelt.',
                 'Be yourself; everyone else is already taken. – Oscar Wilde.',
                 'This above all: to thine own self be true. – William Shakespeare.',
                 'If you cannot do great things, do small things in a great way. – Napoleon Hill.',
                 'Wise men speak because they have something to say; fools because they have to say something. -Plato.',
                 'I find that the harder I work, the more luck I seem to have. -Thomas Jefferson',
                 'The way to get started is to quit talking and begin doing. -Walt Disney',
                 'I never dreamed about success, I worked for it. -Estee Lauder',
                 'There are no secrets to success. It is the result of preparation, hard work, and learning from failure. -Colin Powell',
                 'It is better to fail in originality than to succeed in imitation. -Herman Melville',
                 'If you set your goals ridiculously high and it is a failure, you will fail above everyone elses success. -James Cameron',
                 'Don not be afraid to give up the good to go for the great. -John D. Rockefeller']
    embed = discord.Embed(title='✍️ Quote ✍️', description=f"{random.choice(responses)}", colour=discord.Colour.green())
    await ctx.send(embed=embed)


#darkjoke
@client.command()
async def djoke(ctx):
    responses = ['What is red and bad for your teeth? A brick.',
                 'I was going to tell a dead baby joke. But I decided to abort.',
                 'Why does Helen Keller hate porcupines? They are painful to look at.',
                 'Why can not orphans play baseball? They do not know where home is.',
                 'Give a man a match, and he will be warm for a few hours. Set a man on fire, and he will be warm for the rest of his life.',
                 'A blind woman tells her boyfriend that she is seeing someone. It is either really terrible news or really great news.',
                 'My grandfather says I am too reliant on technology. I called him a hypocrite and unplugged his life support.',
                 'I visited my friend at his new house. He told me to make myself at home. So I threw him out. I hate having visitors.',
                 'I wish the grass in my back lawn was emo. Then it would cut itself.',
                 'I don’t have a carbon footprint. I just drive everywhere.',
                 'You know you’re not liked when you get handed the camera every time they make a group photo',
                 'You’re not completely useless. You can always serve as a bad example.',
                 'What gift did the kid with no hands get for his birthday? No idea. He hasn not figured out how to open it yet.',
                 'What is the difference between me and cancer? My dad did not beat cancer.',
                 'It is important to have a good vocabulary. If I had known the difference between the words antidote and anecdote, one of my good friends would still be alive.',
                 'A man went into a library and asked for a book on how to commit suicide. The librarian said: “Fuck off, you won’t bring it back.”',
                 'Why did the chicken cross the road? To get to the other side…(suicide, for those that are slow)',
                 'Cats have nine lives. Makes them ideal for experimentation.',
                 'Today was a terrible day. My ex got hit by a bus. And I lost my job as a bus driver!']
    embed = discord.Embed(title='😈 Dark Joke 😈', description=f"{random.choice(responses)}", colour=discord.Colour.green())
    await ctx.send(embed=embed)


#help
@client.command()
async def help(ctx):
    embed = discord.Embed(title='🙌 Help commands 🙌', description='Always here to help!', colour=discord.Colour.blue())
    embed.add_field(name='/meme', value='Sends a meme.', inline=False)
    embed.add_field(name='/quote', value='Sends a quote.', inline=True)
    embed.add_field(name='/djoke', value='Sends a dark joke.', inline=False)
    embed.add_field(name="/weather 'city name'", value='Shows weather of that city.', inline=True)
    embed.add_field(name="/joke", value='Sends a lame joke mostly.', inline=False)
    embed.add_field(name="/8ball 'question'", value='Sends a random answer to your yes/no question.', inline=True)
    embed.add_field(name="/insult 'mention member'", value='Sends random insult.', inline=False)
    embed.add_field(name="/ppsize 'mention member'", value='Shows the ppsize of mentioned.', inline=True)
    embed.add_field(name="/info", value='Shows bot dev id and support server link', inline=False)
    embed.add_field(name="/cats", value="Shows random cat facts", inline=True)
    embed.add_field(name="/corona 'country name'", value="Shows entered country's corona stats.", inline=False)
    embed.add_field(name="/lovep 'person1' 'person2'", value="Try it yourself.", inline=True)
    embed.add_field(name="/meaning 'word'", value="Gives meaning of the word.", inline=False)
    #embed.add_field(name="/load greetings", value="Greets the new member in system channel. To stop greetings type '/unload greetings'", inline=False)
    embed.add_field(name="/urls 'url'", value="URL shortner", inline=False)
    embed.add_field(name="/ipl 'ip'", value="IP address look up.", inline=False)
    embed.add_field(name="/horoscope 'sign' 'day'-today/tomorrow/yesterday", value="Gives horoscope", inline=False)
    embed.add_field(name='/dadjoke', value='Sends a dad joke.', inline=True)
    embed.add_field(name="/love 'member mention'", value='Sends a love message.', inline=False)
    await ctx.send(embed=embed)

#info
@client.command()
async def info(ctx):
    await ctx.send("Developer - AnonymousKnull#1481 Help server- https://discord.gg/SbYgZkc")


#corona
@client.command()
async def corona(ctx, *, country):
    country = country
    urlil = f'https://covid-19-data.p.rapidapi.com/country'
    querystring = {"format":"json","name":"italy"}
    querystring["name"]=str(country)
    headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "91a9efd206msh739aa08c6bcd6aap1a64cejsnda168d255a13"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(urlil, headers=headers, params=querystring) as r:
            if r.status == 200:
                js = await r.json()
                country = js[0]["country"]
                conf = js[0]["confirmed"]
                recv = js[0]["recovered"]
                cric = js[0]["critical"]
                dea = js[0]["deaths"]
                embed = discord.Embed(title='Corona stats', description=f"Country: {country}", colour=discord.Colour.green())
                embed.add_field(name='Confirmed:', value=f'{conf} cases', inline=False)
                embed.add_field(name='Recovered:', value=f'{recv}', inline=True)
                embed.add_field(name='Critical:', value=f'{cric}', inline=False)
                embed.add_field(name="Deaths:", value=f'{dea}', inline=True)
                await ctx.send(embed=embed)


#cat facts
@client.command()
async def cats(ctx):
    urlil = f'https://brianiswu-cat-facts-v1.p.rapidapi.com/facts'
    headers = {
    'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com",
    'x-rapidapi-key': "91a9efd206msh739aa08c6bcd6aap1a64cejsnda168d255a13"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(urlil, headers=headers) as r:
            if r.status == 200:
                js = await r.json()
                rangee = range(231)
                woah = js["all"][random.choice(rangee)]["text"]
                embed = discord.Embed(title='🐱 Cat fact 🐱', description=f"{woah}", colour=discord.Colour.blue())
                await ctx.send(embed=embed)


#love
@client.command()
async def lovep(ctx, name, namee):
    urlil = f'https://love-calculator.p.rapidapi.com/getPercentage'
    querystring = {"fname":"John","sname":"Alice"}
    querystring["fname"] = str(name)
    querystring["sname"] = str(namee)
    headers = {
    'x-rapidapi-host': "love-calculator.p.rapidapi.com",
    'x-rapidapi-key': "91a9efd206msh739aa08c6bcd6aap1a64cejsnda168d255a13"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(urlil, headers=headers, params=querystring) as r:
            if r.status == 200:
                js = await r.json()
                na = js["fname"]
                nb = js["sname"]
                say = js["result"]
                perc = js["percentage"]
                embed = discord.Embed(title='❤️ Love is in the air? ❤️', description=f"Let us find out ;)", colour=discord.Colour.blue())
                embed.add_field(name='Person 1:', value=f'{na}', inline=False)
                embed.add_field(name='Person 2:', value=f'{nb}', inline=True)
                embed.add_field(name='Your result:', value=f'{say}', inline=False)
                embed.add_field(name="Chance of relationship being successful:", value=f'{perc}%', inline=True)
                await ctx.send(embed=embed)


#dictionary
@client.command()
async def meaning(ctx, word):
    urlil = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key=6d0d92af-f528-4b77-ae02-eacb9270c68c'
    async with aiohttp.ClientSession() as session:
        async with session.get(urlil) as r:
            if r.status == 200:
                js = await r.json()
                mean = js[0]["shortdef"][0]
                embed = discord.Embed(title=f'📚 Word: {word}', description=f"{mean}", colour=discord.Colour.purple())
                await ctx.send(embed=embed)


#url shortner
@client.command()
async def urls(ctx, *, urll):
    urlil = "https://url-shortener-service.p.rapidapi.com/shorten"
    urlll = str(urllib.parse.quote_plus(urll))
    payload = f"url={urlll}"
    headers = {
    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
    'x-rapidapi-key': "91a9efd206msh739aa08c6bcd6aap1a64cejsnda168d255a13",
    'content-type': "application/x-www-form-urlencoded"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(urlil, data=payload, headers=headers) as r:
            if r.status == 200:
                js = await r.json()
                vlink = js["result_url"]
                await ctx.send(f"Shortened url: {vlink}")


#ip lookup
@client.command()
async def ipl(ctx, *, ip):
    url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
    querystring = {"ip":"12"}
    querystring["ip"]=str(ip)
    headers = {
    'x-rapidapi-host': "ip-geolocation-ipwhois-io.p.rapidapi.com",
    'x-rapidapi-key': "91a9efd206msh739aa08c6bcd6aap1a64cejsnda168d255a13"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=querystring) as r:
            if r.status == 200:
                js = await r.json()
                ipp = js["ip"]
                count = js["country"]
                reg = js["region"]
                cit = js["city"]
                isi = js["isp"]
                embed = discord.Embed(title='IP details', description=f"IP = {ipp}", colour=discord.Colour.blue())
                embed.add_field(name='Country:', value=f'{count}', inline=False)
                embed.add_field(name='City:', value=f'{cit}', inline=True)
                embed.add_field(name='Region:', value=f'{reg}', inline=False)
                embed.add_field(name="ISP:", value=f'{isi}', inline=True)
                await ctx.send(embed=embed)


#horoscope
@client.command()
async def horoscope(ctx, signn, dayy):
    url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"
    querystring = {"sign":"aries","day":"today"}
    querystring["sign"]=str(signn)
    querystring["day"]=str(dayy)
    payload = ""
    headers = {
    'x-rapidapi-host': "sameer-kumar-aztro-v1.p.rapidapi.com",
    'x-rapidapi-key': "91a9efd206msh739aa08c6bcd6aap1a64cejsnda168d255a13",
    'content-type': "application/x-www-form-urlencoded"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers, params=querystring) as r:
            if r.status == 200:
                js = await r.json()
                dattt = js["current_date"]
                desc = js["description"]
                comp = js["compatibility"]
                mod = js["mood"]
                col = js["color"]
                lucn = js["lucky_number"]
                luct = js["lucky_time"]
                embed = discord.Embed(title='♎️ Horoscope ♌️', description=f"Sign = {signn}", colour=discord.Colour.purple())
                embed.add_field(name='Date:', value=f'{dattt}', inline=True)
                embed.add_field(name='Mood:', value=f'{mod}', inline=True)
                embed.add_field(name="Color:", value=f'{col}', inline=True)
                embed.add_field(name="Lucky Number:", value=f'{lucn}', inline=True)
                embed.add_field(name="Lucky Time:", value=f'{luct}', inline=True)
                embed.add_field(name="Compatibility:", value=f'{comp}', inline=True)
                embed.add_field(name='Description:', value=f'{desc}', inline=False)
                await ctx.send(embed=embed)


#dad jokes
@client.command()
async def dadjoke(ctx):
    headers = {
    'Accept': 'application/json',
    }
    async with aiohttp.ClientSession() as session:
        async with session.get('https://icanhazdadjoke.com/', headers=headers) as r:
            if r.status == 200:
                js = await r.json()
                dadjkk = js["joke"]
                embed = discord.Embed(title='👨 Dad joke huh 👨', description=f"{dadjkk}", colour=discord.Colour.red())
                await ctx.send(embed=embed)


#love msg
@client.command()
async def love(ctx, *, member: discord.Member = None):
    member = member or ctx.author
    url = "https://ajith-messages.p.rapidapi.com/getMsgs"
    querystring = {"category":"love"}
    headers = {
    'x-rapidapi-host': "ajith-messages.p.rapidapi.com",
    'x-rapidapi-key': "91a9efd206msh739aa08c6bcd6aap1a64cejsnda168d255a13"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=querystring) as r:
            if r.status == 200:
                js = await r.json()
                lm = js["Message"]
                ctx.send(f"{member.mention}\n{lm}")