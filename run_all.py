import subprocess
import sys

def run_script(name):
    print(f"▶️ 运行: {name}")
    result = subprocess.run([sys.executable, name], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"⚠️ 错误信息: {result.stderr}")

if __name__ == "__main__":
    print("🚀 [STEP 1] 自动刷新并抓取 LunarCrush 页面...")
    run_script("playwright_scraper.py")

    print("\n🔍 [STEP 2] 检查抓取 HTML 文件结构...")
    run_script("html_checker.py")

    print("\n📊 [STEP 3] 运行主流程提取 + Excel + Drive + Telegram...")
    run_script("main.py")

    print("\n✅ 所有步骤执行完成。")