#!/usr/bin/env python3
"""直接通过 Telegram Bot API 发送通知。

只需配两个 Secret：TG_BOT_TOKEN、TG_CHAT_ID
不依赖 notify-gateway，续期结果直接发到你的 Telegram。
"""

from __future__ import annotations

import json
import os
import urllib.request
import urllib.error

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "").strip()
TG_CHAT_ID = os.environ.get("TG_CHAT_ID", "").strip()

TG_API = "https://api.telegram.org/bot{}/sendMessage"

LEVEL_EMOJI = {
    "success": "✅",
    "partial": "⚠️",
    "failed": "❌",
}


def _format_message(title, content, level="success", details=None):
    """把续期结果格式化成 Telegram 消息文本。"""
    emoji = LEVEL_EMOJI.get(level, "📢")
    parts = ["{} {}".format(emoji, title)]
    if content:
        parts.append("")
        parts.append(content)
    if details and isinstance(details, dict):
        total = details.get("total", 0)
        success = details.get("success", 0)
        failed = details.get("failed", 0)
        if total:
            parts.append("")
            parts.append("📊 总计: {} 成功, {} 失败".format(success, failed))
    return "\n".join(parts)


def notify(title, content, level="success", details=None, source="puratya-renew"):
    """直接通过 Telegram Bot API 发消息。"""
    if not TG_BOT_TOKEN or not TG_CHAT_ID:
        print("::warning::TG_BOT_TOKEN 或 TG_CHAT_ID 未设置，跳过通知")
        return {"ok": False, "skipped": True}

    text = _format_message(title, content, level, details)
    if len(text) > 4090:
        text = text[:4090] + "\n..."

    payload = json.dumps({
        "chat_id": TG_CHAT_ID,
        "text": text,
    }).encode("utf-8")

    req = urllib.request.Request(
        TG_API.format(TG_BOT_TOKEN),
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        print("::warning::Telegram 通知失败 HTTP {}: {}".format(e.code, body))
        return {"ok": False, "error": body}
    except Exception as e:
        print("::warning::Telegram 通知失败: {}".format(e))
        return {"ok": False, "error": str(e)}


if __name__ == "__main__":
    print(json.dumps(
        notify(
            "MWS 续期完成",
            "续期完成报告",
            level="partial",
            details={
                "total": 5, "success": 3, "failed": 2,
                "details": [
                    {"id": "bot_001", "name": "Bot A", "status": "success"},
                    {"id": "bot_002", "name": "Bot B", "status": "failed", "error": "HTTP 403"},
                ],
            },
        ),
        ensure_ascii=False, indent=2,
    ))