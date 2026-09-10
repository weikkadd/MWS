# MWS 使用指南

介绍 Discord Bot 和网站的使用入门。平台地址：[cloud.puratya.com](https://cloud.puratya.com)

> **TL;DR**：MWS 的 Bot / 网站启动后有 **7 天倒计时**，到期自动停止。用本仓库的续期脚本（`renew.py` + GitHub Actions）每周一/三/五自动点续期，倒计时永远回满 7 天。本指南是平台本身的使用入门。

---

## 网站 / Bot 创建流程（6 步）

### 1️⃣ 创建 Bot

- 点击仪表盘右下角的 **+** → 添加 Bot
- 输入 Bot 名称（**创建后不可更改**）
- 选择语言：Python / Node.js / TypeScript (Bun) / Go (DiscordGo)

### 2️⃣ 上传文件

- 点击 Bot 卡片打开详情页，上传文件
- 支持单个文件、文件夹和 ZIP；支持拖放上传
- **入口文件优先级**：
  1. `mws.config` 中的 `main=` 指定
  2. `index.ts` / `main.ts`（TypeScript）
  3. `index.js` / `main.js`（Node.js）
  4. `main.py` / `bot.py`（Python）

### 3️⃣ 设置 Token

在「**环境变量**」标签页设置 Discord Token 等信息，**请勿直接写入代码**：

```env
DISCORD_TOKEN=your_token_here
```

代码中获取方式：

```python
# Python
import os
token = os.getenv("DISCORD_TOKEN")
```

```javascript
// Node.js
const token = process.env.DISCORD_TOKEN;
```

### 4️⃣ 启动 Bot

- 点击 Bot 卡片或详情页的 **▶ 启动** 按钮
- 依赖包（pip / npm / bun install）自动安装
- 运行中显示绿色圆点
- 启动失败时日志中会显示错误

### 5️⃣ 查看日志

- 详情页右侧实时显示日志
- 发生错误时页面顶部的 🐛 图标会显示通知
- 可在「**错误日志**」标签页查看完整错误历史

### 6️⃣ 更新计时器

启动 Bot 后开始 **7 天倒计时**：

| 剩余时间 | 状态 |
|----------|------|
| 48h 以上 | 🟢 正常 |
| 24〜48h | 🟠 警告（橙色） |
| 24h 以内 | 🔴 危险（红色） |
| 0h | ⛔ 自动停止 |

点击「**续期（7天）**」按钮重置计时器 —— 本仓库的脚本就是自动帮你点这个。

---

## 支持的语言与依赖安装

只需在各语言的依赖文件中写入要用的库，保存 → 重启即可，启动时自动安装（无需终端操作）。

### Python

- 依赖文件：`requirements.txt`（每行一个包名）
- 入口：`main.py`、`bot.py`
- 启动时自动执行：`pip install`

```text
discord.py
aiohttp
base58
```

### Node.js

- 依赖文件：`package.json` 的 `dependencies`
- 入口：`index.js`、`main.js`
- 启动时自动执行：`npm install`

```json
{
  "dependencies": {
    "discord.js": "^14.14.1"
  }
}
```

### TypeScript / JS（Bun）

- 依赖文件：`package.json` 的 `dependencies`（写法与 Node.js 相同，由 Bun 读取）
- 入口：`index.ts`、`index.js`
- 启动时自动执行：`bun install`

### Go (DiscordGo)

- 依赖文件：`go.mod` 的 `require`（**不要手动改 go.sum**）
- 启动时自动执行：`go mod tidy` / `go build`

```go
require github.com/bwmarrin/discordgo v0.28.1
```

### Rust (Serenity)

- 依赖文件：`Cargo.toml` 的 `[dependencies]`（**不要改 Cargo.lock**）
- 启动时自动执行：`cargo build`

```toml
[dependencies]
serenity = "0.12"
tokio = { version = "1", features = ["full"] }
```

### 常见错误

`ModuleNotFoundError: No module named 'xxx'` = 忘了把 `xxx` 写入 `requirements.txt`。补上并重启即可修复（其他语言同样追加到依赖文件）。
