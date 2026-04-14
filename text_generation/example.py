import os
import sys
import json
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from text_generation import M27, M27Highspeed, M25, M25Highspeed, M21, M21Highspeed, M2


API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")


def parse_response(response: dict) -> dict:
    """解析 API 响应，统一返回格式"""
    if not response:
        return {"success": False, "error": "无响应", "content": None}
    
    choices = response.get("choices")
    base_resp = response.get("base_resp")
    
    if choices is not None and len(choices) > 0:
        content = response["choices"][0].get("message", {}).get("content", "")
        usage = response.get("usage", {})
        return {
            "success": True,
            "content": content,
            "usage": usage,
            "raw": response
        }
    elif base_resp:
        status_code = base_resp.get("status_code", 0)
        status_msg = base_resp.get("status_msg", "未知错误")
        return {
            "success": False,
            "error": f"API 错误 ({status_code}): {status_msg}",
            "content": None
        }
    elif "error" in response:
        return {
            "success": False,
            "error": str(response["error"]),
            "content": None
        }
    else:
        return {
            "success": False,
            "error": "未知响应格式",
            "content": None
        }


def check_api_key() -> bool:
    """检查 API Key 是否有效"""
    if API_KEY == "your_api_key_here" or not API_KEY:
        print("错误: 请设置有效的 API Key")
        print("方式一: 设置环境变量")
        print("  export MINIMAX_API_KEY='your_api_key'")
        print("方式二: 修改 example.py 中的 API_KEY 变量")
        return False
    return True


