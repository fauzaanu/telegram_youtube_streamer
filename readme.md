# Telegram Youtube Streamer

Objectives were to make a userbot that streams a youtube video in telegram chat. decided to use pyrogram as I used telethon before.

1. pyrogram
2. join a voice chat
3. stream stuff

---

## INSTALLATION

RUN SEPERATELY!!

```
apt install ffmpeg
apt install youtube-dl
apt install nodejs
apt install python-virtualenv
python-virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Dont forget to fill line 15 - 22

api_id and api_hash comes from going to my.telegram.org

and the group_id can be got through a bot like https://t.me/MyChatInfoBot
or through running a get_dialog in pyrogram

## MORE FEATURES?

Saw a lot of other implementations of the same thing with a lot of new features. I have decided to write this to do exactly this specefically. If you contributing please make sure to implement features enhancing this one thing instead of adding new features.

Also I did not think it was reasonable to make the bot publicly work for everyone. Which is why my code is defining it to work on one group only. So you and your friends can enjoy the bot instead of getting performance drops because others are using it.
