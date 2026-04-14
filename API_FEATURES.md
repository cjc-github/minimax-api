# MiniMax API 功能模块说明

本文档详细介绍 MiniMax API Python SDK 中所有可用的功能模块。

## 📁 项目结构

```
minimax-api/
├── __init__.py                    # 主入口，导出所有模块
├── text_generation/               # 文本生成模块
│   ├── __init__.py
│   ├── m27.py                     # M2.7 系列模型
│   ├── m25.py                     # M2.5 系列模型
│   ├── m21.py                     # M2.1 系列模型
│   ├── m2.py                      # M2 模型
│   └── example.py                 # 示例代码
├── text_to_speech/                # 语音合成模块
│   ├── __init__.py
│   ├── speech_28.py               # Speech 2.8 系列
│   ├── speech_26.py               # Speech 2.6 系列
│   ├── speech_02.py                # Speech 02 系列
│   └── example.py                 # 示例代码
├── music_generation/              # 音乐生成模块 ✨ 新增
│   ├── __init__.py
│   ├── music_26.py                 # Music 2.6 系列
│   ├── music_cover.py             # Music Cover
│   ├── lyrics_generation.py       # 歌词生成
│   └── example.py                 # 示例代码
├── image_generation/              # 图像生成模块 ✨ 新增
│   ├── __init__.py
│   ├── image_01.py                # Image 01 系列
│   └── example.py                 # 示例代码
└── coding_plan/                   # 编码计划模块 ✨ 新增
    ├── __init__.py
    ├── coding_plan_vlm.py         # VLM 视觉语言模型
    ├── coding_plan_search.py      # 搜索功能
    └── example.py                 # 示例代码
```

---

## 🎵 音乐生成模块 (music_generation)

### 1. Music 2.6 (music-2.6)

**功能**: 强大的音乐生成能力，支持多种风格和标签

**类**:
- `Music26`: 标准版音乐生成
- `Music26Highspeed`: 极速版音乐生成

**主要参数**:
- `prompt`: 音乐描述提示词
- `duration`: 音乐时长（秒），可选
- `style`: 音乐风格（如 "pop", "rock", "jazz"），可选
- `tags`: 音乐标签列表，可选
- `output_token_limit`: 输出 token 限制

**示例**:
```python
from music_generation import Music26

client = Music26(api_key="your_api_key")
response = client.generate(
    prompt="一首欢快的流行歌曲，副歌部分朗朗上口",
    style="pop",
    tags=["happy", "upbeat", "dance"]
)
```

**使用示例**:
```bash
python music_generation/example.py music-26
python music_generation/example.py music-26-hs
```

---

### 2. Music Cover (music-cover)

**功能**: 根据音乐内容生成匹配的封面图片

**类**: `MusicCover`

**主要参数**:
- `music_url`: 音乐文件的 URL 地址
- `prompt`: 封面描述提示词，可选
- `resolution`: 图片分辨率，支持 "1k", "2k", "4k"

**示例**:
```python
from music_generation import MusicCover

client = MusicCover(api_key="your_api_key")
response = client.generate(
    music_url="https://example.com/music.mp3",
    prompt="音乐风格：爵士蓝调，氛围：夜晚酒吧",
    resolution="2k"
)
```

**使用示例**:
```bash
python music_generation/example.py music-cover
```

---

### 3. Lyrics Generation (lyrics_generation)

**功能**: 根据提示词生成完整的歌词内容

**类**:
- `LyricsGeneration`: 标准版歌词生成
- `LyricsGenerationHighspeed`: 极速版歌词生成

**主要参数**:
- `prompt`: 歌词描述或主题提示词
- `genre`: 音乐流派（如 "pop", "rock", "ballad"），可选
- `theme`: 歌词主题（如 "love", "nature", "life"），可选
- `max_tokens`: 最大生成 token 数

**示例**:
```python
from music_generation import LyricsGeneration

client = LyricsGeneration(api_key="your_api_key")
response = client.generate(
    prompt="关于追逐梦想的励志歌词",
    genre="pop",
    theme="奋斗"
)
```

**使用示例**:
```bash
python music_generation/example.py lyrics
python music_generation/example.py lyrics-hs
```

---

## 🖼️ 图像生成模块 (image_generation)

