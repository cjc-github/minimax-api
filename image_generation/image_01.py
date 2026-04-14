import requests
from typing import Any, Dict


class Image01:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def _post_generation_request(self, payload: Dict[str, Any], timeout: int) -> Dict[str, Any]:
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/image_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
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

    def generate(
        self,
        prompt: str,
        model: str = "image-01",
        resolution: str = "1024x1024",
        num_images: int = 1,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Image 01 图像生成

        强大的文本到图像生成能力

        Args:
            prompt: 图像描述提示词
            model: 模型名称，默认 image-01
            resolution: 图像分辨率，支持 "512x512", "1024x1024", "2048x2048" 等，默认 "1024x1024"
            num_images: 生成图像数量，默认 1
            timeout: 超时时间，默认 60 秒

        Returns:
            包含生成图像数据的字典
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "resolution": resolution,
            "num_images": num_images,
        }

        return self._post_generation_request(payload, timeout)

    def generate_from_image(
        self,
        prompt: str,
        image_url: str,
        model: str = "image-01",
        resolution: str = "1024x1024",
        num_images: int = 1,
        reference_type: str = "character",
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Image 01 图生图

        基于参考图生成新的图像内容

        Args:
            prompt: 图像描述提示词
            image_url: 参考图 URL
            model: 模型名称，默认 image-01
            resolution: 图像分辨率，默认 "1024x1024"
            num_images: 生成图像数量，默认 1
            reference_type: 参考图类型，默认 character
            timeout: 超时时间，默认 60 秒

        Returns:
            包含生成图像数据的字典
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "resolution": resolution,
            "num_images": num_images,
            "subject_reference": [
                {
                    "type": reference_type,
                    "image_file": image_url,
                }
            ],
        }

        return self._post_generation_request(payload, timeout)


class Image01Turbo:
    BASE_URL = "https://api.minimaxi.com"
    GROUP_ID = ""

    def __init__(self, api_key: str, group_id: str = ""):
        self.api_key = api_key
        self.group_id = group_id or self.GROUP_ID

    def _post_generation_request(self, payload: Dict[str, Any], timeout: int) -> Dict[str, Any]:
        group_param = f"?GroupId={self.group_id}" if self.group_id else ""
        url = f"{self.BASE_URL}/v1/image_generation{group_param}"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
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

    def generate(
        self,
        prompt: str,
        model: str = "image-01",
        resolution: str = "1024x1024",
        num_images: int = 1,
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Image 01 Turbo 极速版图像生成

        效果不变，更快更敏捷

        Args:
            prompt: 图像描述提示词
            model: 模型名称，默认 image-01
            resolution: 图像分辨率，默认 "1024x1024"
            num_images: 生成图像数量，默认 1
            timeout: 超时时间，默认 60 秒

        Returns:
            包含生成图像数据的字典
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "resolution": resolution,
            "num_images": num_images,
        }

        return self._post_generation_request(payload, timeout)

    def generate_from_image(
        self,
        prompt: str,
        image_url: str,
        model: str = "image-01",
        resolution: str = "1024x1024",
        num_images: int = 1,
        reference_type: str = "character",
        timeout: int = 60,
    ) -> Dict[str, Any]:
        """
        Image 01 Turbo 极速版图生图

        基于参考图生成新的图像内容

        Args:
            prompt: 图像描述提示词
            image_url: 参考图 URL
            model: 模型名称，默认 image-01
            resolution: 图像分辨率，默认 "1024x1024"
            num_images: 生成图像数量，默认 1
            reference_type: 参考图类型，默认 character
            timeout: 超时时间，默认 60 秒

        Returns:
            包含生成图像数据的字典
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "resolution": resolution,
            "num_images": num_images,
            "subject_reference": [
                {
                    "type": reference_type,
                    "image_file": image_url,
                }
            ],
        }

        return self._post_generation_request(payload, timeout)
