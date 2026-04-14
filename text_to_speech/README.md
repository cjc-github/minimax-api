# text-to-speech 模块使用文档

## 概述

text-to-speech 模块提供 MiniMax 语音合成 API 的封装，支持多种语音模型。

## 支持的模型

| 模型 | 说明 | 特点 |
|------|------|------|
| speech-2.8-hd | 最新 HD 模型 | 精准还原真实语气细节，全面提升音色相似度 |
| speech-2.8-turbo | 最新 Turbo 模型 | 精准还原真实语气细节，超低时延 |
| speech-2.6-hd | HD 模型 | 韵律表现出色，极致音质与韵律表现，生成更快更自然 |
| speech-2.6-turbo | Turbo 模型 | 音质优异，超低时延，响应更灵敏 |
| speech-02-hd | HD 模型 | 出色的韵律、稳定性和复刻相似度，音质表现突出 |
| speech-02-turbo | Turbo 模型 | 出色的韵律和稳定性，小语种能力加强 |

## 安装依赖

```bash
pip install requests
```

## 快速开始

### Speech 2.8 HD 模型使用示例

```python
from text_to_speech import Speech28HD

# 初始化客户端
client = Speech28HD(api_key="your_api_key")

# 调用语音合成
response = client.synthesize(
    text="你好，欢迎使用 MiniMax 语音合成服务",
    voice_id="male-qn-qingse"
)

print(response)
```

### Speech 2.8 Turbo 模型使用示例

```python
from text_to_speech import Speech28Turbo

client = Speech28Turbo(api_key="your_api_key")

response = client.synthesize(
    text="你好，欢迎使用 MiniMax 语音合成服务",
    voice_id="female-shaonv",
    speed=1.2  # 语速 1.2 倍
)

print(response)
```

### 自定义音频参数示例

```python
from text_to_speech import Speech26HD

client = Speech26HD(api_key="your_api_key")

response = client.synthesize(
    text="这是一段自定义音频参数的语音合成",
    voice_id="male-qn-qingse",
    speed=0.8,         # 语速放慢到 0.8 倍
    volume=1.5,        # 音量提高到 1.5 倍
    pitch=2,           # 语调升高 2 个半音
    audio_format="mp3",
    sample_rate=32000,
    bitrate=128000
)

print(response)
```

### 使用不同格式示例

```python
from text_to_speech import Speech02HD

client = Speech02HD(api_key="your_api_key")

# 使用 PCM 格式
response = client.synthesize(
    text="生成 PCM 格式音频",
    audio_format="pcm",
    sample_rate=16000
)

# 使用 WAV 格式
response = client.synthesize(
    text="生成 WAV 格式音频",
    audio_format="wav"
)
```

## API 参考

### Speech28HD 类

```python
class Speech28HD:
    def __init__(self, api_key: str)
    
    def synthesize(
        self,
        text: str,
        voice_id: str = "male-qn-qingse",
        model: str = "speech-2.8-hd",
        speed: float = 1.0,
        volume: float = 1.0,
        pitch: float = 0,
        audio_format: str = "mp3",
        sample_rate: int = 32000,
        bitrate: int = 128000,
        timeout: int = 60
    ) -> Dict[str, Any]
```

#### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| text | str | - | 待合成文本，最大 10,000 字符 |
| voice_id | str | "male-qn-qingse" | 音色 ID |
| model | str | "speech-2.8-hd" | 模型名称 |
| speed | float | 1.0 | 语速，范围 0.5-2.0 |
| volume | float | 1.0 | 音量，范围 0.1-10.0 |
| pitch | float | 0 | 语调，范围 -12-12 |
| audio_format | str | "mp3" | 音频格式，支持 mp3/pcm/flac/wav |
| sample_rate | int | 32000 | 采样率 |
| bitrate | int | 128000 | 比特率 |
| timeout | int | 60 | 请求超时时间（秒） |

#### 返回值

返回 JSON 格式的响应，包含音频数据。

---

### 常用音色 ID 参考

| 音色 ID | 说明 |
|---------|------|
| male-qn-qingse | 青涩青年男声 |
| female-shaonj | 少女声 |
| female-yujie | 御姐声 |
| male-badao | 霸道总裁声 |
| female-tianmei | 天真甜美声 |

（注：更多音色 ID 请参考官方文档）

---

### 其他模型类

其他模型类（Speech28Turbo, Speech26HD, Speech26Turbo, Speech02HD, Speech02Turbo）的 API 与 Speech28HD 相同，仅默认模型不同。

## 支持的语言

语音合成支持 40+ 种语言，包括：

- 中文（Chinese）
- 粤语（Cantonese）
- 英语（English）
- 西班牙语（Spanish）
- 法语（French）
- 俄语（Russian）
- 德语（German）
- 葡萄牙语（Portuguese）
- 阿拉伯语（Arabic）
- 意大利语（Italian）
- 日语（Japanese）
- 韩语（Korean）
- 印尼语（Indonesian）
- 越南语（Vietnamese）
- 土耳其语（Turkish）
- 荷兰语（Dutch）
- 泰语（Thai）
- 波兰语（Polish）
- 等等...

## 错误处理

```python
from text_to_speech import Speech28HD
import requests

client = Speech28HD(api_key="your_api_key")

try:
    response = client.synthesize(
        text="你好",
        timeout=30
    )
    print(response)
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")