### 4. Image 01 (image-01)

**功能**: 强大的文本到图像生成能力

**类**:
- `Image01`: 标准版图像生成
- `Image01Turbo`: 极速版图像生成

**主要参数**:
- `prompt`: 图像描述提示词
- `resolution`: 图像分辨率，支持 "512x512", "1024x1024", "2048x2048" 等
- `num_images`: 生成图像数量，默认 1

**示例**:
```python
from image_generation import Image01

client = Image01(api_key="your_api_key")
response = client.generate(
    prompt="一幅美丽的日落风景画，海面上反射着金色的阳光",
    resolution="1024x1024",
    num_images=1
)
```

**使用示例**:
```bash
python image_generation/example.py image-01
python image_generation/example.py image-01-turbo
python image_generation/example.py resolutions
```

---

## 💻 编码计划模块 (coding_plan)

### 5. Coding Plan VLM (coding-plan-vlm)

**功能**: 视觉语言模型分析，支持分析代码截图或图表，生成编码计划

**类**: `CodingPlanVLM`

**主要方法**:

#### analyze() - 图像分析
- `image_url`: 图像 URL 地址
- `prompt`: 分析提示词
- `max_tokens`: 最大生成 token 数

#### generate_plan() - 生成编码计划
- `description`: 功能描述
- `language`: 编程语言（如 "python", "javascript", "java"），可选
- `framework`: 框架（如 "react", "vue", "django"），可选
- `max_tokens`: 最大生成 token 数

**示例**:
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
```

**使用示例**:
```bash
python coding_plan/example.py vlm-analyze
python coding_plan/example.py vlm-generate
```

---

### 6. Coding Plan Search (coding-plan-search)

**功能**: 搜索相关的编码计划和解决方案，基于上下文推荐相关的编码计划

**类**: `CodingPlanSearch`

**主要方法**:

#### search() - 搜索
- `query`: 搜索查询
- `max_results`: 最大返回结果数
- `language`: 编程语言筛选，可选

#### recommend() - 推荐
- `context`: 上下文描述
- `num_recommendations`: 推荐数量

**示例**:
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
```

**使用示例**:
```bash
python coding_plan/example.py search
python coding_plan/example.py recommend
```

---

## 🚀 快速开始

### 方式一：设置环境变量

```bash
export MINIMAX_API_KEY="your_api_key"
```

### 方式二：在代码中传入

```python
API_KEY = "your_api_key"
client = Music26(api_key=API_KEY)
```

### 运行所有测试

```bash
# 音乐生成
python music_generation/example.py all

# 图像生成
python image_generation/example.py all

# 编码计划
python coding_plan/example.py all
```

---

## 📋 API 端点总结

| 模块 | 功能 | 端点 |
|------|------|------|
| music_generation | Music 2.6 | `/v1/music_generation` |
| music_generation | Music Cover | `/v1/music_cover` |
| music_generation | Lyrics Generation | `/v1/lyrics_generation` |
| image_generation | Image 01 | `/v1/image_generation` |
| coding_plan | Coding Plan VLM | `/v1/coding_plan_vlm` |
| coding_plan | Coding Plan Search | `/v1/coding_plan_search` |

---

## 🔧 通用参数说明

所有模块的通用参数：

- `timeout`: 请求超时时间，默认 30-60 秒
- `temperature`: 温度参数，控制生成随机性
- `max_tokens`: 最大生成 token 数

所有模块的统一错误处理：
- HTTP 错误
- 请求超时
- 网络错误
- JSON 解析错误

---

## 📝 注意事项

1. 所有 API 调用需要有效的 API Key
2. 部分功能可能需要额外的 GroupId 参数
3. 建议使用极速版（Highspeed/Turbo）以获得更快的响应速度
4. 详细的参数说明请参考各模块的 docstring

---

## 🐛 故障排除

如果遇到问题：

1. 检查 API Key 是否正确设置
2. 检查网络连接是否正常
3. 查看控制台输出的错误信息
4. 确认参数格式是否符合要求
5. 检查超时设置是否合理

---

## 📚 更多资源

- MiniMax 官方文档
- API 示例代码
- SDK 源代码

---

**版本**: 1.0.0  
**更新日期**: 2026-04-14  
**支持**: Python 3.6+
