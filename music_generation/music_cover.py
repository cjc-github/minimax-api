import requests
from typing import Dict, Any, Optional


# api参考网址：
# https://platform.minimaxi.com/docs/api-reference/music-generation

class MusicCover:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def generate(
        self,
        audio_url: str = "",
        audio_base64: str = "",
        cover_feature_id: str = "",
        prompt: str = "",
        model: str = "music-cover",
        resolution: str = "1k",
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Music Cover 音乐封面生成

        根据音乐内容生成匹配的封面图片。必须提供 cover_feature_id 或
        audio_url/audio_base64 中的至少一个。

        Args:
            audio_url: 音乐文件的 URL 地址（与 audio_base64 二选一）
            audio_base64: 音乐文件的 base64 编码（与 audio_url 二选一）
            cover_feature_id: 封面特征 ID，可选
            prompt: 封面描述提示词，可选
            model: 模型名称，默认 music-cover
            resolution: 图片分辨率，支持 "1k", "2k", "4k"，默认 "1k"
            timeout: 超时时间，默认 60 秒

        Returns:
            包含封面图片数据的字典
        """
        if not cover_feature_id and not audio_url and not audio_base64:
            return {
                "success": False,
                "error": "必须提供 cover_feature_id 或 audio_url/audio_base64",
                "base_resp": {"status_code": -5, "status_msg": "Missing required params"},
            }

        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/music_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
        }

        if audio_url:
            payload["audio_url"] = audio_url
        if audio_base64:
            payload["audio_base64"] = audio_base64
        if cover_feature_id:
            payload["cover_feature_id"] = cover_feature_id
        if prompt:
            payload["prompt"] = prompt
        if resolution:
            payload["resolution"] = resolution

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


class MusicCoverFree:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def generate(
        self,
        audio_url: str = "",
        audio_base64: str = "",
        cover_feature_id: str = "",
        prompt: str = "",
        model: str = "music-cover-free",
        resolution: str = "1k",
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Music Cover Free 音乐封面生成

        免费版本封面生成，适合测试和轻量级使用。必须提供 cover_feature_id 或
        audio_url/audio_base64 中的至少一个。

        Args:
            audio_url: 音乐文件的 URL 地址（与 audio_base64 二选一）
            audio_base64: 音乐文件的 base64 编码（与 audio_url 二选一）
            cover_feature_id: 封面特征 ID，可选
            prompt: 封面描述提示词，可选
            model: 模型名称，默认 music-cover-free
            resolution: 图片分辨率，支持 "1k", "2k", "4k"，默认 "1k"
            timeout: 超时时间，默认 60 秒

        Returns:
            包含封面图片数据的字典
        """
        if not cover_feature_id and not audio_url and not audio_base64:
            return {
                "success": False,
                "error": "必须提供 cover_feature_id 或 audio_url/audio_base64",
                "base_resp": {"status_code": -5, "status_msg": "Missing required params"},
            }

        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/music_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
        }

        if audio_url:
            payload["audio_url"] = audio_url
        if audio_base64:
            payload["audio_base64"] = audio_base64
        if cover_feature_id:
            payload["cover_feature_id"] = cover_feature_id
        if prompt:
            payload["prompt"] = prompt
        if resolution:
            payload["resolution"] = resolution

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