def test_m27():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 M2.7 模型")
    print("=" * 50)
    
    try:
        client = M27(api_key=API_KEY)
        response = client.generate(
            messages=[{"role": "user", "content": "你好，请介绍一下你自己"}]
        )
        
        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
            print(f"\n使用量: {result['usage']}")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_m27_highspeed():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 M2.7-highspeed 模型")
    print("=" * 50)
    
    try:
        client = M27Highspeed(api_key=API_KEY)
        response = client.generate(
            messages=[{"role": "user", "content": "写一首关于春天的诗"}],
            temperature=0.8
        )
        
        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
            print(f"\n使用量: {result['usage']}")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_m25():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 M2.5 模型")
    print("=" * 50)
    
    try:
        client = M25(api_key=API_KEY)
        response = client.generate(
            messages=[{"role": "user", "content": "用一句话解释什么是人工智能"}],
            max_tokens=500
        )
        
        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
            print(f"\n使用量: {result['usage']}")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_m25_highspeed():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 M2.5-highspeed 模型")
    print("=" * 50)
    
    try:
        client = M25Highspeed(api_key=API_KEY)
        response = client.generate(
            messages=[{"role": "user", "content": "你好"}],
            temperature=0.5,
            top_p=0.9
        )
        
        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
            print(f"\n使用量: {result['usage']}")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_m21():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 M2.1 模型（适合编程）")
    print("=" * 50)
    
    try:
        client = M21(api_key=API_KEY)
        response = client.generate(
            messages=[{"role": "user", "content": "用 Python 写一个计算斐波那契数列的函数"}],
            max_tokens=1024
        )
        
        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
            print(f"\n使用量: {result['usage']}")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_m21_highspeed():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 M2.1-highspeed 模型")
    print("=" * 50)
    
    try:
        client = M21Highspeed(api_key=API_KEY)
        response = client.generate(
            messages=[{"role": "user", "content": "解释一下什么是回调函数"}]
        )
        
        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
            print(f"\n使用量: {result['usage']}")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_m2():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 M2 模型（专为高效编码与 Agent 工作流）")
    print("=" * 50)
    
    try:
        client = M2(api_key=API_KEY)
        response = client.generate(
            messages=[{"role": "user", "content": "写一个二分查找算法的 Python 代码"}],
            max_tokens=2048
        )
        
        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
            print(f"\n使用量: {result['usage']}")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def interactive_demo():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("交互式对话演示")
    print("=" * 50)
    
    print("请选择模型:")
    print("1. M2.7 (标准版)")
    print("2. M2.7-highspeed (极速版)")
    print("3. M2.5 (标准版)")
    print("4. M2.5-highspeed (极速版)")
    print("5. M2.1 (标准版)")
    print("6. M2.1-highspeed (极速版)")
    print("7. M2 (编程专用)")
    
    choice = input("\n请输入选项 (1-7): ").strip()
    
    models = {
        "1": (M27, "MiniMax-M2.7"),
        "2": (M27Highspeed, "MiniMax-M2.7-highspeed"),
        "3": (M25, "MiniMax-M2.5"),
        "4": (M25Highspeed, "MiniMax-M2.5-highspeed"),
        "5": (M21, "MiniMax-M2.1"),
        "6": (M21Highspeed, "MiniMax-M2.1-highspeed"),
        "7": (M2, "MiniMax-M2"),
    }
    
    if choice not in models:
        print("错误: 无效选项")
        return
    
    model_class, model_name = models[choice]
    
    try:
        client = model_class(api_key=API_KEY)
    except Exception as e:
        print(f"错误: 初始化客户端失败 - {e}")
        return
    
    print(f"\n使用模型: {model_name}")
    print("输入 'quit' 退出对话\n")
    
    messages = []
    error_count = 0
    
    while True:
        user_input = input("用户: ").strip()
        
        if not user_input:
            print("输入不能为空，请重试")
            continue
        
        if user_input.lower() == "quit":
            break
        
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = client.generate(messages=messages)
            result = parse_response(response)
            
            if result["success"]:
                content = result["content"]
                messages.append({"role": "assistant", "content": content})
                print(f"助手: {content}")
                error_count = 0
            else:
                print(f"错误: {result['error']}")
                messages.pop()
                error_count += 1
                
                if error_count >= 3:
                    print("\n连续错误次数过多，请检查 API Key 和网络连接")
                    break
                    
        except requests.exceptions.Timeout:
            print("错误: 请求超时，请重试")
            messages.pop()
        except requests.exceptions.RequestException as e:
            print(f"错误: 网络请求失败 - {e}")
            messages.pop()
        except Exception as e:
            print(f"错误: {e}")
            messages.pop()
    
    print(f"\n对话结束，共对话 {len(messages)} 轮")


def show_help():
    print("MiniMax 文本生成 API 示例")
    print("=" * 50)
    print("用法: python example.py [选项]")
    print()
    print("选项:")
    print("  interactive  - 交互式对话")
    print("  m27          - 测试 M2.7 模型")
    print("  m27-hs       - 测试 M2.7-highspeed 模型")
    print("  m25          - 测试 M2.5 模型")
    print("  m25-hs       - 测试 M2.5-highspeed 模型")
    print("  m21          - 测试 M2.1 模型")
    print("  m21-hs       - 测试 M2.1-highspeed 模型")
    print("  m2           - 测试 M2 模型")
    print("  -h, --help   - 显示帮助")
    print()
    print("环境变量:")
    print("  MINIMAX_API_KEY - 你的 API Key")
    print()
    print("示例:")
    print("  export MINIMAX_API_KEY='your_key'")
    print("  python example.py m27")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ["-h", "--help"]:
            show_help()
        elif arg == "interactive":
            interactive_demo()
        elif arg == "m27":
            test_m27()
        elif arg == "m27-hs":
            test_m27_highspeed()
        elif arg == "m25":
            test_m25()
        elif arg == "m25-hs":
            test_m25_highspeed()
        elif arg == "m21":
            test_m21()
        elif arg == "m21-hs":
            test_m21_highspeed()
        elif arg == "m2":
            test_m2()
        else:
            print(f"错误: 未知选项 '{arg}'")
            print("使用 python example.py --help 查看帮助")
    else:
        show_help()