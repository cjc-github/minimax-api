# MiniMax API Python SDK

基于 MiniMax 官方文档封装的 Python SDK，支持文本生成、语音合成、音乐生成、图像生成和编码计划等多种功能。

## 功能模块

### 1. 文本生成 (text-generation)

| 模型 | 说明 | 输出速度 | Token Plan 支持 |
|------|------|----------|-----------------|
| M2.7 | 开启模型的自我迭代 | ~60tps | ✅ 支持 |
| M2.7-highspeed | 极速版，效果不变，更快更敏捷 | ~100tps | ❌ 不支持 |
| M2.5 | 顶尖性能与极致性价比 | ~60tps | ✅ 支持 |
| M2.5-highspeed | 极速版，效果不变，更快更敏捷 | ~100tps | ✅ 支持 |
| M2.1 | 强大多语言编程能力 | ~60tps | ✅ 支持 |
| M2.1-highspeed | 极速版，效果不变，更快更敏捷 | ~100tps | ✅ 支持 |
| M2 | 专为高效编码与 Agent 工作流 | - | ✅ 支持 |

### 2. 语音合成 (text-to-speech)

| 模型 | 说明 | 特点 | Token Plan 支持 |
|------|------|------|-----------------|
| speech-2.8-hd | 最新 HD 模型 | 精准还原真实语气细节 | ✅ 支持 |
| speech-2.8-turbo | 最新 Turbo 模型 | 超低时延 | ❌ 不支持 |
| speech-2.6-hd | HD 模型 | 韵律表现出色 | ❌ 不支持 |
| speech-2.6-turbo | Turbo 模型 | 音质优异 | ❌ 不支持 |
| speech-02-hd | HD 模型 | 稳定性好 | ❌ 不支持 |
| speech-02-turbo | Turbo 模型 | 小语种能力强 | ❌ 不支持 |

### 3. 音乐生成 (music-generation)

| 模型 | 说明 | 特点 | Token Plan 支持 |
|------|------|------|-----------------|
| music-2.6 | 音乐生成 | 强大的音乐生成能力，支持多种风格和标签 | ✅ 支持 |
| music-2.6-highspeed | 极速版 | 极速响应，效果不变 | ❌ 不支持 |
| music-cover | 封面生成 | 根据音乐内容生成匹配的封面图片 | ✅ 支持 |
| lyrics-generation | 歌词生成 | 根据提示词生成完整歌词 | ✅ 支持 |
| lyrics-generation-highspeed | 极速版 | 极速响应，效果不变 | ❌ 不支持 |

### 4. 图像生成 (image-generation)

| 模型 | 说明 | 特点 | Token Plan 支持 |
|------|------|------|-----------------|
| image-01 | 标准版 | 强大的文本到图像生成能力 | ✅ 支持 |
| image-01-turbo | 极速版 | 极速响应，效果不变 | ❌ 不支持 |

### 5. 编码计划 (coding-plan)

| 模型 | 说明 | 特点 | Token Plan 支持 |
|------|------|------|-----------------|
| coding-plan-vlm | VLM 模型 | 视觉语言模型分析，生成编码计划 | ✅ 支持 |
| coding-plan-search | 搜索模型 | 搜索和推荐相关编码计划 | ✅ 支持 |

## 安装

```bash
pip install -r requirements.txt
```

## 快速开始

### 方式一：设置环境变量

```bash
export MINIMAX_API_KEY="your_api_key"
```

### 方式二：代码中传入

```python
client = M27(api_key="your_api_key")
```

## 使用示例

### 文本生成

```python
from text_generation import M27

client = M27(api_key="your_api_key")

response = client.generate(
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ]
)

print(response)
```

### 语音合成

```python
from text_to_speech import Speech28HD

client = Speech28HD(api_key="your_api_key")

response = client.synthesize(
    text="你好，欢迎使用语音合成服务",
    voice_id="male-qn-qingse",
    speed=1.0
)

print(response)
```

