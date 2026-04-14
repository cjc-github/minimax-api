import requests
from typing import Any, Dict, Optional


class CodingPlanSearch:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def search(
        self,
        query: str,
        model: str = "coding-plan-search",
        max_results: int = 10,
        language: Optional[str] = None,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Coding Plan Search 编码计划搜索

        搜索相关的编码计划和解决方案

        Args:
            query: 搜索查询
            model: 模型名称，默认 coding-plan-search
            max_results: 最大返回结果数，默认 10
            language: 编程语言筛选，可选
            timeout: 超时时间，默认 30 秒

        Returns:
            包含搜索结果的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/coding_plan_search{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "query": query,
            "max_results": max_results,
        }

        if language is not None:
            payload["language"] = language

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

    def recommend(
        self,
        context: str,
        model: str = "coding-plan-search",
        num_recommendations: int = 5,
        timeout: int = 30,
    ) -> Dict[str, Any]:
        """
        Coding Plan Search 推荐编码计划

        基于上下文推荐相关的编码计划

        Args:
            context: 上下文描述
            model: 模型名称，默认 coding-plan-search
            num_recommendations: 推荐数量，默认 5
            timeout: 超时时间，默认 30 秒

        Returns:
            包含推荐结果的字典
        """
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/coding_plan_search{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "context": context,
            "num_recommendations": num_recommendations,
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
