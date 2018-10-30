#===========================================================================================================================                                                                                                                          
#   SSSSSSSSSSSSSSS PPPPPPPPPPPPPPPPP        AAA               DDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEE   SSSSSSSSSSSSSSS  
# SS:::::::::::::::SP::::::::::::::::P      A:::A              D::::::::::::DDD   E::::::::::::::::::::E SS:::::::::::::::S
#S:::::SSSSSS::::::SP::::::PPPPPP:::::P    A:::::A             D:::::::::::::::DD E::::::::::::::::::::ES:::::SSSSSS::::::S
#S:::::S     SSSSSSSPP:::::P     P:::::P  A:::::::A            DDD:::::DDDDD:::::DEE::::::EEEEEEEEE::::ES:::::S     SSSSSSS
#S:::::S              P::::P     P:::::P A:::::::::A             D:::::D    D:::::D E:::::E       EEEEEES:::::S            
#S:::::S              P::::P     P:::::PA:::::A:::::A            D:::::D     D:::::DE:::::E             S:::::S            
# S::::SSSS           P::::PPPPPP:::::PA:::::A A:::::A           D:::::D     D:::::DE::::::EEEEEEEEEE    S::::SSSS         
#  SS::::::SSSSS      P:::::::::::::PPA:::::A   A:::::A          D:::::D     D:::::DE:::::::::::::::E     SS::::::SSSSS    
#    SSS::::::::SS    P::::PPPPPPPPP A:::::A     A:::::A         D:::::D     D:::::DE:::::::::::::::E       SSS::::::::SS  
#       SSSSSS::::S   P::::P        A:::::AAAAAAAAA:::::A        D:::::D     D:::::DE::::::EEEEEEEEEE          SSSSSS::::S 
#            S:::::S  P::::P       A:::::::::::::::::::::A       D:::::D     D:::::DE:::::E                         S:::::S
#            S:::::S  P::::P      A:::::AAAAAAAAAAAAA:::::A      D:::::D    D:::::D E:::::E       EEEEEE            S:::::S
#SSSSSSS     S:::::SPP::::::PP   A:::::A             A:::::A   DDD:::::DDDDD:::::DEE::::::EEEEEEEE:::::ESSSSSSS     S:::::S
#S::::::SSSSSS:::::SP::::::::P  A:::::A               A:::::A  D:::::::::::::::DD E::::::::::::::::::::ES::::::SSSSSS:::::S
#S:::::::::::::::SS P::::::::P A:::::A                 A:::::A D::::::::::::DDD   E::::::::::::::::::::ES:::::::::::::::SS 
# SSSSSSSSSSSSSSS   PPPPPPPPPPAAAAAAA                   AAAAAAADDDDDDDDDDDDD      EEEEEEEEEEEEEEEEEEEEEE SSSSSSSSSSSSSSS   
#==========================================================================================================================                                                                                                                         

#import requirements                                                                                                                          
import asyncio
import datetime
import discord
import os
from discord.ext import commands
		
#setup bots prefix and tokens
prefix = "$"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
commands = """```diff
-Admin Commands-
-==============-
-./add role-
-./remove role-
-./remove all roles-
-./Destroy the server-
-./Change nickname-
-./change all nicknames-
-./server info-
-./user info-
-./purge-

-Fun Commands-
-============-
-./rr = russian roulette-
-./8ball = magic 8 ball-

-EXTRAS-
-======-
-./proxy = gives random no log proxy sites-
-./namegen = generates 1st and last name-
-./shutdown = kill the bot-
```
"""

