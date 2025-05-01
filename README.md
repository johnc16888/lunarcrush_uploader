# 🌕 LunarCrush Uploader 自动化系统

该系统自动从 [LunarCrush 热门代币页面](https://lunarcrush.com/categories/cryptocurrencies?metric=alt_rank&reverse=) 抓取代币数据，筛选符合条件的项目（AltRank 前 50 且 Engagement > 1M），并执行以下操作：

- ✅ 自动刷新页面并保存 HTML
- ✅ 自动解析代币数据（价格、涨幅、AltRank、Engagement、Mentions 等）
- ✅ 自动生成 Excel 报告
- ✅ 自动上传至 Google Drive（按月分类）
- ✅ 自动推送 Telegram 消息（仅推送符合条件的代币）

---

## 🚀 一键运行方式

运行以下命令，即可完成全部流程：

```bash
python run_all.py
```

---

## 🛠 项目结构说明

| 文件名                  | 功能 |
|-------------------------|------|
| `run_all.py`            | 一键执行整个流程 |
| `playwright_scraper.py` | 使用 Playwright 自动刷新并抓取网页 |
| `html_checker.py`       | 验证 HTML 是否为有效结构 |
| `main.py`               | 提取数据 + 上传 + 推送主流程 |
| `html_parser.py`        | 从 HTML 中提取代币信息 |
| `excel_exporter.py`     | 将数据写入 Excel 文件 |
| `drive_uploader.py`     | 上传 Excel 到 Google Drive |
| `telegram_notifier.py`  | 推送 Telegram 消息 |
| `sample_lunarcrush.html`| 抓取结果保存文件（自动生成） |
| `env_example.txt`       | 环境变量参考文件 |
| `data/json/`            | 缓存数据目录（保留即可） |

---

## ⚙️ Render 平台部署

1. 将项目上传至 GitHub
2. 在 [Render](https://render.com/) 创建 Python Cron Job 服务
3. 设定命令：
```bash
python run_all.py
```
4. 设置环境变量：

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

5. 上传你的 Google Drive 凭证 `credentials.json` 到项目根目录（不要上传至 GitHub）

---

## 📦 依赖安装

首次运行请执行：

```bash
pip install -r requirements.txt
playwright install
```

---

## 🧪 测试建议

- 先运行 `python playwright_scraper.py` 确保 HTML 能正确抓取
- 再运行 `python html_checker.py` 确保结构正常
- 最后运行 `python run_all.py` 查看是否能完成整个流程

---

如需修改筛选逻辑、增加字段、分析信号，请联系开发者或提交 Issue。