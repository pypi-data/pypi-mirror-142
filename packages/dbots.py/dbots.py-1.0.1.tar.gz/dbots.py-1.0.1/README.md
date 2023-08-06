# dbots 
useful library for [dbots.online](https://dbots.online)

# API DOCS
Link to api docs: [API DOCS](https://docs.dbots.online)

## Installation
```
pip install dbots
```
## example 
Server Count Post :
```python
from dbots import dbots
from discord.ext import commands

client = commands.Bot(command_prefix="!") 
dbl = dbots(client,"token of dbots")

@client.event
async def on_ready():
  x = await dbl.serverCountPost()
  print(x)

client.run("token")
```

Search bot: 
```python
from dbots import dbots

client = commands.Bot(command_prefix="!") 
dbl = dbots(client,"token of dbots")
id=botid

a = dbl.search(id)
print(a)

```
All functions in api:
```angular2html
1: serverCountPost()
2: search()
3: hasVoted()
```


**JOIN OUR DISCORD SERVER FOR SUPPORT**\
[DISCORD LINK](https://discord.gg/BHyhqk4n)

