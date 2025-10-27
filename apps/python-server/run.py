#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 后端服务启动脚本
用于替代命令行启动，便于维护和配置管理
"""

import uvicorn
import os
import sys
from pathlib import Path

# 确保当前目录在 Python 路径中
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    """启动 FastAPI 服务"""

    # 服务配置
    config = {
        "app": "main:app",
        "host": "0.0.0.0",
        "port": 5174,
        "reload": True,
        "reload_dirs": [str(current_dir)],
        "log_level": "info",
        # 开发模式配置
        "access_log": True,
        "use_colors": True,
    }

    # 从环境变量读取配置（可选）
    host_env = os.getenv("PYTHON_SERVER_HOST")
    if host_env:
        config["host"] = host_env

    port_env = os.getenv("PYTHON_SERVER_PORT")
    if port_env:
        config["port"] = int(port_env)

    reload_env = os.getenv("PYTHON_SERVER_RELOAD")
    if reload_env:
        config["reload"] = reload_env.lower() == "true"

    print("=== Python FastAPI 服务启动 ===")
    print(f"服务地址: http://{config['host']}:{config['port']}")
    print(f"API 文档: http://{config['host']}:{config['port']}/docs")
    print(f"热重载: {'开启' if config['reload'] else '关闭'}")
    print("按 Ctrl+C 停止服务\n")

    try:
        # 启动服务
        uvicorn.run(**config)
    except KeyboardInterrupt:
        print("\n服务已停止")
    except Exception as e:
        print(f"启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
