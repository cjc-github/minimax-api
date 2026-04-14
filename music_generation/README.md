# 音乐生成模块 (music_generation)

基于 MiniMax API 的音乐生成模块，支持音乐创作、歌词生成和音乐封面生成。

## 功能说明

### 1. Music 2.6 音乐生成

**类**: `Music26`, `Music26Highspeed`

**功能**: 根据歌词和提示词生成完整的音乐作品

**主要参数**:
- `prompt`: 音乐描述提示词
- `lyrics`: 歌词内容（**必需参数**）
- `duration`: 音乐时长（秒），可选
- `style`: 音乐风格（如 "pop", "rock", "jazz"），可选
- `tags`: 音乐标签列表，可选
- `output_token_limit`: 输出 token 限制

**使用示例**:
```python
from music_generation import Music26

client = Music26(api_key="your_api_key")
response = client.generate(
    prompt="一首欢快的流行歌曲，副歌部分朗朗上口",
    lyrics="啦啦啦啦 快乐的心情\n啦啦啦啦 美好的时光\n让我们一起唱歌\n开心每一天",
    style="pop",
    tags=["happy", "upbeat", "dance"]
)
```

### 2. Music Cover 音乐翻唱

**类**: `MusicCover`, `MusicCoverFree`

**功能**: 基于已有音频生成音乐翻唱，返回翻唱后的音频文件

**前置条件**: 需要先准备一个音频文件（mp3/wav），可通过以下方式之一提供：
- 设置环境变量 `MINIMAX_TEST_AUDIO=/path/to/audio.mp3`
- 将音频文件放到 `output/` 目录
- 先运行 `python example.py music-26` 生成一个音频文件

**主要参数**:
- `audio_url`: 音乐文件的 URL 地址（与 `audio_base64` 二选一）
- `audio_base64`: 音乐文件的 base64 编码（与 `audio_url` 二选一）
- `cover_feature_id`: 封面特征 ID，可选
- `prompt`: 描述提示词，可选

**使用示例**:

#### 方式一：通过 audio_url
```python
from music_generation import MusicCover

client = MusicCover(api_key="your_api_key")
response = client.generate(
    audio_url="https://your-server.com/music.mp3",
    prompt="音乐风格：爵士蓝调，氛围：夜晚酒吧",
)
```

#### 方式二：通过本地文件 + audio_base64
```python
import base64
from music_generation import MusicCover

# 读取本地音频文件
with open("path/to/music.mp3", "rb") as f:
    audio_b64 = base64.b64encode(f.read()).decode("utf-8")

client = MusicCover(api_key="your_api_key")
response = client.generate(
    audio_base64=audio_b64,
    prompt="音乐风格：爵士蓝调，氛围：夜晚酒吧",
)
```

### 3. Lyrics Generation 歌词生成

**类**: `LyricsGeneration`, `LyricsGenerationHighspeed`

**功能**: 根据提示词生成完整的歌词内容，支持创作新歌词或编辑现有歌词

**主要参数**:
- `mode`: 生成模式（**必需参数**）
  - `"write_full_song"`: 创作完整的全新歌词
  - `"edit"`: 编辑或修改现有歌词
- `prompt`: 歌词描述或主题提示词（**必需参数**）
- `model`: 模型名称（可选）

**三种使用方式**:

#### 方式一：使用 generate() 方法
```python
from music_generation import LyricsGeneration

client = LyricsGeneration(api_key="your_api_key")

# 创作完整歌词
response = client.generate(
    mode="write_full_song",
    prompt="一首关于夏日海边的轻快情歌"
)

# 编辑歌词
response = client.generate(
    mode="edit",
    prompt="将歌词改为更加欢快的风格"
)
```

#### 方式二：使用快捷方法 write_full_song()
```python
from music_generation import LyricsGeneration

client = LyricsGeneration(api_key="your_api_key")
response = client.write_full_song(
    prompt="一首关于夏日海边的轻快情歌"
)
```

#### 方式三：使用快捷方法 edit()
```python
from music_generation import LyricsGeneration

client = LyricsGeneration(api_key="your_api_key")
response = client.edit(
    prompt="将歌词改为更加欢快的风格"
)
```

## 运行测试

### 测试 Music 2.6
```bash
python example.py music-26
```

### 测试 Music Cover 音乐翻唱

⚠️ **前置条件**: 需要先有一个可用的音频文件。

```bash
# 步骤 1: 先生成一个音频文件（如果 output/ 目录下还没有）
python example.py music-26

# 步骤 2: 运行翻唱测试（自动从 output/ 目录读取音频）
python example.py music-cover

# 或者指定音频文件路径
export MINIMAX_TEST_AUDIO=/path/to/your/music.mp3
python example.py music-cover
```

### 测试歌词生成
```bash
python example.py lyrics              # 标准版
python example.py lyrics-hs           # 极速版
```

### 运行所有测试
```bash
python example.py all
```

## 重要提示

### Music 2.6 - lyrics 参数必需
⚠️ **注意**: Music 2.6 API 的 `lyrics` 参数是**必需**的，不能为空或省略。

错误示例：
```python
# ❌ 错误 - 会返回 "lyrics is required" 错误
response = client.generate(prompt="欢快的歌曲")
```

正确示例：
```python
# ✅ 正确 - 包含必需的 lyrics 参数
response = client.generate(
    prompt="欢快的歌曲",
    lyrics="啦啦啦啦 快乐的心情\n啦啦啦啦 美好的时光"
)
```

### Lyrics Generation - mode 参数必需
⚠️ **注意**: Lyrics Generation API 的 `mode` 参数是**必需**的，用于指定生成模式。

可选值：
- `"write_full_song"`: 创作完整的全新歌词
- `"edit"`: 编辑或修改现有歌词

错误示例：
```python
# ❌ 错误 - 会返回缺少 mode 参数的错误
response = client.generate(prompt="一首情歌")
```

正确示例：
```python
# ✅ 正确 - 包含必需的 mode 参数
response = client.generate(
    mode="write_full_song",
    prompt="一首关于夏日海边的轻快情歌"
)
```

推荐使用快捷方法：
```python
# ✅ 使用快捷方法更简洁
response = client.write_full_song(prompt="一首关于夏日海边的轻快情歌")
```

## 响应处理

示例代码中包含 `parse_response()` 函数，可以统一处理 API 响应：

```python
def parse_response(response: dict) -> dict:
    """
    解析 API 响应，统一返回格式
    
    Returns:
        {
            "success": bool,      # 是否成功
            "content": any,       # 成功时的数据
            "error": str,        # 失败时的错误信息
            "raw": dict          # 原始响应
        }
    """
```

## 错误处理

代码包含完整的错误处理机制：

- HTTP 错误（状态码非 200）
- 请求超时
- 网络连接错误
- JSON 解析错误
- API 返回的业务错误

## 环境变量

```bash
export MINIMAX_API_KEY="your_api_key"

# 可选：指定 music-cover 测试使用的音频文件
export MINIMAX_TEST_AUDIO="/path/to/audio.mp3"
```

或者在代码中直接设置：
```python
API_KEY = "your_api_key"
```

## 依赖

- Python 3.6+
- requests >= 2.28.0

安装依赖：
```bash
pip install -r requirements.txt
```

## 官方API参考

```python
import requests

url = "https://api.minimaxi.com/v1/lyrics_generation"
payload = {
    "mode": "write_full_song",
    "prompt": "一首关于夏日海边的轻快情歌"
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <token>"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
```
