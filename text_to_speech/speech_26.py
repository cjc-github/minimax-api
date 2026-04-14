import requests
from typing import Dict, Any


class Speech26HD:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def synthesize(
        self,
        text: str,
        voice_id: str = "male-qn-qingse",
        model: str = "speech-2.6-hd",
        speed: float = 1.0,
        volume: float = 1.0,
        pitch: float = 0,
        audio_format: str = "mp3",
        sample_rate: int = 32000,
        bitrate: int = 128000,
        timeout: int = 60
    ) -> Dict[str, Any]:
        """
        Speech 2.6 HD 同步语音合成

        HD 模型，韵律表现出色，极致音质与韵律表现，生成更快更自然

        Args:
            text: 待合成文本，最大 10,000 字符
            voice_id: 音色 ID，默认 male-qn-qingse
            model: 模型名称，默认 speech-2.6-hd
            speed: 语速，默认 1.0 (范围 0.5-2.0)
            volume: 音量，默认 1.0 (范围 0.1-10.0)
            pitch: 语调，默认 0 (范围 -12-12)
            audio_format: 音频格式，支持 mp3/pcm/flac/wav
            sample_rate: 采样率，默认 32000
            bitrate: 比特率，默认 128000
            timeout: 超时时间，默认 60 秒

        Returns:
            包含音频数据的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/t2a_v2{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "text": text,
            "voice_setting": {
                "voice_id": voice_id,
                "speed": speed,
                "vol": volume,
                "pitch": pitch
            },
            "audio_setting": {
                "format": audio_format,
                "sample_rate": sample_rate,
                "bitrate": bitrate
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=timeout)
            
            if response.status_code != 200:
                print(f"HTTP 错误: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "base_resp": {"status_code": response.status_code, "status_msg": response.text}
                }
            
            result = response.json()
            if result is None:
                print(f"警告: 响应 JSON 为 None")
                print(f"响应状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": "响应内容为空",
                    "base_resp": {"status_code": -1, "status_msg": "Empty response"}
                }
            
            return result
            
        except requests.exceptions.Timeout:
            print(f"错误: 请求超时")
            return {
                "success": False,
                "error": "请求超时",
                "base_resp": {"status_code": -2, "status_msg": "Timeout"}
            }
        except requests.exceptions.RequestException as e:
            print(f"错误: 网络请求失败 - {e}")
            return {
                "success": False,
                "error": f"网络请求失败: {e}",
                "base_resp": {"status_code": -3, "status_msg": str(e)}
            }
        except Exception as e:
            print(f"错误: {e}")
            return {
                "success": False,
                "error": str(e),
                "base_resp": {"status_code": -4, "status_msg": str(e)}
            }


class Speech26Turbo:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def synthesize(
        self,
        text: str,
        voice_id: str = "male-qn-qingse",
        model: str = "speech-2.6-turbo",
        speed: float = 1.0,
        volume: float = 1.0,
        pitch: float = 0,
        audio_format: str = "mp3",
        sample_rate: int = 32000,
        bitrate: int = 128000,
        timeout: int = 60
    ) -> Dict[str, Any]:
        """
        Speech 2.6 Turbo 同步语音合成

        Turbo 模型，音质优异，超低时延，响应更灵敏

        Args:
            text: 待合成文本，最大 10,000 字符
            voice_id: 音色 ID
            model: 模型名称，默认 speech-2.6-turbo
            speed: 语速
            volume: 音量
            pitch: 语调
            audio_format: 音频格式
            sample_rate: 采样率
            bitrate: 比特率
            timeout: 超时时间

        Returns:
            包含音频数据的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/t2a_v2{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "text": text,
            "voice_setting": {
                "voice_id": voice_id,
                "speed": speed,
                "vol": volume,
                "pitch": pitch
            },
            "audio_setting": {
                "format": audio_format,
                "sample_rate": sample_rate,
                "bitrate": bitrate
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=timeout)
            
            if response.status_code != 200:
                print(f"HTTP 错误: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "base_resp": {"status_code": response.status_code, "status_msg": response.text}
                }
            
            result = response.json()
            if result is None:
                print(f"警告: 响应 JSON 为 None")
                print(f"响应状态码: {response.status_code}")
                print(f"响应内容: {response.text}")
                return {
                    "success": False,
                    "error": "响应内容为空",
                    "base_resp": {"status_code": -1, "status_msg": "Empty response"}
                }
            
            return result
            
        except requests.exceptions.Timeout:
            print(f"错误: 请求超时")
            return {
                "success": False,
                "error": "请求超时",
                "base_resp": {"status_code": -2, "status_msg": "Timeout"}
            }
        except requests.exceptions.RequestException as e:
            print(f"错误: 网络请求失败 - {e}")
            return {
                "success": False,
                "error": f"网络请求失败: {e}",
                "base_resp": {"status_code": -3, "status_msg": str(e)}
            }
        except Exception as e:
            print(f"错误: {e}")
            return {
                "success": False,
                "error": str(e),
                "base_resp": {"status_code": -4, "status_msg": str(e)}
            }