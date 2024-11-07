# ai-voice-chat
ai 语音聊天


> 确保已经安装python的包管理 poetry

在 `.env` 设置 APIKEY `ALIYUN_API_KEY`


## 语音识别

- 官方文档： https://help.aliyun.com/zh/model-studio/developer-reference/quick-start-7

- 采用 “录音文件识别”

- 运行示例代码:  [asr.py](./asr.py)

```
poetry shell

poetry install

python asr.py

```


## 语音合成

- 官方文档： https://help.aliyun.com/zh/model-studio/developer-reference/sambert-quick-start

- 音色列表： https://help.aliyun.com/zh/model-studio/developer-reference/model-list

- 运行示例代码: [tts.py](./tts.py)

```
poetry shell

poetry install

python tts.py

```



##  前端录音

在线体验：  https://youngqqcn.github.io/ai-voice-chat/

- 代码:
  - [index.html](./index.html)
  - [recorder.js](./recorder.js)