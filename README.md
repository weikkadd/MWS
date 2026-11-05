## Auto-Renew-MWS

这是一个基于 GitHub Actions 的自动化脚本，用于自动续期 [MWS](https://cloud.m-ws.cc) 服务。

续期逻辑：优先使用Cookie请求api续期，过期自动使用Discord登录获取新的Cookie再续期，并更新新的Cookie到secrets,以供下次续期使用,如果最终结果失败,那就代表该换discord token了

⚠️ 首次运行建议随意设置一个错误的COOKIE触发Discord token登录自动获取新的Cookie，后期自动更新Cookie到Secrets

━━━━━━━━━━━━━━━━━━━━━━
### 🔐 Secrets 配置说明

| Secret 名称         | 是否必填 | 说明                                              |
|---------------------|----------|---------------------------------------------------|
| EMAIL              | ❌ 可选  | 用于通知使用的Email,可随意填写                         |
| COOKIE             | ✅ 必填   | __Host-mrtcloud_token的值,有效期1个月,首次可随意填写   |
| SERVER_IDS         | ✅ 必填   | 服务器id, 切换到网络,点进服务器看请求记录，多个用逗号隔开，例如：9001,9002   |
| DISCORD_TOKEN      | ✅ 必填  | Discord Token，SESSION_TOKEN失效时自动OAuth登录        |
| GH_TOKEN           | ✅ 必填   | GitHub(classic) token,用于自动更新session_token,以ghp_xxx开头|
| NODE_LINK          | ❌ 可选  | 代理链接（如 vless:// vmess:// trojan:// hysteria2:// tuic:// anytls:// socks5:// )|
| TG_BOT_TOKEN       | ❌ 可选  | Telegram Bot Token（用于发送通知）                      |
| TG_CHAT_ID         | ❌ 可选  | Telegram Chat ID（接收通知的用户或群组 ID）               |

━━━━━━━━━━━━━━━━━━━━━━

### 🔐 `NODE_LINK`代理配置说明

| 协议类型         | 格式         | 说明         |
|-----------------|--------------|--------------|
| vless           | vless://uuid@server:port?security=reality&sni=...&type=ws&...   | 可直接使用v2rayN导出的链接                |
| vmess           | vmess://base64encoded...  | 可直接使用v2rayN导出的链接                |
| trojan          | trojan://password@server:port?sni=...&type=ws&...   | 可直接使用v2rayN导出的链接                |
| anytls          | anytls://uuid@server:port... | 可直接使用v2rayN导出的链接                |
| tuic            | tuic://uuid:password@server:port...   | 可直接使用v2rayN导出的链接                |
| hysteria2       | hysteria2://base64@server:port...  | 可直接使用v2rayN导出的链接                |               |
| socks5:         | socks或socks5://user:pass@server:port   | 可直接使用v2rayN导出的链接,不建议  |

━━━━━━━━━━━━━━━━━━━━━━

### SERVER_ID的获取

<img width="800" height="200" alt="image" src="https://github.com/user-attachments/assets/04624397-ff2e-4010-bee0-d704d95bf6ab" />


## 使用

### GitHub Actions 运行步骤

1. Fork 本仓库  
2. 在仓库 Secrets 中配置必填的环境变量,（可选）配置 `TG_BOT_TOKEN`、`TG_CHAT_ID`、`NODE_LINK`
3. 在Actions菜单允许 `I understand my workflows, go ahead and enable them` 按钮
4. Actions菜单里手动触发 `workflow_dispatch`  
5. cron运行时间为每隔6天运行一次，可自行更改时间,避免集中同一时间运行需要排队更久

---

**⚠️ 免责声明**：本脚本仅供学习交流使用，使用者需遵守 [MWS](https://cloud.m-ws.cc) 的服务条款。因使用本脚本造成的任何问题，作者不承担任何责任。
