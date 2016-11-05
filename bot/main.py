import os

from aiotg import Bot
import logging

# Logging
from abuse import matfilter

logging.basicConfig(
    level=getattr(logging, os.environ.get('BOT_LOGGING_LEVEL', 'DEBUG')),
    format='%(asctime)s | %(name)s | %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logger.addHandler(ch)

moderator_id = os.environ['BOT_NOTIFICATION_USER_ID']

bot = Bot(
    api_token=os.environ["BOT_TOKEN"])

private = bot.private(moderator_id)


async def notify_moderator(chat, abuse=False):
    message_id = chat.message['message_id']
    tags = ['foul']
    if abuse:
        tags.append('abuse')
    alert_message = "{tags} user @{username} with userid: {userid} in {chat} chat sent".format(
        username=chat.message['from'].get('username', 'unknown'),
        chat=chat.message['chat']['title'],
        userid=chat.message['from']['id'],
        tags=" #".join(tags)
    )
    await private.send_text(alert_message)
    await private.forward_message(chat.id, message_id)


@bot.handle("photo")
@bot.handle("video")
@bot.handle("audio")
@bot.handle("voice")
@bot.handle("document")
@bot.handle("sticker")
async def handle(chat, media):
    await notify_moderator(chat)

    try:
        username = chat.message['from']['username']
    except KeyError:
        text = "В чате запрещена отправка медиаконтента напрямую и использование стикеров. Мана-мана. #foul"
    else:
        text = '@{}, в чате запрещена отправка медиаконтента напрямую и использование стикеров. Мана-мана. #foul'.format(
            username)

    await chat.reply(text)


@bot.command(".*")
async def check_mats(chat, match):
    if len(matfilter(match.group(0))):
        await notify_moderator(chat)
        # await chat.reply('В вашем сообщение присутствует брань. Мана-мана.')


@bot.default
async def default(chat, match):
    await chat.send_text(
        'Да, капитан!?'
    )


if __name__ == "__main__":
    logger.info("Running...")
    bot.run()
