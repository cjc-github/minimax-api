# MiniMax API Python SDK

基于 MiniMax 官方文档封装的 Python SDK，支持文本生成和语音合成功能。

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

## 文档

- [文本生成模块文档](text-generation/README.md)
- [语音合成模块文档](text-to-speech/README.md)

## 获取 API Key

1. 登录 [MiniMax 开放平台](https://platform.minimaxi.com)
2. 进入「接口密钥」页面
3. 创建 Token Plan Key 或按量付费 API Key
4. 参考官方文档：https://platform.minimaxi.com/docs/api-reference/api-overview