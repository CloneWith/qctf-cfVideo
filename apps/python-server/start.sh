#!/bin/bash
# Python 后端服务启动脚本 (Unix/Linux/macOS)

# 切换到脚本所在目录
cd "$(dirname "$0")"

echo "启动 Python FastAPI 服务..."

# python3 run.py
uvicorn main:app --host 0.0.0.0 --port 5174 --reload
