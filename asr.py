# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html

import json
from urllib import request
from http import HTTPStatus

import dashscope

from dotenv import load_dotenv
import os

load_dotenv()

dashscope.api_key = os.getenv("ALIYUN_API_KEY")

task_response = dashscope.audio.asr.Transcription.async_call(
    model="paraformer-v2",
    file_urls=[
        "https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/paraformer/hello_world_female2.wav",
        "https://dashscope.oss-cn-beijing.aliyuncs.com/samples/audio/paraformer/hello_world_male2.wav",
    ],
    language_hints=["zh", "en"],
)  # “language_hints”只支持paraformer-v2和paraformer-realtime-v2模型

transcription_response = dashscope.audio.asr.Transcription.wait(
    task=task_response.output.task_id
)

if transcription_response.status_code == HTTPStatus.OK:
    for transcription in transcription_response.output["results"]:
        url = transcription["transcription_url"]
        result = json.loads(request.urlopen(url).read().decode("utf8"))
        print(json.dumps(result, indent=4, ensure_ascii=False))
    print("transcription done!")
else:
    print("Error: ", transcription_response.output.message)
