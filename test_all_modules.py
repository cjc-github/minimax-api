#!/usr/bin/env python3
"""
MiniMax API 综合测试脚本
测试所有已实现的功能模块
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

print("=" * 60)
print("MiniMax API Python SDK - 模块测试")
print("=" * 60)
print()

API_KEY = os.environ.get("MINIMAX_API_KEY", "")

def check_api_key():
    """检查 API Key 是否设置"""
    if not API_KEY:
        print("⚠️  警告: 环境变量 MINIMAX_API_KEY 未设置")
        print("   提示: export MINIMAX_API_KEY='your_api_key'")
        print("   测试将以模拟模式运行")
        print()
        return False
    return True

def test_imports():
    """测试所有模块导入"""
    print("1. 测试模块导入...")
    print("-" * 60)
    
    try:
        from text_generation import M27, M27Highspeed, M25, M25Highspeed, M21, M21Highspeed, M2
        print("  ✓ text_generation 模块导入成功")
        print("    - M27, M27Highspeed")
        print("    - M25, M25Highspeed")
        print("    - M21, M21Highspeed")
        print("    - M2")
    except Exception as e:
        print(f"  ✗ text_generation 模块导入失败: {e}")
        return False
    
    try:
        from text_to_speech import Speech28HD, Speech28Turbo, Speech26HD, Speech26Turbo, Speech02HD, Speech02Turbo
        print("  ✓ text_to_speech 模块导入成功")
        print("    - Speech28HD, Speech28Turbo")
        print("    - Speech26HD, Speech26Turbo")
        print("    - Speech02HD, Speech02Turbo")
    except Exception as e:
        print(f"  ✗ text_to_speech 模块导入失败: {e}")
        return False
    
    try:
        from music_generation import Music26, Music26Highspeed, MusicCover, LyricsGeneration, LyricsGenerationHighspeed
        print("  ✓ music_generation 模块导入成功")
        print("    - Music26, Music26Highspeed")
        print("    - MusicCover")
        print("    - LyricsGeneration, LyricsGenerationHighspeed")
    except Exception as e:
        print(f"  ✗ music_generation 模块导入失败: {e}")
        return False
    
    try:
        from image_generation import Image01, Image01Turbo
        print("  ✓ image_generation 模块导入成功")
        print("    - Image01, Image01Turbo")
    except Exception as e:
        print(f"  ✗ image_generation 模块导入失败: {e}")
        return False
    
    try:
        from coding_plan import CodingPlanVLM, CodingPlanSearch
        print("  ✓ coding_plan 模块导入成功")
        print("    - CodingPlanVLM")
        print("    - CodingPlanSearch")
    except Exception as e:
        print(f"  ✗ coding_plan 模块导入失败: {e}")
        return False
    
    print()
    return True

def test_class_instantiation():
    """测试类实例化"""
    print("2. 测试类实例化...")
    print("-" * 60)
    
    try:
        from text_generation import M27
        client = M27(api_key="test_key")
        print(f"  ✓ M27 实例化成功")
        assert client.api_key == "test_key"
    except Exception as e:
        print(f"  ✗ M27 实例化失败: {e}")
        return False
    
    try:
        from text_to_speech import Speech28HD, Speech28Turbo, Speech26HD, Speech26Turbo, Speech02HD, Speech02Turbo
        client1 = Speech28HD(api_key="test_key", group_id="test_group")
        client2 = Speech28Turbo(api_key="test_key", group_id="test_group")
        client3 = Speech26HD(api_key="test_key", group_id="test_group")
        client4 = Speech26Turbo(api_key="test_key", group_id="test_group")
        client5 = Speech02HD(api_key="test_key", group_id="test_group")
        client6 = Speech02Turbo(api_key="test_key", group_id="test_group")
        print(f"  ✓ Speech28HD, Speech28Turbo, Speech26HD, Speech26Turbo, Speech02HD, Speech02Turbo 实例化成功")
        assert client1.api_key == "test_key"
        assert client1.group_id == "test_group"
        assert client2.api_key == "test_key"
        assert client2.group_id == "test_group"
        assert client3.api_key == "test_key"
        assert client3.group_id == "test_group"
        assert client4.api_key == "test_key"
        assert client4.group_id == "test_group"
        assert client5.api_key == "test_key"
        assert client5.group_id == "test_group"
        assert client6.api_key == "test_key"
        assert client6.group_id == "test_group"
    except Exception as e:
        print(f"  ✗ Speech 模块实例化失败: {e}")
        return False
    
    try:
        from music_generation import Music26, MusicCover, LyricsGeneration
        client1 = Music26(api_key="test_key", group_id="test_group")
        client2 = MusicCover(api_key="test_key", group_id="test_group")
        client3 = LyricsGeneration(api_key="test_key", group_id="test_group")
        print(f"  ✓ Music26, MusicCover, LyricsGeneration 实例化成功")
        assert client1.api_key == "test_key"
        assert client1.group_id == "test_group"
        assert client2.api_key == "test_key"
        assert client2.group_id == "test_group"
        assert client3.api_key == "test_key"
        assert client3.group_id == "test_group"
    except Exception as e:
        print(f"  ✗ 音乐模块实例化失败: {e}")
        return False
    
    try:
        from image_generation import Image01, Image01Turbo
        client1 = Image01(api_key="test_key", group_id="test_group")
        client2 = Image01Turbo(api_key="test_key", group_id="test_group")
        print(f"  ✓ Image01, Image01Turbo 实例化成功")
        assert client1.api_key == "test_key"
        assert client1.group_id == "test_group"
        assert client2.api_key == "test_key"
        assert client2.group_id == "test_group"
        assert callable(client1.generate_from_image)
        assert callable(client2.generate_from_image)
        print("    - generate_from_image 方法可用")
    except Exception as e:
        print(f"  ✗ Image01 实例化失败: {e}")
        return False
    
    try:
        from coding_plan import CodingPlanVLM, CodingPlanSearch
        client1 = CodingPlanVLM(api_key="test_key", group_id="test_group")
        client2 = CodingPlanSearch(api_key="test_key", group_id="test_group")
        print(f"  ✓ CodingPlanVLM, CodingPlanSearch 实例化成功")
        assert client1.api_key == "test_key"
        assert client1.group_id == "test_group"
        assert client2.api_key == "test_key"
        assert client2.group_id == "test_group"
    except Exception as e:
        print(f"  ✗ CodingPlanVLM 实例化失败: {e}")
        return False
    
    print()
    return True

def test_api_keys():
    """测试 API 端点配置"""
    print("3. 测试 API 端点配置...")
    print("-" * 60)
    
    try:
        from text_generation import M27
        client = M27(api_key="test")
        assert client.BASE_URL == "https://api.minimaxi.com"
        print(f"  ✓ text_generation BASE_URL 配置正确: {client.BASE_URL}")
    except Exception as e:
        print(f"  ✗ text_generation BASE_URL 配置错误: {e}")
        return False

    try:
        from text_to_speech import Speech28HD
        client = Speech28HD(api_key="test", group_id="test_group")
        assert client.BASE_URL == "https://api.minimaxi.com"
        assert client.group_id == "test_group"
        print(f"  ✓ text_to_speech BASE_URL 配置正确: {client.BASE_URL}")
    except Exception as e:
        print(f"  ✗ text_to_speech BASE_URL 配置错误: {e}")
        return False

    try:
        from music_generation import Music26
        client = Music26(api_key="test", group_id="test_group")
        assert client.BASE_URL == "https://api.minimaxi.com"
        assert client.group_id == "test_group"
        print(f"  ✓ music_generation BASE_URL 配置正确: {client.BASE_URL}")
    except Exception as e:
        print(f"  ✗ music_generation BASE_URL 配置错误: {e}")
        return False

    try:
        from image_generation import Image01
        client = Image01(api_key="test", group_id="test_group")
        assert client.BASE_URL == "https://api.minimaxi.com"
        assert client.group_id == "test_group"
        print(f"  ✓ image_generation BASE_URL 配置正确: {client.BASE_URL}")
    except Exception as e:
        print(f"  ✗ image_generation BASE_URL 配置错误: {e}")
        return False

    try:
        from coding_plan import CodingPlanVLM
        client = CodingPlanVLM(api_key="test", group_id="test_group")
        assert client.BASE_URL == "https://api.minimaxi.com"
        assert client.group_id == "test_group"
        print(f"  ✓ coding_plan BASE_URL 配置正确: {client.BASE_URL}")
    except Exception as e:
        print(f"  ✗ coding_plan BASE_URL 配置错误: {e}")
        return False

    print()
    return True

def show_summary():
    """显示功能总结"""
    print("4. 功能模块总结...")
    print("-" * 60)
    print()
    print("  已实现的功能模块：")
    print()
    print("  📝 文本生成 (text_generation):")
    print("     - M2.7 / M2.7-highspeed")
    print("     - M2.5 / M2.5-highspeed")
    print("     - M2.1 / M2.1-highspeed")
    print("     - M2")
    print()
    print("  🔊 语音合成 (text_to_speech):")
    print("     - Speech 2.8 HD / Turbo")
    print("     - Speech 2.6 HD / Turbo")
    print("     - Speech 02 HD / Turbo")
    print()
    print("  🎵 音乐生成 (music_generation): ✨ 新增")
    print("     - Music 2.6 / 2.6-highspeed")
    print("     - Music Cover")
    print("     - Lyrics Generation / Highspeed")
    print()
    print("  🖼️  图像生成 (image_generation): ✨ 新增")
    print("     - Image 01")
    print("     - Image 01 Turbo")
    print("     - Image-to-Image")
    print()
    print("  💻 编码计划 (coding_plan): ✨ 新增")
    print("     - Coding Plan VLM")
    print("     - Coding Plan Search")
    print()
    print("  总计: 6 个模块, 18 个功能类")
    print()

def main():
    """主函数"""
    print()
    check_api_key()
    
    all_passed = True
    
    if not test_imports():
        all_passed = False
    
    if not test_class_instantiation():
        all_passed = False
    
    if not test_api_keys():
        all_passed = False
    
    show_summary()
    
    print("=" * 60)
    if all_passed:
        print("✅ 所有测试通过！")
        print()
        print("下一步：")
        print("  1. 设置环境变量: export MINIMAX_API_KEY='your_key'")
        print("  2. 运行示例代码:")
        print("     - python text_generation/example.py m27")
        print("     - python music_generation/example.py music-26")
        print("     - python image_generation/example.py image-01")
        print("     - python coding_plan/example.py vlm-generate")
        print()
        print("  详细文档: 查看 API_FEATURES.md")
    else:
        print("❌ 部分测试失败，请检查错误信息")
        sys.exit(1)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
