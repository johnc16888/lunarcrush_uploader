import os
import subprocess
from html_checker import is_valid_lunarcrush_html

def run_step(description, command, error_message=None, required_file=None):
    print(f"🚀 [STEP] {description}")
    try:
        result = subprocess.run(command, check=True)
        if result.returncode != 0:
            raise Exception("Non-zero return code")
    except Exception as e:
        print(f"❌ 错误: {error_message or str(e)}")
        return False

    if required_file and not os.path.exists(required_file):
        print(f"⚠️ 缺少预期文件: {required_file}")
        return False

    return True

# STEP 1: Playwright 刷新并抓取 HTML
if not run_step("自动刷新并抓取 LunarCrush 页面", ["python", "playwright_scraper.py"], "Playwright 执行失败"):
    exit(1)

# STEP 2: 检查 HTML 是否有效
print("🚀 [STEP] 检查抓取 HTML 文件结构...")
try:
    with open("sample_lunarcrush.html", "r", encoding="utf-8") as f:
        html = f.read()
    if not is_valid_lunarcrush_html(html):
        print("⚠️ 页面中未检测到代币卡片结构")
        print("⚠️ 页面结构异常，继续执行主流程（将尝试提取可能的内容）")
except Exception as e:
    print(f"⚠️ HTML 验证失败: {e}")
    print("⚠️ 页面结构异常，继续执行主流程")

# STEP 3: 主逻辑处理（数据提取、分析、Excel、Drive、Telegram）
if not run_step("运行主流程提取 + Excel + Drive + Telegram", ["python", "main.py"], "主流程执行失败"):
    exit(1)

print("✅ 所有步骤执行完成。")
