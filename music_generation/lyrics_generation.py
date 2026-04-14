import requests
from typing import Dict, Any, Literal


# api参考网址：
# https://platform.minimaxi.com/docs/api-reference/lyrics-generation

class LyricsGeneration:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def generate(
        self,
        mode: Literal["write_full_song", "edit"],
        prompt: str,
        model: str = "lyrics_generation",
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Lyrics Generation 歌词生成

        根据提示词生成完整的歌词内容

        Args:
            mode: 生成模式，可选 "write_full_song"（创作新歌词）或 "edit"（编辑现有歌词）
            prompt: 歌词描述或主题提示词
            model: 模型名称，默认 lyrics_generation
            timeout: 超时时间，默认 30 秒

        Returns:
            包含生成歌词的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/lyrics_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "mode": mode,
            "prompt": prompt,
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=timeout)

            if response.status_code != 200:
                print(f"HTTP 错误: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "base_resp": {"status_code": response.status_code, "status_msg": response.text},
                }

            result = response.json()
            if result is None:
                print("警告: 响应 JSON 为 None")
                print(f"响应状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": "响应内容为空",
                    "base_resp": {"status_code": -1, "status_msg": "Empty response"},
                }

            return result

        except requests.exceptions.Timeout:
            print("错误: 请求超时")
            return {
                "success": False,
                "error": "请求超时",
                "base_resp": {"status_code": -2, "status_msg": "Timeout"},
            }
        except requests.exceptions.RequestException as e:
            print(f"错误: 网络请求失败 - {e}")
            return {
                "success": False,
                "error": f"网络请求失败: {e}",
                "base_resp": {"status_code": -3, "status_msg": str(e)},
            }
        except Exception as e:
            print(f"错误: {e}")
            return {
                "success": False,
                "error": str(e),
                "base_resp": {"status_code": -4, "status_msg": str(e)},
            }

    def write_full_song(self, prompt: str, model: str = "lyrics_generation", timeout: int = 30) -> Dict[str, Any]:
        """
        创作完整歌词

        Args:
            prompt: 歌词描述或主题提示词
            model: 模型名称，默认 lyrics_generation
            timeout: 超时时间，默认 30 秒

        Returns:
            包含生成歌词的字典
        """
        return self.generate(mode="write_full_song", prompt=prompt, model=model, timeout=timeout)

    def edit(self, prompt: str, model: str = "lyrics_generation", timeout: int = 30) -> Dict[str, Any]:
        """
        编辑歌词

        Args:
            prompt: 歌词编辑提示词
            model: 模型名称，默认 lyrics_generation
            timeout: 超时时间，默认 30 秒

        Returns:
            包含生成歌词的字典
        """
        return self.generate(mode="edit", prompt=prompt, model=model, timeout=timeout)


class LyricsGenerationHighspeed:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def generate(
        self,
        mode: Literal["write_full_song", "edit"],
        prompt: str,
        model: str = "lyrics_generation-highspeed",
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Lyrics Generation 极速版歌词生成

        效果不变，更快更敏捷

        Args:
            mode: 生成模式，可选 "write_full_song"（创作新歌词）或 "edit"（编辑现有歌词）
            prompt: 歌词描述或主题提示词
            model: 模型名称，默认 lyrics_generation-highspeed
            timeout: 超时时间，默认 30 秒

        Returns:
            包含生成歌词的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/lyrics_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "mode": mode,
            "prompt": prompt,
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=timeout)

            if response.status_code != 200:
                print(f"HTTP 错误: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "base_resp": {"status_code": response.status_code, "status_msg": response.text},
                }

            result = response.json()
            if result is None:
                print("警告: 响应 JSON 为 None")
                print(f"响应状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": "响应内容为空",
                    "base_resp": {"status_code": -1, "status_msg": "Empty response"},
                }

            return result

        except requests.exceptions.Timeout:
            print("错误: 请求超时")
            return {
                "success": False,
                "error": "请求超时",
                "base_resp": {"status_code": -2, "status_msg": "Timeout"},
            }
        except requests.exceptions.RequestException as e:
            print(f"错误: 网络请求失败 - {e}")
            return {
                "success": False,
                "error": f"网络请求失败: {e}",
                "base_resp": {"status_code": -3, "status_msg": str(e)},
            }
        except Exception as e:
            print(f"错误: {e}")
            return {
                "success": False,
                "error": str(e),
                "base_resp": {"status_code": -4, "status_msg": str(e)},
            }

    def write_full_song(self, prompt: str, model: str = "lyrics_generation-highspeed", timeout: int = 30) -> Dict[str, Any]:
        """
        极速版创作完整歌词

        Args:
            prompt: 歌词描述或主题提示词
            model: 模型名称，默认 lyrics_generation-highspeed
            timeout: 超时时间，默认 30 秒

        Returns:
            包含生成歌词的字典
        """
        return self.generate(mode="write_full_song", prompt=prompt, model=model, timeout=timeout)

    def edit(self, prompt: str, model: str = "lyrics_generation-highspeed", timeout: int = 30) -> Dict[str, Any]:
        """
        极速版编辑歌词

        Args:
            prompt: 歌词编辑提示词
            model: 模型名称，默认 lyrics_generation-highspeed
            timeout: 超时时间，默认 30 秒

        Returns:
            包含生成歌词的字典
        """
        return self.generate(mode="edit", prompt=prompt, model=model, timeout=timeout)
