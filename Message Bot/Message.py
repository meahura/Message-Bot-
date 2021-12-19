from pyrogram import Client
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters
from pyrogram.types import * 
from pyromod import listen  

app = Client(
    session_name= "message" , 
    api_hash= "هش" , # https://my.telegram.org/auth
    api_id= 'ایدی' , 
    bot_token= "توکن ربات" # @BotFather 

)

@app.on_message(filters.text) 
async def Bot_message(Client , m:Message): 
    user = m.text

    send_message_Admin = await app.ask(chat_id =m.from_user.id , text="""✅ کاربر عزیز به ربات خوش آمدید. شما در حال ارسال پیام به ادمین میباشید.
سازنده : @CyberyArmyy""") 

    await app.send_message('ایدی اکانت' , text=f'''

username = @{m.from_user.username} 
ID = ```{m.from_user.id}```
text = {send_message_Admin.text}
''')

    await m.reply('✅پیام شما ارسال شد.')

app.run()

# Packge install : 
#  - pyrogram --> pip install pyrogram 
#  - pyromod -> pip install pyromod 
# - owner : @CyberyArmyy
