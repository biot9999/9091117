#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动翻译模块
提供轻量级的自动翻译功能，支持 LibreTranslate
"""

import logging
import requests
from typing import Optional

logger = logging.getLogger("auto_translate")


class AutoTranslator:
    """
    自动翻译器类
    
    默认使用 LibreTranslate，支持自定义 endpoint 和 API key
    提供失败安全的翻译功能，失败时返回原文
    """
    
    def __init__(
        self, 
        provider: str = "libre",
        endpoint: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: int = 5
    ):
        """
        初始化翻译器
        
        Args:
            provider: 翻译提供商，默认 "libre"
            endpoint: LibreTranslate API endpoint，默认 https://libretranslate.com
            api_key: API密钥（可选）
            timeout: 请求超时时间（秒），默认5秒
        """
        self.provider = provider.lower()
        self.endpoint = endpoint or "https://libretranslate.com"
        self.api_key = api_key
        self.timeout = timeout
        
        # 确保 endpoint 不以斜杠结尾
        self.endpoint = self.endpoint.rstrip("/")
        
        logger.info(f"✅ AutoTranslator initialized: provider={self.provider}, endpoint={self.endpoint}")
    
    def translate(self, text: str, source_lang: str = "zh", target_lang: str = "en") -> str:
        """
        翻译文本（中文 -> 英文）
        
        Args:
            text: 要翻译的文本
            source_lang: 源语言代码，默认 "zh"（中文）
            target_lang: 目标语言代码，默认 "en"（英文）
        
        Returns:
            翻译后的文本，失败时返回原文本
        """
        if not text or not text.strip():
            return text
        
        if self.provider != "libre":
            logger.warning(f"⚠️ Unsupported provider: {self.provider}, returning original text")
            return text
        
        try:
            # 构建 LibreTranslate API 请求
            url = f"{self.endpoint}/translate"
            
            payload = {
                "q": text,
                "source": source_lang,
                "target": target_lang,
                "format": "text"
            }
            
            # 如果有 API key，添加到请求中
            if self.api_key:
                payload["api_key"] = self.api_key
            
            # 发送请求
            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout,
                headers={"Content-Type": "application/json"}
            )
            
            # 检查响应状态
            if response.status_code != 200:
                logger.warning(
                    f"⚠️ LibreTranslate API returned status {response.status_code}: {response.text[:100]}"
                )
                return text
            
            # 解析响应
            result = response.json()
            translated_text = result.get("translatedText")
            
            if not translated_text:
                logger.warning(f"⚠️ LibreTranslate API response missing 'translatedText': {result}")
                return text
            
            logger.debug(f"✅ Translated '{text[:50]}...' -> '{translated_text[:50]}...'")
            return translated_text
            
        except requests.exceptions.Timeout:
            logger.warning(f"⚠️ Translation timeout for text: {text[:50]}...")
            return text
        except requests.exceptions.RequestException as e:
            logger.warning(f"⚠️ Translation request failed: {e}")
            return text
        except Exception as e:
            logger.error(f"❌ Unexpected error during translation: {e}")
            return text
