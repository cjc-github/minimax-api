import os
import sys
import json
import base64
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from text_to_speech import (
    Speech28HD, Speech28Turbo,
    Speech26HD, Speech26Turbo,
    Speech02HD, Speech02Turbo
)


API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")
OUTPUT_DIR = os.path.join(current_dir, "output")


def ensure_output_dir():
    """确保输出目录存在"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def save_audio(audio_data: str, filename: str, audio_format: str = "mp3") -> str:
    """
    保存音频数据到文件
    
    Args:
        audio_data: base64 编码的音频数据
        filename: 文件名（不含扩展名）
        audio_format: 音频格式
    
    Returns:
        保存的文件路径
    """
    ensure_output_dir()
    
    try:
        audio_bytes = base64.b64decode(audio_data)
        file_path = os.path.join(OUTPUT_DIR, f"{filename}.{audio_format}")
        
        with open(file_path, "wb") as f:
            f.write(audio_bytes)
        
        return file_path
    except Exception as e:
        print(f"保存音频失败: {e}")
        return ""


def parse_response(response: dict) -> dict:
    """解析 API 响应，统一返回格式"""
    if not response:
        return {"success": False, "error": "无响应", "data": None}
    
    base_resp = response.get("base_resp")
    data = response.get("data")
    
    if data:
        audio = data.get("audio")
        if audio:
            return {
                "success": True,
                "data": audio,
                "extra_info": data.get("extra_info"),
                "raw": response
            }
    
    if base_resp:
        status_code = base_resp.get("status_code", 0)
        status_msg = base_resp.get("status_msg", "未知错误")
        
        if status_code == 0:
            return {
                "success": False,
                "error": f"API 返回成功但无音频数据",
                "data": None
            }
        
        return {
            "success": False,
            "error": f"API 错误 ({status_code}): {status_msg}",
            "data": None
        }
    elif "error" in response:
        return {
            "success": False,
            "error": str(response["error"]),
            "data": None
        }
    else:
        return {
            "success": False,
            "error": "未知响应格式",
            "data": None
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


def test_speech_28_hd():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 Speech 2.8 HD 模型")
    print("=" * 50)
    
    try:
        client = Speech28HD(api_key=API_KEY)
        response = client.synthesize(
            text="你好，欢迎使用 MiniMax 语音合成服务。这是 Speech 2.8 HD 模型生成的语音。",
            voice_id="male-qn-qingse",
            speed=1.0,
            volume=1.0,
            pitch=0
        )
        
        result = parse_response(response)
        if result["success"]:
            print("合成成功!")
            audio_data = result.get("data", "")
            if audio_data:
                file_path = save_audio(audio_data, "speech_28_hd", "mp3")
                print(f"音频已保存到: {file_path}")
                print(f"文件大小: {os.path.getsize(file_path)} bytes")
            else:
                print("无音频数据")
        else:
            print(f"合成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_speech_28_turbo():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 Speech 2.8 Turbo 模型")
    print("=" * 50)
    
    try:
        client = Speech28Turbo(api_key=API_KEY)
        response = client.synthesize(
            text="这是 Speech 2.8 Turbo 模型，响应更灵敏。",
            voice_id="female-shaonv",
            speed=1.2
        )
        
        result = parse_response(response)
        if result["success"]:
            print("合成成功!")
            audio_data = result.get("data", "")
            if audio_data:
                file_path = save_audio(audio_data, "speech_28_turbo", "mp3")
                print(f"音频已保存到: {file_path}")
            else:
                print("无音频数据")
        else:
            print(f"合成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_speech_26_hd():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 Speech 2.6 HD 模型")
    print("=" * 50)
    
    try:
        client = Speech26HD(api_key=API_KEY)
        response = client.synthesize(
            text="这是 Speech 2.6 HD 模型，韵律表现出色。",
            voice_id="male-qn-qingse",
            audio_format="mp3",
            sample_rate=32000,
            bitrate=128000
        )
        
        result = parse_response(response)
        if result["success"]:
            print("合成成功!")
            audio_data = result.get("data", "")
            if audio_data:
                file_path = save_audio(audio_data, "speech_26_hd", "mp3")
                print(f"音频已保存到: {file_path}")
            else:
                print("无音频数据")
        else:
            print(f"合成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_speech_26_turbo():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 Speech 2.6 Turbo 模型")
    print("=" * 50)
    
    try:
        client = Speech26Turbo(api_key=API_KEY)
        response = client.synthesize(
            text="这是 Speech 2.6 Turbo 模型，超低时延。",
            voice_id="male-badao",
            speed=0.9
        )
        
        result = parse_response(response)
        if result["success"]:
            print("合成成功!")
            audio_data = result.get("data", "")
            if audio_data:
                file_path = save_audio(audio_data, "speech_26_hd", "mp3")
                print(f"音频已保存到: {file_path}")
            else:
                print("无音频数据")
        else:
            print(f"合成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_speech_02_hd():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 Speech 02 HD 模型")
    print("=" * 50)
    
    try:
        client = Speech02HD(api_key=API_KEY)
        response = client.synthesize(
            text="这是 Speech 02 HD 模型，稳定性好，音质突出。",
            voice_id="female-yujie",
            pitch=2
        )
        
        result = parse_response(response)
        if result["success"]:
            print("合成成功!")
            audio_data = result.get("data", "")
            if audio_data:
                file_path = save_audio(audio_data, "speech_26_hd", "mp3")
                print(f"音频已保存到: {file_path}")
            else:
                print("无音频数据")
        else:
            print(f"合成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_speech_02_turbo():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试 Speech 02 Turbo 模型")
    print("=" * 50)
    
    try:
        client = Speech02Turbo(api_key=API_KEY)
        response = client.synthesize(
            text="这是 Speech 02 Turbo 模型，小语种能力加强。",
            voice_id="female-tianmei",
            volume=1.5
        )
        
        result = parse_response(response)
        if result["success"]:
            print("合成成功!")
            audio_data = result.get("data", "")
            if audio_data:
                file_path = save_audio(audio_data, "speech_26_hd", "mp3")
                print(f"音频已保存到: {file_path}")
            else:
                print("无音频数据")
        else:
            print(f"合成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")
    
    print()


def test_different_formats():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试不同音频格式")
    print("=" * 50)
    
    try:
        client = Speech28HD(api_key=API_KEY)
    except Exception as e:
        print(f"错误: 初始化客户端失败 - {e}")
        return
    
    formats = ["mp3", "pcm", "flac", "wav"]
    
    for fmt in formats:
        print(f"测试格式: {fmt}")
        try:
            response = client.synthesize(
                text=f"这是 {fmt} 格式的音频",
                audio_format=fmt
            )
            result = parse_response(response)
            if result["success"]:
                print(f"  ✓ {fmt} 支持")
            else:
                print(f"  ✗ {fmt} 失败: {result['error']}")
        except Exception as e:
            print(f"  ✗ {fmt} 错误: {e}")
    print()


def test_voice_settings():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试不同音色设置")
    print("=" * 50)
    
    try:
        client = Speech28HD(api_key=API_KEY)
    except Exception as e:
        print(f"错误: 初始化客户端失败 - {e}")
        return
    
    voices = [
        "male-qn-qingse",
        "female-shaonv",
        "female-yujie",
        "male-badao",
        "female-tianmei"
    ]
    
    for voice in voices:
        print(f"测试音色: {voice}")
        try:
            response = client.synthesize(
                text=f"你好，我是 {voice} 音色",
                voice_id=voice
            )
            result = parse_response(response)
            if result["success"]:
                print(f"  ✓ 成功")
            else:
                print(f"  ✗ 失败: {result['error']}")
        except Exception as e:
            print(f"  ✗ 错误: {e}")
    print()


def test_multi_language():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("测试多语言支持")
    print("=" * 50)
    
    try:
        client = Speech28HD(api_key=API_KEY)
    except Exception as e:
        print(f"错误: 初始化客户端失败 - {e}")
        return
    
    languages = [
        ("中文", "你好，今天天气很好。"),
        ("英语", "Hello, how are you today?"),
        ("日语", "こんにちは、お元気ですか。"),
        ("韩语", "안녕하세요, 오늘天气很好。"),
    ]
    
    for lang, text in languages:
        print(f"测试语言: {lang}")
        try:
            response = client.synthesize(
                text=text,
                voice_id="male-qn-qingse"
            )
            result = parse_response(response)
            if result["success"]:
                print(f"  ✓ 成功")
            else:
                print(f"  ✗ 失败: {result['error']}")
        except Exception as e:
            print(f"  ✗ 错误: {e}")
    print()


def interactive_demo():
    if not check_api_key():
        return
    
    print("=" * 50)
    print("交互式语音合成演示")
    print("=" * 50)
    
    print("请选择模型:")
    print("1. Speech 2.8 HD")
    print("2. Speech 2.8 Turbo")
    print("3. Speech 2.6 HD")
    print("4. Speech 2.6 Turbo")
    print("5. Speech 02 HD")
    print("6. Speech 02 Turbo")
    
    choice = input("\n请输入选项 (1-6): ").strip()
    
    models = {
        "1": (Speech28HD, "speech-2.8-hd"),
        "2": (Speech28Turbo, "speech-2.8-turbo"),
        "3": (Speech26HD, "speech-2.6-hd"),
        "4": (Speech26Turbo, "speech-2.6-turbo"),
        "5": (Speech02HD, "speech-02-hd"),
        "6": (Speech02Turbo, "speech-02-turbo"),
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
    print("输入文本进行语音合成，输入 'quit' 退出\n")
    
    count = 0
    error_count = 0
    
    while True:
        text = input("输入文本: ").strip()
        
        if not text:
            print("输入不能为空，请重试")
            continue
        
        if text.lower() == "quit":
            break
        
        speed_input = input("语速 (0.5-2.0, 默认 1.0): ").strip()
        speed = float(speed_input) if speed_input else 1.0
        
        if not (0.5 <= speed <= 2.0):
            print("语速超出范围 (0.5-2.0)，使用默认值 1.0")
            speed = 1.0
        
        try:
            response = client.synthesize(text=text, speed=speed)
            result = parse_response(response)
            
            if result["success"]:
                print("✓ 合成成功!")
                audio_data = result.get("data", "")
                if audio_data:
                    filename = f"interactive_{count + 1}"
                    file_path = save_audio(audio_data, filename, "mp3")
                    print(f"音频已保存到: {file_path}")
                count += 1
                error_count = 0
            else:
                print(f"✗ 合成失败: {result['error']}")
                error_count += 1
                
                if error_count >= 3:
                    print("\n连续错误次数过多，请检查 API Key 和网络连接")
                    break
                    
        except requests.exceptions.Timeout:
            print("错误: 请求超时，请重试")
            error_count += 1
        except requests.exceptions.RequestException as e:
            print(f"错误: 网络请求失败 - {e}")
            error_count += 1
        except Exception as e:
            print(f"错误: {e}")
            error_count += 1
    
    print(f"\n演示结束，共合成 {count} 次")


def show_help():
    print("MiniMax 语音合成 API 示例")
    print("=" * 50)
    print("用法: python example.py [选项]")
    print()
    print("选项:")
    print("  interactive  - 交互式语音合成")
    print("  28-hd       - 测试 Speech 2.8 HD")
    print("  28-turbo    - 测试 Speech 2.8 Turbo")
    print("  26-hd       - 测试 Speech 2.6 HD")
    print("  26-turbo    - 测试 Speech 2.6 Turbo")
    print("  02-hd       - 测试 Speech 02 HD")
    print("  02-turbo    - 测试 Speech 02 Turbo")
    print("  formats     - 测试不同音频格式")
    print("  voices      - 测试不同音色")
    print("  languages   - 测试多语言支持")
    print("  -h, --help  - 显示帮助")
    print()
    print("环境变量:")
    print("  MINIMAX_API_KEY - 你的 API Key")
    print()
    print("示例:")
    print("  export MINIMAX_API_KEY='your_key'")
    print("  python example.py 28-hd")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ["-h", "--help"]:
            show_help()
        elif arg == "interactive":
            interactive_demo()
        elif arg == "28-hd":
            test_speech_28_hd()
        elif arg == "28-turbo":
            test_speech_28_turbo()
        elif arg == "26-hd":
            test_speech_26_hd()
        elif arg == "26-turbo":
            test_speech_26_turbo()
        elif arg == "02-hd":
            test_speech_02_hd()
        elif arg == "02-turbo":
            test_speech_02_turbo()
        elif arg == "formats":
            test_different_formats()
        elif arg == "voices":
            test_voice_settings()
        elif arg == "languages":
            test_multi_language()
        else:
            print(f"错误: 未知选项 '{arg}'")
            print("使用 python example.py --help 查看帮助")
    else:
        show_help()