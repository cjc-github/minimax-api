import os
import sys
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from image_generation import Image01, Image01Turbo


API_KEY = os.environ.get("MINIMAX_API_KEY", "your_api_key_here")
OUTPUT_DIR = os.path.join(current_dir, "output")
REFERENCE_IMAGE_URL = "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=1024&q=80"


def ensure_output_dir():
    """确保输出目录存在"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def infer_extension(content_type: str, image_url: str) -> str:
    """根据响应头或 URL 推断图片扩展名"""
    content_type = (content_type or "").lower()
    if "png" in content_type:
        return ".png"
    if "webp" in content_type:
        return ".webp"
    if "jpeg" in content_type or "jpg" in content_type:
        return ".jpg"

    clean_url = image_url.split("?", 1)[0].lower()
    for suffix in (".png", ".webp", ".jpg", ".jpeg"):
        if clean_url.endswith(suffix):
            return suffix

    return ".png"


def save_image(image_url: str, filename: str, timeout: int = 60) -> str:
    """下载并保存单张图片"""
    ensure_output_dir()

    try:
        response = requests.get(image_url, timeout=timeout)
        response.raise_for_status()
        extension = infer_extension(response.headers.get("Content-Type", ""), image_url)
        file_path = os.path.join(OUTPUT_DIR, f"{filename}{extension}")
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    except requests.exceptions.RequestException as e:
        print(f"保存图片失败: {e}")
        return ""
    except Exception as e:
        print(f"保存图片失败: {e}")
        return ""


def save_images(image_urls: list, prefix: str) -> list:
    """下载并保存多张图片"""
    saved_paths = []

    for index, image_url in enumerate(image_urls, start=1):
        file_path = save_image(image_url, f"{prefix}_{index}")
        if file_path:
            saved_paths.append(file_path)

    return saved_paths


def parse_response(response: dict) -> dict:
    """解析 API 响应，统一返回格式"""
    if not response:
        return {"success": False, "error": "无响应", "content": None}

    base_resp = response.get("base_resp") or {}
    status_code = base_resp.get("status_code")
    status_msg = base_resp.get("status_msg", "")
    data = response.get("data") or {}
    image_urls = data.get("image_urls")

    if image_urls:
        return {
            "success": True,
            "content": image_urls,
            "raw": response,
        }

    if "error" in response:
        return {
            "success": False,
            "error": str(response["error"]),
            "content": None,
        }

    if base_resp and status_code not in (None, 0):
        return {
            "success": False,
            "error": f"API 错误 ({status_code}): {status_msg or '未知错误'}",
            "content": None,
        }

    if base_resp and status_msg and status_msg.lower() != "success":
        return {
            "success": False,
            "error": f"API 错误 ({status_code or 0}): {status_msg}",
            "content": None,
        }

    return {
        "success": True,
        "content": data or response,
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


def run_image_test(title: str, image_prefix: str, generate_func, **kwargs):
    print("=" * 50)
    print(title)
    print("=" * 50)

    try:
        response = generate_func(**kwargs)
        result = parse_response(response)
        if result["success"]:
            image_urls = result["content"]
            print("生成成功:")
            print(image_urls)
            saved_paths = save_images(image_urls, image_prefix)
            if saved_paths:
                print("图片已保存到:")
                for path in saved_paths:
                    print(path)
            else:
                print("图片保存失败")
        else:
            print(f"生成失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_image_01():
    if not check_api_key():
        return

    client = Image01(api_key=API_KEY)
    run_image_test(
        "测试 Image 01 图像生成",
        "image_01",
        client.generate,
        prompt="一幅美丽的日落风景画，海面上反射着金色的阳光",
        resolution="1024x1024",
        num_images=1,
    )


def test_image_01_turbo():
    if not check_api_key():
        return

    client = Image01Turbo(api_key=API_KEY)
    run_image_test(
        "测试 Image 01 Turbo 极速版",
        "image_01_turbo",
        client.generate,
        prompt="一只可爱的猫咪在草地上玩耍",
        resolution="2048x2048",
        num_images=2,
    )


def test_image_to_image():
    if not check_api_key():
        return

    client = Image01(api_key=API_KEY)
    run_image_test(
        "测试 Image 01 图生图",
        "image_to_image",
        client.generate_from_image,
        prompt="保持主体特征不变，转换成电影感插画风格",
        image_url=REFERENCE_IMAGE_URL,
        resolution="1024x1024",
        num_images=1,
    )


def test_various_resolutions():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试不同分辨率")
    print("=" * 50)

    resolutions = ["512x512", "1024x1024", "2048x2048"]

    try:
        client = Image01(api_key=API_KEY)

        for resolution in resolutions:
            print(f"\n测试分辨率: {resolution}")
            response = client.generate(
                prompt="一幅抽象艺术画",
                resolution=resolution,
            )

            result = parse_response(response)
            if result["success"]:
                print("  ✓ 生成成功")
                saved_paths = save_images(result["content"], f"resolution_{resolution.replace('x', '_')}")
                if saved_paths:
                    for path in saved_paths:
                        print(f"  已保存: {path}")
                else:
                    print("  图片保存失败")
            else:
                print(f"  ✗ 生成失败: {result['error']}")

    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def show_help():
    print("MiniMax 图像生成 API 示例")
    print("=" * 50)
    print("用法: python example.py [选项]")
    print()
    print("选项:")
    print("  image-01         - 测试 Image 01")
    print("  image-01-turbo   - 测试 Image 01 Turbo")
    print("  image-to-image   - 测试图生图")
    print("  resolutions      - 测试不同分辨率")
    print("  all              - 运行所有测试")
    print("  -l, --list       - 列出所有测试")
    print("  -h, --help       - 显示帮助")
    print()
    print("环境变量:")
    print("  MINIMAX_API_KEY - 你的 API Key")
    print()
    print("输出目录:")
    print(f"  {OUTPUT_DIR}")
    print()
    print("示例:")
    print("  export MINIMAX_API_KEY='your_key'")
    print("  python example.py image-01")
    print("  python example.py image-to-image")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="MiniMax 图像生成 API 示例")
    parser.add_argument("test", nargs="?", help="运行特定测试")
    parser.add_argument("-l", "--list", action="store_true", help="列出所有测试")

    args = parser.parse_args()

    if args.list:
        print("可用测试:")
        print("  image-01         - 测试 Image 01")
        print("  image-01-turbo   - 测试 Image 01 Turbo")
        print("  image-to-image   - 测试图生图")
        print("  resolutions      - 测试不同分辨率")
        print("  all              - 运行所有测试")
        return

    if args.test == "image-01":
        test_image_01()
    elif args.test == "image-01-turbo":
        test_image_01_turbo()
    elif args.test == "image-to-image":
        test_image_to_image()
    elif args.test == "resolutions":
        test_various_resolutions()
    elif args.test == "all":
        test_image_01()
        test_image_01_turbo()
        test_image_to_image()
        test_various_resolutions()
    else:
        show_help()


if __name__ == "__main__":
    main()
