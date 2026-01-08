import asyncio
import edge_tts

# 配置参数
TEXT = "你好，欢迎使用 Edge TTS！这是由 Python 调用生成的语音。"
VOICE = "zh-CN-XiaoxiaoNeural"  # 中文女声
OUTPUT_FILE = "output.mp3"


async def main():
    # 创建通信对象
    communicate = edge_tts.Communicate(text=TEXT, voice=VOICE)

    # 保存为音频文件
    await communicate.save(OUTPUT_FILE)
    print(f"音频已保存为 {OUTPUT_FILE}")


# 运行异步函数
if __name__ == "__main__":
    asyncio.run(main())