import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 获取环境变量
ACCESS_KEY_ID = os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET')

if not ACCESS_KEY_ID or not ACCESS_KEY_SECRET:
    raise ValueError("Access Key ID and Secret must be set in the environment variables.")
