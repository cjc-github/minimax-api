# text-generation 模块使用文档

## 概述

text-generation 模块提供 MiniMax 文本生成 API 的封装，支持多种模型版本。

## 支持的模型

| 模型 | 说明 | 输出速度 |
|------|------|----------|
| M2.7 | 开启模型的自我迭代 | ~60tps |
| M2.7-highspeed | 极速版，效果不变，更快更敏捷 | ~100tps |
| M2.5 | 顶尖性能与极致性价比 | ~60tps |
| M2.5-highspeed | 极速版，效果不变，更快更敏捷 | ~100tps |
| M2.1 | 强大多语言编程能力 | ~60tps |
| M2.1-highspeed | 极速版，效果不变，更快更敏捷 | ~100tps |
| M2 | 专为高效编码与 Agent 工作流而生 | - |

## 安装依赖

```bash
pip install requests
```

## 快速开始

### M2.7 模型使用示例

```python
from text_generation import M27

# 初始化客户端
client = M27(api_key="your_api_key")

# 调用生成
response = client.generate(
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ]
)

print(response)
```

### M2.7 极速版使用示例

```python
from text_generation import M27Highspeed

client = M27Highspeed(api_key="your_api_key")

response = client.generate(
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ],
    temperature=0.8  # 自定义温度参数
)

print(response)
```

### M2.5 模型使用示例

```python
from text_generation import M25

client = M25(api_key="your_api_key")

response = client.generate(
    messages=[
        {"role": "user", "content": "写一首关于春天的诗"}
    ],
    max_tokens=1024  # 控制输出长度
)

print(response)
```

### M2 模型使用示例（适合编程场景）

```python
from text_generation import M2

client = M2(api_key="your_api_key")

response = client.generate(
    messages=[
        {"role": "user", "content": "用 Python 写一个快速排序算法"}
    ],
    max_tokens=2048
)

print(response)
```

## API 参考

### M27 类

```python
class M27:
    def __init__(self, api_key: str)
    
    def generate(
        self,
        messages: List[Dict[str, str]],
        model: str = "MiniMax-M2.7",
        max_tokens: int = 2048,
        temperature: float = 0.7,
        top_p: float = 0.95,
        timeout: int = 30
    ) -> Dict[str, Any]
```

#### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| messages | List[Dict] | - | 消息列表，格式为 [{"role": "user/assistant", "content": "内容"}] |
| model | str | "MiniMax-M2.7" | 模型名称 |
| max_tokens | int | 2048 | 最大生成 token 数 |
| temperature | float | 0.7 | 温度参数，控制生成随机性 |
| top_p | float | 0.95 | top_p 采样参数 |
| timeout | int | 30 | 请求超时时间（秒） |

#### 返回值

返回 JSON 格式的响应，包含生成文本内容。

---

### 其他模型类

其他模型类（M27Highspeed, M25, M25Highspeed, M21, M21Highspeed, M2）的 API 与 M27 相同，仅默认模型不同。

## 错误处理

```python
from text_generation import M27

client = M27(api_key="your_api_key")

try:
    response = client.generate(
        messages=[{"role": "user", "content": "你好"}],
        timeout=10
    )
    print(response)
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")