![image](https://github.com/user-attachments/assets/fc8bdf1e-83d6-4a70-8a49-4a28b52ea026)项目名称：智能助手演示
1.项目简介
1.1 项目背景
该项目是一个智能助手Demo，旨在展示如何利用AI技术处理用户请求，提供语音识别、任务查询等功能。Demo使用阿里云OSS存储文件，通过配置的API进行文件上传和访问。
1.2 项目技术栈
API接口：阿里云OSS，通义听悟, 听悟基于OpenAPI封装后的SDK
2.2 Python 依赖
项目使用 Python 3.x，请确保安装相应版本的 Python。
pip install requests aliyun-python-sdk-core
pip install -r requirements.txt
2.3 阿里云配置
配置阿里云的 AccessKeyId 和 AccessKeySecret
可以通过环境变量或直接在代码中配置（推荐使用环境变量）。
2.4 配置文件
OSS 配置：
配置阿里云 OSS 的 AccessKeyId 和 AccessKeySecret
配置 OSS Bucket 名称和区域信息
启动项目：
python backend/main.py
![image](https://github.com/user-attachments/assets/8c083f70-da10-40b7-a9e2-d83cf0ea4f80)



 常见问题及解决方案
403 错误：权限拒绝
问题：您没有足够的权限访问 OSS，或签名 URL 已过期。
解决方案：检查 OSS 配置和签名有效期，确保阿里云 AccessKeyId 和 AccessKeySecret 配置正确。
503 错误：服务不可用
问题：请求的服务暂时不可用。
解决方案：稍后重试，检查网络连接，确保阿里云服务没有中断。
