import re
import requests
from slackbot.bot import respond_to

def gas_translate(text, source='en', target='ja'):
    translation_url = 'https://script.google.com/macros/xxxxxxxxxxxxxxxxxxxxxx'
    params = {
        'text':text,
        'source':source,
        'target':target,
    }

    response = requests.get(translation_url, params=params)
    if response.status_code != 200:
        return '翻訳失敗 (Error Code: %d)' % response.status_code
    else:
        return response.content.decode('utf-8')

@respond_to('')
def reply_translation(message):
    message.reply('メッセージを取得しました．翻訳中...')

    # テキストの整形
    msg_txt = message.body['text']
    msg_txt = msg_txt.replace('\n', ' ')
    msg_txt = msg_txt.replace('\r', ' ')
    lines = re.split('(?<=[^A-Z]\.) (?=[A-Z])', msg_txt)

    # 各文翻訳
    reply_txt = ''
    for ln in lines:
        reply_txt += '==== ==== ==== ====\n'
        reply_txt += ln + '\n'
        reply_txt += gas_translate(ln) + '\n'

    # 送信
    message.reply(reply_txt)