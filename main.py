
from backend.app.transcribe import transcribe_audio, check_task_status, get_transcription_text
from backend.utils.oss import download_file


def main():
    # 你的音频文件的公网 URL
    audio_url = "https://your-bucket-name.oss-cn-beijing.aliyuncs.com/qiangjinjiu.mp3"

    print("🚀 提交语音转写任务...")
    task_id = transcribe_audio(audio_url)

    if task_id:
        # 轮询任务状态，直到任务完成
        transcription_url = check_task_status(task_id)

        if transcription_url:
            print(f"📝 获取转录文本: {transcription_url}")
            transcription_text = get_transcription_text(transcription_url)

            if transcription_text:
                print("\n🎉 ===== 语音转写完成 =====")
                print(transcription_text)

    else:
        print("❌ 任务创建失败，请检查 API 调用是否正确。")


if __name__ == '__main__':
    main()
