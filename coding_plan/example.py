import argparse
import os
import sys
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from coding_plan import CodingPlanSearch, CodingPlanVLM


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


def test_coding_plan_vlm_analyze():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Coding Plan VLM 图像分析")
    print("=" * 50)

    try:
        client = CodingPlanVLM(api_key=API_KEY)
        response = client.analyze(
            image_url="https://example.com/code-screenshot.png",
            prompt="分析这段代码的功能和结构",
            max_tokens=2048,
        )

        result = parse_response(response)
        if result["success"]:
            print("分析成功:")
            print(result["content"])
        else:
            print(f"分析失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_coding_plan_vlm_generate():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Coding Plan VLM 生成计划")
    print("=" * 50)

    try:
        client = CodingPlanVLM(api_key=API_KEY)
        response = client.generate_plan(
            description="一个用户登录注册系统",
            language="python",
            framework="flask",
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


def test_coding_plan_search():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Coding Plan Search 搜索")
    print("=" * 50)

    try:
        client = CodingPlanSearch(api_key=API_KEY)
        response = client.search(
            query="用户认证和授权系统设计",
            max_results=10,
            language="python",
        )

        result = parse_response(response)
        if result["success"]:
            print("搜索成功:")
            print(result["content"])
        else:
            print(f"搜索失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def test_coding_plan_recommend():
    if not check_api_key():
        return

    print("=" * 50)
    print("测试 Coding Plan Search 推荐")
    print("=" * 50)

    try:
        client = CodingPlanSearch(api_key=API_KEY)
        response = client.recommend(
            context="我正在开发一个电商平台，需要处理订单管理、支付集成、库存管理等核心功能",
            num_recommendations=5,
        )

        result = parse_response(response)
        if result["success"]:
            print("推荐成功:")
            print(result["content"])
        else:
            print(f"推荐失败: {result['error']}")
    except requests.exceptions.Timeout:
        print("错误: 请求超时")
    except requests.exceptions.RequestException as e:
        print(f"错误: 网络请求失败 - {e}")
    except Exception as e:
        print(f"错误: {e}")

    print()


def show_help():
    print("MiniMax Coding Plan API 示例")
    print("=" * 50)
    print("用法: python example.py [选项]")
    print()
    print("选项:")
    print("  vlm-analyze   - 测试 VLM 图像分析")
    print("  vlm-generate  - 测试 VLM 生成计划")
    print("  search        - 测试搜索功能")
    print("  recommend     - 测试推荐功能")
    print("  all           - 运行所有测试")
    print("  -l, --list    - 列出所有测试")
    print("  -h, --help    - 显示帮助")
    print()
    print("环境变量:")
    print("  MINIMAX_API_KEY - 你的 API Key")
    print()
    print("示例:")
    print("  export MINIMAX_API_KEY='your_key'")
    print("  python example.py vlm-generate")


def main():
    parser = argparse.ArgumentParser(description="MiniMax Coding Plan API 示例")
    parser.add_argument("test", nargs="?", help="运行特定测试")
    parser.add_argument("-l", "--list", action="store_true", help="列出所有测试")

    args = parser.parse_args()

    if args.list:
        print("可用测试:")
        print("  vlm-analyze   - 测试 VLM 图像分析")
        print("  vlm-generate  - 测试 VLM 生成计划")
        print("  search        - 测试搜索功能")
        print("  recommend     - 测试推荐功能")
        print("  all           - 运行所有测试")
        return

    if args.test == "vlm-analyze":
        test_coding_plan_vlm_analyze()
    elif args.test == "vlm-generate":
        test_coding_plan_vlm_generate()
    elif args.test == "search":
        test_coding_plan_search()
    elif args.test == "recommend":
        test_coding_plan_recommend()
    elif args.test == "all":
        test_coding_plan_vlm_analyze()
        test_coding_plan_vlm_generate()
        test_coding_plan_search()
        test_coding_plan_recommend()
    else:
        show_help()


if __name__ == "__main__":
    main()
