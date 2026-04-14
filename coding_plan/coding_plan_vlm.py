import requests
from typing import Any, Dict, Optional


class CodingPlanVLM:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def analyze(
        self,
        image_url: str,
        prompt: str,
        model: str = "coding-plan-vlm",
        max_tokens: int = 2048,
        temperature: float = 0.7,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Coding Plan VLM 视觉语言模型分析

        分析代码截图或图表，生成编码计划

        Args:
            image_url: 图像 URL 地址
            prompt: 分析提示词
            model: 模型名称，默认 coding-plan-vlm
            max_tokens: 最大生成 token 数，默认 2048
            temperature: 温度参数，默认 0.7
            timeout: 超时时间，默认 30 秒

        Returns:
            包含分析结果的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/coding_plan_vlm{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "image_url": image_url,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
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

    def generate_plan(
        self,
        description: str,
        language: Optional[str] = None,
        framework: Optional[str] = None,
        model: str = "coding-plan-vlm",
        max_tokens: int = 2048,
        temperature: float = 0.7,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Coding Plan VLM 生成编码计划

        根据描述生成详细的编码计划

        Args:
            description: 功能描述
            language: 编程语言，可选（如 "python", "javascript", "java"）
            framework: 框架，可选（如 "react", "vue", "django"）
            model: 模型名称，默认 coding-plan-vlm
            max_tokens: 最大生成 token 数，默认 2048
            temperature: 温度参数，默认 0.7
            timeout: 超时时间，默认 30 秒

        Returns:
            包含编码计划的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/coding_plan_vlm{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "description": description,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        if language is not None:
            payload["language"] = language
        if framework is not None:
            payload["framework"] = framework

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
