# 智能助手演示

## 1. 项目简介

### 1.1 项目背景
该项目是一个智能助手 Demo，旨在展示如何利用 AI 技术处理用户请求，提供语音识别、任务查询等功能。Demo 使用阿里云 OSS 存储文件，通过配置的 API 进行文件上传和访问。

### 1.2 项目技术栈
- **API 接口**：阿里云 OSS[https://www.aliyun.com/?spm=a2c4g.11186623.J_4VYgf18xNlTAyFFbOuOQe.d_logo.1abe2c52FeY9Cs]，
- 通义听悟[，https://help.aliyun.com/zh/tingwu/]
- 听悟基于 OpenAPI 封装后的 SDK[https://api.aliyun.com/api-tools/sdk/tingwu?version=2023-09-30&language=python-tea&tab=primer-doc]。

## 2. 配置与安装

### 2.1 Python 依赖
项目使用 Python 3.x，请确保安装相应版本的 Python。

#### 安装依赖：
```bash
pip install requests aliyun-python-sdk-core
pip install -r requirements.txt
```
## 2. 配置与安装

###  阿里云配置
配置阿里云的 **AccessKeyId** 和 **AccessKeySecret**。可以通过环境变量或直接在代码中配置（推荐使用环境变量）。

#### 配置示例：
```bash
export ACCESS_KEY_ID=your_access_key_id
export ACCESS_KEY_SECRET=your_access_key_secret
```
### 配置文件
## OSS 配置：
配置阿里云 OSS 的 AccessKeyId 和 AccessKeySecret
配置 OSS Bucket 名称和区域信息
## 阿里云通义听悟配置：
安装阿里云SDK
```bash
pip install aliyun-python-sdk-core
```

#AccessKey环境变量设置
需要使用您的AccessKey的Id和secret替换如下命令中的YOUR_ACCESS_KEY_ID和YOUR_ACCESS_KEY_SECRET。
```bash
export ALIBABA_CLOUD_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID &&
export ALIBABA_CLOUD_ACCESS_KEY_SECRET=YOUR_ACCESS_KEY_SECRET
```
示例代码：[https://help.aliyun.com/zh/tingwu/offline-transcribe-of-audio-and-video-files?spm=a2c4g.11186623.0.i4]

启动项目：
```bash
python backend/main.py
```

![image](https://github.com/user-attachments/assets/8c083f70-da10-40b7-a9e2-d83cf0ea4f80)

## 常见问题及解决方案

### 403 错误：权限拒绝
问题：您没有足够的权限访问 OSS，或签名 URL 已过期。
解决方案：检查 OSS 配置和签名有效期，确保阿里云 AccessKeyId 和 AccessKeySecret 配置正确。

### 503 错误：服务不可用
问题：请求的服务暂时不可用。
解决方案：稍后重试，检查网络连接，确保阿里云服务没有中断。
## 目前进展
录音文件放在oss文档中，从oss中读取文件有时候会报错403.
