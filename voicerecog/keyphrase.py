# Azureの音声認識, 合成
class Color:
	BLACK          = '\033[30m'#(文字)黒
	RED            = '\033[31m'#(文字)赤
	GREEN          = '\033[32m'#(文字)緑
	YELLOW         = '\033[33m'#(文字)黄
	BLUE           = '\033[34m'#(文字)青
	MAGENTA        = '\033[35m'#(文字)マゼンタ
	CYAN           = '\033[36m'#(文字)シアン
	WHITE          = '\033[37m'#(文字)白
	COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
	BOLD           = '\033[1m'#太字
	UNDERLINE      = '\033[4m'#下線
	INVISIBLE      = '\033[08m'#不可視
	REVERCE        = '\033[07m'#文字色と背景色を反転
	BG_BLACK       = '\033[40m'#(背景)黒
	BG_RED         = '\033[41m'#(背景)赤
	BG_GREEN       = '\033[42m'#(背景)緑
	BG_YELLOW      = '\033[43m'#(背景)黄
	BG_BLUE        = '\033[44m'#(背景)青
	BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
	BG_CYAN        = '\033[46m'#(背景)シアン
	BG_WHITE       = '\033[47m'#(背景)白
	BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
	RESET          = '\033[0m'#全てリセット
try:
    from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
    from azure.cognitiveservices.speech.audio import AudioOutputConfig
    import azure.cognitiveservices.speech as speechsdk
    speech_config = speechsdk.SpeechConfig(subscription="**********", region="japanwest")
    speech_config.speech_recognition_language="ja-JP"
    speech_config.speech_synthesis_voice_name='ja-JP-NanamiNeural'

    speech_config.set_property(speechsdk.PropertyId.Speech_SegmentationSilenceTimeoutMs, "3000")
    speech_config.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "3000")

    audio_config = AudioOutputConfig(use_default_speaker=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    import time
    import re
    import random
    import datetime
    import winsound # 音声ファイルの再生
except Exception as e:
    print(f'{Color.RED}'"keyphrase : "+str(e)+f'{Color.RESET}')
    subprocess.run(["ShutDown.bat"])



# 関数
# def fill(response):
# def filler(text):
# def Reviving_Lost_Words(rist):
# def mecab(text)
# def speech_recog(search_recom):
 # search_recomは　0:検索　1:おすすめ　をspeech_recogに送る

# 検索の際、and検索かor検索かを設定
and_or='or'

import MeCab
# MeCab.Tagger('') //オブジェクト
# tagger.parseToNode(text) //きりわけ
# pos = node.feature.split(',')[0] //品詞の判別

part_of_speech=['人名', '代名詞','固有名詞', '名詞']

tagger= MeCab.Tagger(r'-d"C:\mecab-ipadic-neologd"')

def filler(text):
    fillers_and_symbols = [
        '。', '？', '！', 'あー', 'あのー', 'あの', 'あれ', 'とー',
        'ええ', 'えーっと', 'えっと', 'えー', 'えっ', 'え', 'うーんと', 'うーんん', 'うーん', 
        'うー', 'うう', 'うん', 'そういう', 'のような', 'ような', 'みたいな', 'それで', 
        'それから', 'そんな', 'まあ', 'まぁ', 'あ ', ' ー', 'さん', 'さま ', '関する',
        'まじ ', 'マジ ','んー','まあ','そのー','ええと','なんていうか','何ていうか','何て言うか',
        'なんて言うか','こう','ほら','んーっと','どうだっけ','そうだなぁ','そうだなー','なんだろう','なんだろー',
        'でしょ','ね？','ほらね','わかるよ','えーっとさー','だからさ','かなぁ','みたいな','とりあえず','取り合えず',
        '取りあえず','取り敢えず','なんか','ていうか'
    ]
    # フィラーや記号を空白に置換
    for fs in fillers_and_symbols:
        text = text.replace(fs, ' ')
    return text

# '本'のような図書館検索に必要のない単語を消す
def delete_word(response):
    j=0
    # 削除するワードのリスト
    stop_words = ['系', '本','の','こと','検索','しよう','ん','さ','方','紹介','お願い'] # 日本や生態系などのワードに影響するため分けた。
    for fs in stop_words:
        if fs == response:
            response=''
    j+=1
    return response

# mecabで消されてしまう単語を呼び戻す
def Reviving_Lost_Words(rist):
    add_que=[]
    Lost_Words=[
        ''
    ]
    for fs in Lost_Words:
        if fs in rist[0]:
            rist[0]=rist[0].replace(fs, ' ')
            add_que.append(fs)
        add_text=" ".join(add_que)
    return add_text

# mecabで形態素解析
def mecab(text):
    node = tagger.parseToNode(text)
    # print(node)
    que=[]
    while node:
        term=node.surface
        term=delete_word(term)     # '本'のような図書館検索に必要のない単語を消す
        # print(node.feature.split())
        pos = node.feature.split(',')   # listになってる
        part_num=0
        for _ in part_of_speech:
            if _ in pos:
                if term in que:    # 単語を重複させない
                    break
                que.append(term)
                break
            part_num+=1
        node = node.next
    text_result = ' '.join(que)
    return text_result

# main文
def speech_recog(search_recom):
    # roop=2になったら聞き返すことを終了させる
    roop=0
    
    d = speech_recognizer.recognize_once_async().get()
    speechget=d.text
    print(f'{Color.GREEN}'"voicerecog : *"+str(d.text)+"＊を認識しました"+f'{Color.RESET}')
    rist=speechget.split(",")
    print(rist[0])

    #フィラー
    text=filler(speechget)

    #mecabで形態素解析
    text=mecab(text)
    print(text)
    
    if not not text:
        speech_synthesizer.speak_text(text+"に関する本をご紹介します")
        
        # or検索するなら空白を|に変換する <=> and検索は空白
        if and_or=='or':
            text = text.replace(' ', '|') # 空白を'|'に置換
            

        # "おすすめ"の場合
        if search_recom==1:
            if '小説' == text:
                synthesizer.speak_text("最近入ったお勧めの小説を表示します。")
                return text
            else:
                #synthesizer.speak_text("お勧めの本を表示します。")
                return text
        return text

    # if not text:
    #     roop+=1
    #     text=""
    #     if roop<3:
    #         # "もう一度お願いします"
    #         #speech_synthesizer.speak_text("もう一度お願いします")
    #         winsound.PlaySound('sound\mouitidoonegaisimasu2.wav',winsound.SND_FILENAME)
    #     else:
    #         speech_synthesizer.speak_text("すみません。初めからやり直してください")
    #         return text
    else:
        return text


# # デバッグ用
# synthesizer.speak_text("本の検索ですね。著者やキーワードを教えてください。")
# text=speech_recog(1)    # 0は検索　1はおすすめ