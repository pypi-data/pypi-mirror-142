# bhbotlist 
useful library for [bhbotlist.xyz](https://bhbotlist.xyz)

# API DOCS
Link to api docs: [API DOCS](https://docs.bhbotlist.xyz)

## Installation
```
pip install bhbotlist
```
## example 
Server Count Post :
```python
from bhbotlist import bhbotlist
from discord.ext import commands

client = commands.Bot(command_prefix="!") 
dbl = bhbotlist(client,"token of bhbotlist")

@client.event
async def on_ready():
  x = await dbl.serverCountPost()
  print(x)

client.run("token")
```

Search bot: 
```python
from bhbotlist import bhbotlist

client = commands.Bot(command_prefix="!") 
dbl = bhbotlist(client,"token of bhbotlist")
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
[DISCORD LINK](https://bhbotlist.xyz/dc)

