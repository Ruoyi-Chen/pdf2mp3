from gtts import gTTS
import pyttsx3
# from pydub import AudioSegment

def str_to_mp3(text, save_file = False, save_as = "test.mp3",
               say = False, rate = 200, volume = 0.8):
    engine = pyttsx3.init()

    """Rate"""
    # rate = engine.getProperty('rate') # getting details of current speaking rate
    engine.setProperty('rate', rate) # setting up new voice rate

    """Volume"""
    # volume = engine.getProperty('volume')
    engine.setProperty('volume', volume) # setting up volume level between 0 and 1

    """Voice"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    # engine.setProperty('voice',"com.apple.speech.synthesis.voice.ting-ting.premium") #普通话
    # engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji") #粤语
    # engine.setProperty('voice',"com.apple.speech.synthesis.voice.mei-jia") #台湾腔
    # engine.setProperty('voice',"com.apple.speech.synthesis.voice.fiona.premium")

    if say:
        print("****************Speaking the contents....****************")
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        print("****************End speaking.****************")


    """Saving voice to a file"""
    if save_file:
        print("****************Saving to file...****************")
        # pyttsx3语音（python3.7）
        # engine.save_to_file(text, save_as)
        # engine.runAndWait()

        # 谷歌语音
        tts = gTTS(text=text, lang='en-uk')
        tts.save(save_as)
        print("****************File saved.****************")