@bot.event
async def on_ready():
	print ("""
                	_.+sd$$$$$$$$$bs+._                   
               .+d$$$$$$$$$$$$$$$$$$$$$b+.               
            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.            
          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          
        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        
       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       
     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     
    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    
   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   
  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  
  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  
 :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; 
 $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ 
:$$$$$$$b            `*T$$$s                      :$$$$$;
:$$$$$$$$b.                                        $$$$$;
$$$$$$$$$$$b.                                     :$$$$$$
$$$$$$$$$$$$$bs.                                 .$$$$$$$
$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
 $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
 :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$; 
  $$$b       `T$b+                        :$$$$$$$BUG$$  
  :$P'         `"'               ,._.     ;$$$$$$$$$$$;  
   \                            `*TP*     d$$P*******$   
    \                                    :$$P'      /    
     \                                  :dP'       /     
      `.                               d$P       .'      
        `.                             `'      .'        
          `-.                               .-'          
             `-.                         .-'             
                `*+-._             _.-+*'                
                      `"*-------*"'
============================================================
<CREDITS> CODED BY SPADES[...]
<TO> MR.PROXY[...]
<FROM> SPADES[...]
<COMMENT> ENJOY THE BOT!!![...]
============================================================
""")
	print ('Logged in as')
	print (bot.user.name)
	print (bot.user.id)
	
@bot.command(pass_context=True)
async def commands(ctx):
	await ctx.send("""```diff
-Self Commands-
-=============-
-./purge-
-./status-
-./guild-
	
-Admin Commands-
-==============-
-./add role-
-./remove role-
-./remove all roles-
-./Destroy the server-
-./Change nickname-
-./change all nicknames-
-./kick user-
-./ban user-
-./server info-
-./user info-

-Fun Commands-
-============-
-./rr = russian roulette-
-./8ball = magic 8 ball-

-EXTRAS-
-======-
-./proxy = gives random no log proxy sites-
-./namegen = generates 1st and last name-
-./shutdown = kill the bot-
```
""")

@bot.command(pass_context=True)
async def rr(ctx):
	croll = ("```diff -you pick up the revolver and spin the chamber-```")
	roll = ('```css you shot yourself and died','you live for now and pass the gun```')
	await ctx.send(croll)
	await ctx.send(random.choice(roll))

@bot.command(pass_context=True)	
async def purge(message, parameters, recursion=0):
    if parameters == '':
        await reply(message, commands['purge'][1].format(PREFIX))
        return
    if not parameters.isdigit():
        await reply(message, "Number of messages to purge must be a positive integer.")
        return
    async for msg in bot.logs_from(message.channel, limit=int(parameters) + 1):
        try:
            await bot.delete_message(msg)
        except:
            pass
    success_msg = await bot.send_message(message.channel, "Successfully purged **" + parameters + "** messages! :thumbsup:")
    await asyncio.sleep(2)
    await bot.delete_message(success_msg)

bot.command(pass_context=True)
async def serverinfo(message, parameters, recursion=0):
    server = message.server
    text = 0
    voice = 0
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            text += 1
        elif channel.type == discord.ChannelType.voice:
            voice += 1
    msg = "```autohotkey\n"
    msg += '                id: {server.id}\n'
    msg += '       server name: {server.name}\n'
    try:
        msg += '             owner: {server.owner.name}#{server.owner.discriminator} ({server.owner.id})\n'
    except:
        msg += '             owner: <error - could not get information on owner>\n'
    msg += '        created at: {server.created_at} ({} ago)\n'.format(strfdelta(datetime.datetime.utcnow() - server.created_at), server=server)
    msg += '            region: {server.region}\n'
    msg += '           members: {server.member_count}\n'
    msg += 'verification level: {server.verification_level}\n'
    msg += '          channels: {} channels ({} text, {} voice)\n'.format(text + voice, text, voice)
    if len(server.roles) > 50:
        msg += '             roles: {} roles, showing top 50\n{}\n'.format(len(server.roles), ', '.join([x.name for x in server.role_hierarchy][0:50]))
    else:
        msg += '             roles: {} roles\n{}\n'.format(len(server.role_hierarchy), ', '.join(map(lambda x: x.name, server.role_hierarchy)))
    msg += '            emojis: {}\n'.format(len(server.emojis))
    msg += '              icon:```{server.icon_url}'
    await reply(message, msg.format(server=server))


bot.run("NDcxNDc5OTQ2OTc2NDI4MDUy.DrYQLw.yVAu2aJsC3toRX-My7bqqBLSvCk", bot=False)
