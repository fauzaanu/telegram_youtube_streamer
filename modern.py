import asyncio
import os
from pytgcalls.types.input_stream.quality import HighQualityAudio, LowQualityAudio, HighQualityVideo, LowQualityVideo, MediumQualityAudio, MediumQualityVideo
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, VideoPiped, AudioVideoPiped
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream

app = Client(
    # your api_id and api_hash
    'telegram_youtube_streamer',
    api_id=123456,
    api_hash='123abc', 
)
call_py = PyTgCalls(app)
group = -123 # define your group chat get this via a bot or call get_dialogs() in pyrogram


# only listen to messages from the group gateway
@app.on_message()
async def play_handler(client: Client, message: Message):
    
    
    if '#play' in message.text and message.chat.id == group:
        print(message.text)
        stream_link = message.text.split(" ")[1]
        # download the stream link
        # ffmpeg -i "$(youtube-dl -x -g "{YOUTUBE_LINK}")" -f s16le -ac 1 -ar {BITRATE} {OUTPUT_FILE}
        print('Downloading stream link...' + stream_link)
        proc = await asyncio.create_subprocess_exec(
            'youtube-dl',
            '-g',
            '-f',
            # CHANGE THIS BASED ON WHAT YOU WANT
            'best[height<=?480][width<=?1080]',
            f'{stream_link}',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        stream_link = stdout.decode().split('\n')[0]


        # start the call
        print('Starting call...')
        await call_py.join_group_call(group,  AudioVideoPiped(
                stream_link,
                HighQualityAudio(),
                HighQualityVideo(),
            ),
            stream_type=StreamType().pulse_stream,)
        await idle()

    elif '#stop' in message.text and message.chat.id == group:
        try:
            await call_py.leave_group_call(group)
        except Exception as e:
            print(e)
    

call_py.start()
idle()