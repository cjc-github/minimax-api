import requests
from typing import Dict, Any, Optional


class MusicCover:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def generate(
        self,
        music_url: str,
        prompt: str = "",
        model: str = "music-cover",
        resolution: str = "1k",
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Music Cover 音乐封面生成

        根据音乐内容生成匹配的封面图片

        Args:
            music_url: 音乐文件的 URL 地址
            prompt: 封面描述提示词，可选
            model: 模型名称，默认 music-cover
            resolution: 图片分辨率，支持 "1k", "2k", "4k"，默认 "1k"
            timeout: 超时时间，默认 60 秒

        Returns:
            包含封面图片数据的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/music_cover{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "music_url": music_url,
        }

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
