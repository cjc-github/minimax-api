import requests
from typing import Dict, Any, List


class M21:
    BASE_URL = "https://api.minimaxi.com"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate(
        self,
        messages: List[Dict[str, str]],
        model: str = "MiniMax-M2.1",
        max_tokens: int = 2048,
        temperature: float = 0.7,
        top_p: float = 0.95,
        timeout: int = 30
    ) -> Dict[str, Any]:
        """
        M2.1 文本生成

        强大多语言编程能力，全面升级编程体验，输出速度约 60tps

        Args:
            messages: 消息列表，格式为 [{"role": "user/assistant", "content": "内容"}]
            model: 模型名称，默认 MiniMax-M2.1
            max_tokens: 最大生成 token 数，默认 2048
            temperature: 温度参数，默认 0.7
            top_p: top_p 参数，默认 0.95
            timeout: 超时时间，默认 30 秒

        Returns:
            包含生成结果的字典
        """
        url = f"{self.BASE_URL}/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p
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


class M21Highspeed:
    BASE_URL = "https://api.minimaxi.com"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate(
        self,
        messages: List[Dict[str, str]],
        model: str = "MiniMax-M2.1-highspeed",
        max_tokens: int = 2048,
        temperature: float = 0.7,
        top_p: float = 0.95,
        timeout: int = 30
    ) -> Dict[str, Any]:
        """
        M2.1 极速版文本生成

        效果不变，更快更敏捷，输出速度约 100tps

        Args:
            messages: 消息列表
            model: 模型名称，默认 MiniMax-M2.1-highspeed
            max_tokens: 最大生成 token 数
            temperature: 温度参数
            top_p: top_p 参数
            timeout: 超时时间

        Returns:
            包含生成结果的字典
        """
        url = f"{self.BASE_URL}/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p
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