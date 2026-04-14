import os
import sys
import base64
import requests
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from music_generation import Music26, Music26Free, MusicCover, MusicCoverFree, LyricsGeneration, LyricsGenerationHighspeed


API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")
OUTPUT_DIR = os.path.join(current_dir, "output")


def ensure_output_dir():
    """确保输出目录存在"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"创建输出目录: {OUTPUT_DIR}")


def save_lyrics_to_file(lyrics_content: str, filename: str = None) -> str:
    """
    将歌词保存到文本文件

    Args:
        lyrics_content: 歌词内容
        filename: 文件名（可选），如果不提供则自动生成

    Returns:
        保存的文件路径
    """
    ensure_output_dir()

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"lyrics_{timestamp}.txt"

    file_path = os.path.join(OUTPUT_DIR, filename)

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(lyrics_content)
        print(f"歌词已保存到: {file_path}")
        return file_path
    except Exception as e:
        print(f"保存歌词失败: {e}")
        return None


def save_audio_to_file(audio_data, filename: str = None) -> str:
    """
    将音频数据保存到文件

    Args:
        audio_data: API返回的音频数据（可能是dict、str或其他类型）
        filename: 文件名（可选），如果不提供则自动生成

    Returns:
        保存的文件路径
    """
    ensure_output_dir()

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"music_{timestamp}.mp3"

    file_path = os.path.join(OUTPUT_DIR, filename)

    try:
        # 尝试提取base64编码的音频数据
        b64_audio = None
        
        if isinstance(audio_data, dict):
            # 尝试不同的字段名
            for key in ["audio_file", "audio", "data"]:
                value = audio_data.get(key)
                if value:
                    if isinstance(value, dict):
                        # 嵌套字典，再次尝试提取
                        for nested_key in ["audio_file", "audio", "data"]:
                            nested_value = value.get(nested_key)
                            if nested_value:
                                b64_audio = nested_value
                                break
                    else:
                        b64_audio = value
                        break
        elif isinstance(audio_data, str):
            b64_audio = audio_data
        else:
            b64_audio = str(audio_data)

        if not b64_audio:
            print(f"警告: 未能从响应中提取音频数据")
            print(f"数据类型: {type(audio_data)}")
            print(f"数据内容: {str(audio_data)[:200]}")
            return None

        # 清理base64字符串（移除可能的空白字符）
        b64_audio = b64_audio.strip()

        # 判断数据编码格式并解码
        try:
            # 检测是否为 hex 编码（仅包含 0-9a-fA-F）
            import re
            if re.fullmatch(r'[0-9a-fA-F]+', b64_audio) and len(b64_audio) % 2 == 0:
                # 尝试 hex 解码并检查是否为有效音频（ID3/MPEG 帧头）
                test_bytes = bytes.fromhex(b64_audio[:8])
                if test_bytes[:3] == b'ID3' or test_bytes[0] == 0xFF:
                    print("检测到 hex 编码的音频数据，使用 hex 解码")
                    audio_bytes = bytes.fromhex(b64_audio)
                else:
                    audio_bytes = base64.b64decode(b64_audio)
            else:
                audio_bytes = base64.b64decode(b64_audio)
        except Exception as decode_error:
            # 如果是padding错误，尝试修复
            if "Incorrect padding" in str(decode_error):
                print(f"警告: Base64 padding 不正确，尝试修复...")
                # 添加缺失的padding
                padding_needed = 4 - (len(b64_audio) % 4)
                if padding_needed != 4:
                    b64_audio += "=" * padding_needed
                try:
                    audio_bytes = base64.b64decode(b64_audio)
                except:
                    print(f"警告: Base64修复失败，尝试直接保存原始数据")
                    audio_bytes = b64_audio.encode('utf-8')
            else:
                print(f"警告: Base64解码失败: {decode_error}，尝试直接保存原始数据")
                audio_bytes = b64_audio.encode('utf-8')

        # 保存文件
        with open(file_path, 'wb') as f:
            f.write(audio_bytes)

        print(f"音频已保存到: {file_path}")
        print(f"文件大小: {len(audio_bytes) / 1024:.2f} KB")
        return file_path

    except Exception as e:
        print(f"保存音频失败: {e}")
        import traceback
        print(f"详细错误: {traceback.format_exc()}")
        return None


def save_image_to_file(image_data, filename: str = None) -> str:
    """
    将图片数据保存到文件

    Args:
        image_data: API返回的图片数据（可能是dict、str或其他类型）
        filename: 文件名（可选），如果不提供则自动生成

    Returns:
        保存的文件路径
    """
    ensure_output_dir()

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cover_{timestamp}.png"

    file_path = os.path.join(OUTPUT_DIR, filename)

    try:
        # 尝试提取base64编码的图片数据
        b64_image = None
        
        if isinstance(image_data, dict):
            # 尝试不同的字段名
            for key in ["image_url", "image_file", "image", "data"]:
                value = image_data.get(key)
                if value:
                    if isinstance(value, dict):
                        # 嵌套字典，再次尝试提取
                        for nested_key in ["image_url", "image_file", "image", "data"]:
                            nested_value = value.get(nested_key)
                            if nested_value:
                                b64_image = nested_value
                                break
                    else:
                        b64_image = value
                        break
        elif isinstance(image_data, str):
            b64_image = image_data
        else:
            b64_image = str(image_data)

        if not b64_image:
            print(f"警告: 未能从响应中提取图片数据")
            print(f"数据类型: {type(image_data)}")
            print(f"数据内容: {str(image_data)[:200]}")
            return None

        # 清理base64字符串（移除可能的空白字符）
        b64_image = b64_image.strip()

        # 检查是否是URL格式
        if b64_image.startswith("http://") or b64_image.startswith("https://"):
            print(f"图片为URL格式，直接保存URL文本")
            image_bytes = b64_image.encode('utf-8')
        else:
            # 尝试解码base64，如果失败则保存原始数据
            try:
                image_bytes = base64.b64decode(b64_image)
            except Exception as decode_error:
                # 如果是padding错误，尝试修复
                if "Incorrect padding" in str(decode_error):
                    print(f"警告: Base64 padding 不正确，尝试修复...")
                    # 添加缺失的padding
                    padding_needed = 4 - (len(b64_image) % 4)
                    if padding_needed != 4:
                        b64_image += "=" * padding_needed
                    try:
                        image_bytes = base64.b64decode(b64_image)
                    except:
                        print(f"警告: Base64修复失败，尝试直接保存原始数据")
                        image_bytes = b64_image.encode('utf-8')
                else:
                    print(f"警告: Base64解码失败: {decode_error}，尝试直接保存原始数据")
                    image_bytes = b64_image.encode('utf-8')

        # 保存文件
        with open(file_path, 'wb') as f:
            f.write(image_bytes)

        print(f"封面已保存到: {file_path}")
        print(f"文件大小: {len(image_bytes) / 1024:.2f} KB")
        return file_path

    except Exception as e:
        print(f"保存封面失败: {e}")
        import traceback
        print(f"详细错误: {traceback.format_exc()}")
        return None


def parse_response(response: dict) -> dict:
    """解析 API 响应，统一返回格式"""
    if not response:
        return {"success": False, "error": "无响应", "content": None}

    base_resp = response.get("base_resp")

    if base_resp:
        status_code = base_resp.get("status_code", 0)
        status_msg = base_resp.get("status_msg", "")
        if status_code == 0 and status_msg == "success":
            content = response.get("data", response)
            return {
                "success": True,
                "content": content,
                "raw": response,
            }
        elif status_code != 0:
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


def test_music_26(save: bool = True):
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Music 2.6 音乐生成")
    print("=" * 50)

    try:
        client = Music26(api_key=API_KEY)
        response = client.generate(
            prompt="一首欢快的流行歌曲，副歌部分朗朗上口",
            lyrics="啦啦啦啦 快乐的心情\n啦啦啦啦 美好的时光\n让我们一起唱歌\n开心每一天",
            style="pop",
            tags=["happy", "upbeat", "dance"],
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功!")
            if save:
                save_audio_to_file(result["content"], "music_26_demo.mp3")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_music_26_free(save: bool = True):
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Music 2.6 Free 音乐生成")
    print("=" * 50)

    try:
        client = Music26Free(api_key=API_KEY)
        response = client.generate(
            prompt="一首抒情的民谣歌曲",
            lyrics="月光照在小路上\n风吹过稻田香\n远方的人在何方\n思念随风飘向远方",
            duration=180,
            style="folk",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功!")
            if save:
                save_audio_to_file(result["content"], "music_26_free_demo.mp3")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def load_audio_as_base64(file_path: str) -> str:
    """
    读取本地音频文件并返回 base64 编码

    Args:
        file_path: 音频文件路径

    Returns:
        base64 编码的字符串
    """
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def find_test_audio() -> str:
    """
    查找可用的测试音频文件

    优先顺序：
    1. 环境变量 MINIMAX_TEST_AUDIO 指定的路径
    2. output 目录下的 mp3 文件
    3. 项目中其他 mp3 文件

    Returns:
        音频文件路径，找不到则返回空字符串
    """
    # 1. 环境变量
    env_path = os.environ.get("MINIMAX_TEST_AUDIO", "")
    if env_path and os.path.isfile(env_path):
        return env_path

    # 2. output 目录
    if os.path.isdir(OUTPUT_DIR):
        for f in os.listdir(OUTPUT_DIR):
            if f.endswith((".mp3", ".wav", ".flac", ".m4a")):
                return os.path.join(OUTPUT_DIR, f)

    # 3. 项目中其他 mp3 (text_to_speech/output 等)
    for root, _dirs, files in os.walk(project_root):
        for f in files:
            if f.endswith((".mp3", ".wav")):
                return os.path.join(root, f)

    return ""


def test_music_cover(save: bool = True):
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Music Cover 音乐翻唱")
    print("=" * 50)

    audio_path = find_test_audio()
    if not audio_path:
        print("错误: 找不到测试音频文件")
        print("请通过以下方式提供:")
        print("  1. 设置环境变量 MINIMAX_TEST_AUDIO=/path/to/audio.mp3")
        print("  2. 将音频文件放到 output/ 目录")
        print()
        return

    print(f"使用测试音频: {audio_path}")

    try:
        audio_b64 = load_audio_as_base64(audio_path)
        print(f"音频 base64 编码完成 (长度: {len(audio_b64)})")

        client = MusicCover(api_key=API_KEY)
        response = client.generate(
            audio_base64=audio_b64,
            prompt="音乐风格：爵士蓝调，氛围：夜晚酒吧",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功!")
            if save:
                save_audio_to_file(result["content"], "music_cover_demo.mp3")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_music_cover_free(save: bool = True):
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Music Cover Free 音乐翻唱")
    print("=" * 50)

    audio_path = find_test_audio()
    if not audio_path:
        print("错误: 找不到测试音频文件")
        print("请通过以下方式提供:")
        print("  1. 设置环境变量 MINIMAX_TEST_AUDIO=/path/to/audio.mp3")
        print("  2. 将音频文件放到 output/ 目录")
        print()
        return

    print(f"使用测试音频: {audio_path}")

    try:
        audio_b64 = load_audio_as_base64(audio_path)
        print(f"音频 base64 编码完成 (长度: {len(audio_b64)})")

        client = MusicCoverFree(api_key=API_KEY)
        response = client.generate(
            audio_base64=audio_b64,
            prompt="音乐风格：流行摇滚，氛围：热情奔放",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功!")
            if save:
                save_audio_to_file(result["content"], "music_cover_free_demo.mp3")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_lyrics_generation(save: bool = True):
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Lyrics Generation 歌词生成")
    print("=" * 50)

    try:
        client = LyricsGeneration(api_key=API_KEY)
        response = client.generate(
            mode="write_full_song",
            prompt="一首关于夏日海边的轻快情歌",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])

            if save:
                lyrics_content = result["content"]
                if isinstance(lyrics_content, dict):
                    lyrics_text = lyrics_content.get("lyrics", str(lyrics_content))
                else:
                    lyrics_text = str(lyrics_content)
                save_lyrics_to_file(lyrics_text, "lyrics_summer_beach.txt")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_lyrics_generation_highspeed(save: bool = True):
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Lyrics Generation Highspeed 极速版")
    print("=" * 50)

    try:
        client = LyricsGenerationHighspeed(api_key=API_KEY)
        response = client.generate(
            mode="edit",
            prompt="将歌词改为更加欢快的风格",
        )

        result = parse_response(response)
        if result["success"]:
            print("生成成功:")
            print(result["content"])

            if save:
                lyrics_content = result["content"]
                if isinstance(lyrics_content, dict):
                    lyrics_text = lyrics_content.get("lyrics", str(lyrics_content))
                else:
                    lyrics_text = str(lyrics_content)
                save_lyrics_to_file(lyrics_text, "lyrics_edited.txt")
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
    print("  music-26-free     - 测试 Music 2.6 Free")
    print("  music-cover       - 测试 Music Cover 音乐翻唱")
    print("  music-cover-free  - 测试 Music Cover Free 音乐翻唱")
    print("  lyrics            - 测试 Lyrics Generation")
    print("  lyrics-hs         - 测试 Lyrics Generation Highspeed")
    print("  all               - 运行所有测试")
    print("  -l, --list        - 列出所有测试")
    print("  -h, --help        - 显示帮助")
    print()
    print("保存说明:")
    print("  音频文件: output/music_*.mp3")
    print("  翻唱文件: output/music_cover_*.mp3")
    print("  歌词文件: output/lyrics_*.txt")
    print()
    print("环境变量:")
    print("  MINIMAX_API_KEY   - 你的 API Key")
    print("  MINIMAX_TEST_AUDIO - 测试音频文件路径（music-cover 使用）")
    print()
    print("示例:")
    print("  export MINIMAX_API_KEY='your_key'")
    print("  python example.py music-26            # 生成音乐")
    print("  python example.py music-cover         # 音乐翻唱（需先有音频文件）")
    print("  python example.py lyrics              # 生成歌词")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="MiniMax 音乐生成 API 示例")
    parser.add_argument("test", nargs="?", help="运行特定测试")
    parser.add_argument("-l", "--list", action="store_true", help="列出所有测试")

    args = parser.parse_args()

    if args.list:
        print("可用测试:")
        print("  music-26          - 测试 Music 2.6")
        print("  music-26-free     - 测试 Music 2.6 Free")
        print("  music-cover       - 测试 Music Cover 音乐翻唱")
        print("  music-cover-free  - 测试 Music Cover Free 音乐翻唱")
        print("  lyrics            - 测试 Lyrics Generation")
        print("  lyrics-hs         - 测试 Lyrics Generation Highspeed")
        print("  all               - 运行所有测试")
        return

    if args.test == "music-26":
        test_music_26(save=True)
    elif args.test == "music-26-free":
        test_music_26_free(save=True)
    elif args.test == "music-cover":
        test_music_cover(save=True)
    elif args.test == "music-cover-free":
        test_music_cover_free(save=True)
    elif args.test == "lyrics":
        test_lyrics_generation(save=True)
    elif args.test == "lyrics-hs":
        test_lyrics_generation_highspeed(save=True)
    elif args.test == "all":
        test_music_26(save=True)
        test_music_26_free(save=True)
        test_music_cover(save=True)
        test_music_cover_free(save=True)
        test_lyrics_generation(save=True)
        test_lyrics_generation_highspeed(save=True)
    else:
        show_help()


if __name__ == "__main__":
    main()
