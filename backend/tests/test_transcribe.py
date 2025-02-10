# backend/test/test_transcribe.py

import unittest
from backend.app.transcribe import transcribe_audio

class TestTranscribe(unittest.TestCase):

    def test_transcribe_audio(self):
        audio_url = "https://intelligent-assistant-demo.oss-cn-beijing.aliyuncs.com/qiangjinjiu.mp3?Expires=1738983164&OSSAccessKeyId=TMP.3KecD2day7MG1EDkL7gPRCbCk5gjATkGU2Qr2gP37FnQ7uSEJZbKEi2bspsxT2jhvsGhEdC9rKyzYggQDWyXbiytrjzwkT&Signature=0fA0q7WfAIrq%2BX9JKtxHdWCqUqY%3D"  # 替换为音频文件的 URL
        response = transcribe_audio(audio_url)
        self.assertIn('TaskId', response)  # 验证响应中是否包含 TaskId

if __name__ == '__main__':
    unittest.main()
