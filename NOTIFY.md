# 通知说明（Telegram 直发）

本仓库的通知**不**经过 notify-gateway 中间层，**直接通过 Telegram Bot API 发消息**。

只需配两个 GitHub Secret：

| Secret        | 说明 |
| ------------- | ---- |
| `TG_BOT_TOKEN` | Telegram Bot Token（@BotFather 创建 bot 后获取） |
| `TG_CHAT_ID`   | 接收通知的 Chat ID（你的用户 ID 或群组 ID） |

## 怎么配

1. Telegram 找 [@BotFather](https://t.me/BotFather) → `/newbot` → 取 `TG_BOT_TOKEN`
2. 给你的 bot 发一条消息（任意内容），然后浏览器打开：
   ```
   https://api.telegram.org/bot<TG_BOT_TOKEN>/getUpdates
   ```
   找 `"chat":{"id":xxxxx}` 里的数字，就是 `TG_CHAT_ID`
3. 两个值分别填进仓库 **Settings → Secrets → Actions** 的 `TG_BOT_TOKEN` 和 `TG_CHAT_ID`

> 不配通知也能正常续期，`TG_BOT_TOKEN` / `TG_CHAT_ID` 留空时自动跳过通知。

## 通知格式

脚本在三种情况下发通知：

- **token 失效**：❌ 提醒你更新 `MWS_TOKEN`
- **账号下没有对象**：✅ 说明跳过
- **正常续期**：全部成功 ✅ / 有失败 ⚠️，附每个 Bot/Site 的续期结果和总计统计

通知失败只打 `::warning::` 日志，**不阻断续期主流程**。