# coding=utf-8

import sys

import dashscope
from dashscope.audio.tts import SpeechSynthesizer
from dotenv import load_dotenv
import os

load_dotenv()

dashscope.api_key = os.getenv("ALIYUN_API_KEY")


def tts():
    """语音合成"""

    model = "sambert-eva-v1"
    txt = """
    I love you more than anything else in the world. I will give you anything you want for it.
    """

    models = {
        "sambert-brian-v1": "Long before you or I were born, there reigned, in a country a great way off, a king who had three sons. ",  # 客服男声, 美式英文
        "sambert-donna-v1": "Every morning she went into the garden and prayed to God in heaven to bestow on her a son or a daughter. ",  # 教育女声, 美式英文
        "sambert-eva-v1": "I love you more than anything else in the world. I will give you anything you want for it.",  # 陪伴女声, 美式英文
        "sambert-cindy-v1": "It was the middle of winter, when the broad flakes of snow were falling around.",  # 对话女声, 美式英文
        "sambert-cally-v1": "This child was a daughter, who was very beautiful; and her mother loved her dearly, and was very kind to her. ",  # 自然女声, 美式英文
        "sambert-betty-v1": "A certain king had a beautiful garden, and in the garden stood a tree which bore golden apples. ", #客服女声, 美式英文
        "sambert-beth-v1": "Time passed on again, and the youngest son too wished to set out into the wide world to seek for the golden bird.", # 咨询女声, 美式英文

        "sambert-zhimiao-emo-v1":"In a village dwelt a poor old woman, who had gathered together a dish of beans and wanted to cook them.",
        "sambert-zhimao-v1":"A shepherd had a faithful dog, called Sultan, who was grown very old, and had lost all his teeth. ",
        "sambert-zhiyue-v1":"A shepherd's dog had a master who took no care of him, but often let him suffer the greatest hunger. ",
        "sambert-zhiyuan-v1":"There was a king who had twelve beautiful daughters. They slept in twelve beds all in one room.",
        "sambert-zhiting-v1":"The little tailor demanded of the king the promised reward; he, however, repented of his promise",
        "sambert-zhistella-v1":"In a great forest dwelt a poor wood-cutter with his wife and his two children. ",
        "sambert-zhishu-v1":"The girl went back to the well not knowing what to do, and at last in her distress she jumped into the water after the spindle.",
        "sambert-zhiqi-v1":"I have nothing to give you; you must go out into the wide world and try your luck.",
        "sambert-zhijing-v1":"A long time ago there lived a king who was famed for his wisdom through all the land. ",
        "sambert-zhijia-v1":"An aged count once lived in Switzerland, who had an only son, but he was stupid, and could learn nothing.",
        "sambert-zhigui-v1": "After many, many years there came a king's son into that land: and an old man told him the story of the thicket of thorns",
        "sambert-zhida-v1": "Let us sit down by the side of the river, and rest a while, to eat and drink", # 标准男声, 中文+英文

        # "sambert-waan-v1": "", #泰语女声, 泰语
        # "sambert-hanna-v1": "", #德语女声, 德语
        # "sambert-clara-v1" : "", #法语女声 , 法语
        # "sambert-indah-v1": "", # 印尼语女声, 印尼语
        # "sambert-perla-v1": "",  # 意大利语女声, 意大利语
        # "sambert-camila-v1": "", # 西班牙语女声, 西班牙语

        
        # "sambert-zhifei-v1": "An honest farmer had once an ass that had been a faithful servant to him a great many years",
        # "sambert-zhilun-v1": "After he had travelled a little way, he spied a dog lying by the roadside and panting as if he were tired.",
        # "sambert-zhishuo-v1":"A king and queen once upon a time reigned in a country a great way off, where there were in those days fairies. ",
        # "sambert-zhiying-v1":"There was once on a time a Fisherman who lived with his wife in a miserable hovel close by the sea, and every day he went out fishing.",
        # "sambert-zhiye-v1":"With that he reached the sea, and the sea was quite black and thick, and began to boil up from below",
        # "sambert-zhiya-v1":"One fine evening a young princess put on her bonnet and clogs, and went out to take a walk by herself in a wood",
        # "sambert-zhixiao-v1":"One day the woman was standing by this window and looking down into the garden",
        # "sambert-zhina-v1":"When the wolf had appeased his appetite, he lay down again in the bed, fell asleep and began to snore very louuuuuud",
        # "sambert-zhimo-v1":"The two strangers were all this time looking on, and did not know what to say for wonder. ",
        # "sambert-zhiming-v1":"By the side of a wood, in a country a long way off, ran a fine stream of water; and upon the stream there stood a mill. ",
        # "sambert-zhihao-v1":"In his trouble and fear he went down into the courtyard and took thought how to help himself out of his trouble.",
        # "sambert-zhiwei-v1":"The path led him into a wood, and there he saw two old ravens standing by their nest, and throwing out their young ones.",
        # "sambert-zhixiang-v1":"There was once upon a time an old goat who had seven little kids, and loved them with all the love of a mother for her children.",
        # "sambert-zhiqian-v1":"The next morning he came to the eldest and took him to a marble table",
        # "sambert-zhiru-v1":"Two kings' sons once upon a time went into the world to seek their fortunes; but they soon fell into a wasteful foolish way of living",
        # "sambert-zhide-v1":"The youth wandered on, and after some time came to a fortress where he begged for a night's lodging. ",
        # "sambert-zhichu-v1":"After some time he took it in his head that he would travel to Rome.",
        # "sambert-zhinan-v1":"You have made good use of your time, and learnt something worth the knowing",
    }

    for k, v in models.items():

        result = SpeechSynthesizer.call(model=k, text=v, sample_rate=16000)
        if result.get_audio_data() is not None:
            with open('./sample_audios/' + k + ".wav", "wb") as f:
                f.write(result.get_audio_data())
            print(
                "SUCCESS: get audio data: %dbytes in output.wav"
                % (sys.getsizeof(result.get_audio_data()))
            )
        else:
            print("ERROR: response is %s" % (result.get_response()))


def main():
    tts()
    pass


if __name__ == "__main__":
    main()
