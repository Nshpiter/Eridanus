# 基础镜像：用 Python 3.11 官方镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY . .

# 设置 PyPI 镜像源（加速国内下载）
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 运行 main.py
CMD ["python", "main.py"]
