# 基础镜像：Python 3.11 slim
FROM python:3.11-slim

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    nodejs \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . .

# 安装 Python 依赖（可选加速）
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 默认运行
CMD ["python", "main.py"]
