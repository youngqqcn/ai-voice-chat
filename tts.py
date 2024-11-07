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
    result = SpeechSynthesizer.call(
        model="sambert-zhichu-v1", text="今天天气怎么样", sample_rate=48000
    )
    if result.get_audio_data() is not None:
        with open("output.wav", "wb") as f:
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
