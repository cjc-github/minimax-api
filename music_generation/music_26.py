import requests
from typing import Dict, Any, List, Optional


class Music26:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def generate(
        self,
        prompt: str,
        model: str = "music-2.6",
        output_token_limit: int = 2048,
        duration: Optional[int] = None,
        style: Optional[str] = None,
        tags: Optional[List[str]] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Music 2.6 音乐生成

        强大的音乐生成能力，支持多种风格和标签

        Args:
            prompt: 音乐描述提示词
            model: 模型名称，默认 music-2.6
            output_token_limit: 输出 token 限制，默认 2048
            duration: 音乐时长（秒），可选
            style: 音乐风格，可选（如 "pop", "rock", "jazz"）
            tags: 音乐标签列表，可选
            timeout: 超时时间，默认 60 秒

        Returns:
            包含生成音乐数据的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/music_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "prompt": prompt,
            "output_token_limit": output_token_limit,
        }

        if duration is not None:
            payload["duration"] = duration
        if style is not None:
            payload["style"] = style
        if tags is not None:
            payload["tags"] = tags

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


class Music26Highspeed:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def generate(
        self,
        prompt: str,
        model: str = "music-2.6-highspeed",
        output_token_limit: int = 2048,
        duration: Optional[int] = None,
        style: Optional[str] = None,
        tags: Optional[List[str]] = None,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Music 2.6 极速版音乐生成

        效果不变，更快更敏捷

        Args:
            prompt: 音乐描述提示词
            model: 模型名称，默认 music-2.6-highspeed
            output_token_limit: 输出 token 限制，默认 2048
            duration: 音乐时长（秒），可选
            style: 音乐风格，可选
            tags: 音乐标签列表，可选
            timeout: 超时时间，默认 60 秒

        Returns:
            包含生成音乐数据的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/music_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "prompt": prompt,
            "output_token_limit": output_token_limit,
        }

        if duration is not None:
            payload["duration"] = duration
        if style is not None:
            payload["style"] = style
        if tags is not None:
            payload["tags"] = tags

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
