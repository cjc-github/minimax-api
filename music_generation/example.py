import os
import sys
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from music_generation import Music26, Music26Highspeed, MusicCover, LyricsGeneration, LyricsGenerationHighspeed


API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")


def parse_response(response: dict) -> dict:
    """解析 API 响应，统一返回格式"""
    if not response:
        return {"success": False, "error": "无响应", "content": None}

    base_resp = response.get("base_resp")

    if base_resp:
        status_code = base_resp.get("status_code", 0)
        status_msg = base_resp.get("status_msg", "未知错误")
        return {
            "success": False,
            "error": f"API 错误 ({status_code}): {status_msg}",
            "content": None,
        }

    content = response.get("data", response)
    return {
        "success": True,
        "content": content,
        "raw": response,
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


def test_music_26():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Music 2.6 音乐生成")
    print("=" * 50)

    try:
        client = Music26(api_key=API_KEY)
        response = client.generate(
            prompt="一首欢快的流行歌曲，副歌部分朗朗上口",
            style="pop",
            tags=["happy", "upbeat", "dance"],
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_music_26_highspeed():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Music 2.6 Highspeed 极速版")
    print("=" * 50)

    try:
        client = Music26Highspeed(api_key=API_KEY)
        response = client.generate(
            prompt="一首抒情的民谣歌曲",
            duration=180,
            style="folk",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_music_cover():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Music Cover 封面生成")
    print("=" * 50)

    try:
        client = MusicCover(api_key=API_KEY)
        response = client.generate(
            music_url="https://example.com/music.mp3",
            prompt="音乐风格：爵士蓝调，氛围：夜晚酒吧",
            resolution="2k",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_lyrics_generation():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Lyrics Generation 歌词生成")
    print("=" * 50)

    try:
        client = LyricsGeneration(api_key=API_KEY)
        response = client.generate(
            prompt="关于追逐梦想的励志歌词",
            genre="pop",
            theme="奋斗",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_lyrics_generation_highspeed():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Lyrics Generation Highspeed 极速版")
    print("=" * 50)

    try:
        client = LyricsGenerationHighspeed(api_key=API_KEY)
        response = client.generate(
            prompt="关于爱情的抒情歌词",
            genre="ballad",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def show_help():
    print("MiniMax 音乐生成 API 示例")
    print("=" * 50)
    print("用法: python example.py [选项]")
    print()
    print("选项:")
    print("  music-26          - 测试 Music 2.6")
    print("  music-26-hs       - 测试 Music 2.6 Highspeed")
    print("  music-cover       - 测试 Music Cover")
    print("  lyrics            - 测试 Lyrics Generation")
    print("  lyrics-hs         - 测试 Lyrics Generation Highspeed")
    print("  all               - 运行所有测试")
    print("  -l, --list        - 列出所有测试")
    print("  -h, --help        - 显示帮助")
    print()
    print("环境变量:")
    print("  MINIMAX_API_KEY - 你的 API Key")
    print()
    print("示例:")
    print("  export MINIMAX_API_KEY='your_key'")
    print("  python example.py music-26")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="MiniMax 音乐生成 API 示例")
    parser.add_argument("test", nargs="?", help="运行特定测试")
    parser.add_argument("-l", "--list", action="store_true", help="列出所有测试")

    args = parser.parse_args()

    if args.list:
        print("可用测试:")
        print("  music-26          - 测试 Music 2.6")
        print("  music-26-hs       - 测试 Music 2.6 Highspeed")
        print("  music-cover       - 测试 Music Cover")
        print("  lyrics            - 测试 Lyrics Generation")
        print("  lyrics-hs         - 测试 Lyrics Generation Highspeed")
        print("  all               - 运行所有测试")
        return

    if args.test == "music-26":
        test_music_26()
    elif args.test == "music-26-hs":
        test_music_26_highspeed()
    elif args.test == "music-cover":
        test_music_cover()
    elif args.test == "lyrics":
        test_lyrics_generation()
    elif args.test == "lyrics-hs":
        test_lyrics_generation_highspeed()
    elif args.test == "all":
        test_music_26()
        test_music_26_highspeed()
        test_music_cover()
        test_lyrics_generation()
        test_lyrics_generation_highspeed()
    else:
        show_help()


if __name__ == "__main__":
    main()
