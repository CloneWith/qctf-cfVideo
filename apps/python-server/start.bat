@echo off
REM Python 后端服务启动脚本 (Windows 批处理)
cd /d "%~dp0"
echo 启动 Python FastAPI 服务...
python run.py
pause
