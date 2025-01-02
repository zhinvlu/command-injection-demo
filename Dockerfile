# 使用官方的Python运行时作为基础镜像
FROM python:3.14.0a3-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录中
COPY . /app

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用运行的端口
EXPOSE 5000

# 设置容器启动时执行的命令
CMD ["python", "commandinjection.py"]