### 音乐生成

```python
from music_generation import Music26

client = Music26(api_key="your_api_key")

response = client.generate(
    prompt="一首欢快的流行歌曲，副歌部分朗朗上口",
    style="pop",
    tags=["happy", "upbeat", "dance"]
)

print(response)
```

### 音乐封面生成

```python
from music_generation import MusicCover

client = MusicCover(api_key="your_api_key")

response = client.generate(
    music_url="https://example.com/music.mp3",
    prompt="音乐风格：爵士蓝调，氛围：夜晚酒吧",
    resolution="2k"
)

print(response)
```

### 歌词生成

```python
from music_generation import LyricsGeneration

client = LyricsGeneration(api_key="your_api_key")

response = client.generate(
    prompt="关于追逐梦想的励志歌词",
    genre="pop",
    theme="奋斗"
)

print(response)
```

### 图像生成

```python
from image_generation import Image01

client = Image01(api_key="your_api_key")

response = client.generate(
    prompt="一幅美丽的日落风景画，海面上反射着金色的阳光",
    resolution="1024x1024",
    num_images=1
)

print(response)
```

### 编码计划 VLM

```python
from coding_plan import CodingPlanVLM

client = CodingPlanVLM(api_key="your_api_key")

# 分析图像
response = client.analyze(
    image_url="https://example.com/code-screenshot.png",
    prompt="分析这段代码的功能和结构"
)

# 生成编码计划
response = client.generate_plan(
    description="一个用户登录注册系统",
    language="python",
    framework="flask"
)

print(response)
```

### 编码计划搜索

```python
from coding_plan import CodingPlanSearch

client = CodingPlanSearch(api_key="your_api_key")

# 搜索
response = client.search(
    query="用户认证和授权系统设计",
    max_results=10,
    language="python"
)

# 推荐
response = client.recommend(
    context="我正在开发一个电商平台，需要处理订单管理、支付集成、库存管理等核心功能",
    num_recommendations=5
)

print(response)
```

## 运行示例脚本

### 文本生成示例

```bash
cd text-generation
python example.py --help
python example.py m27
python example.py interactive
```

### 语音合成示例

```bash
cd text-to-speech
python example.py --help
python example.py 28-hd
python example.py interactive
```

### 音乐生成示例

```bash
cd music-generation
python example.py --help
python example.py music-26           # 测试 Music 2.6
python example.py music-26-hs         # 测试极速版
python example.py music-cover        # 测试封面生成
python example.py lyrics              # 测试歌词生成
python example.py all                 # 运行所有测试
```

### 图像生成示例

```bash
cd image-generation
python example.py --help
python example.py image-01            # 测试 Image 01
python example.py image-01-turbo      # 测试极速版
python example.py resolutions          # 测试不同分辨率
python example.py all                  # 运行所有测试
```

### 编码计划示例

```bash
cd coding-plan
python example.py --help
python example.py vlm-analyze          # 测试 VLM 图像分析
python example.py vlm-generate         # 测试 VLM 生成计划
python example.py search              # 测试搜索功能
python example.py recommend            # 测试推荐功能
python example.py all                  # 运行所有测试
```

### 综合测试

```bash
# 运行所有模块的综合测试
python test_all_modules.py
```

## 文档

- [文本生成模块文档](text-generation/README.md)
- [语音合成模块文档](text-to-speech/README.md)
- [音乐生成模块文档](music-generation/)
- [图像生成模块文档](image-generation/)
- [编码计划模块文档](coding-plan/)
- [完整功能说明](API_FEATURES.md)

## 获取 API Key

1. 登录 [MiniMax 开放平台](https://platform.minimaxi.com)
2. 进入「接口密钥」页面
3. 创建 Token Plan Key 或按量付费 API Key
4. 参考官方文档：https://platform.minimaxi.com/docs/api-reference/api-overview