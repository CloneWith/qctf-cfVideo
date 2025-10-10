# 全栈模板：Vue 3 + Vite + TypeScript（前端）/ Express + TypeScript + Prisma + MySQL（后端）

该仓库是一个 Monorepo，包含前端与后端两个应用，采用 npm workspaces 管理。

## 结构

- apps/client: Vite + Vue 3 + TS 前端
- apps/server: Express + TS 后端（Prisma 连接 MySQL）
- .vscode: VS Code 任务配置
- docker-compose.yml: 本地 MySQL 服务

## 快速开始（Windows PowerShell）

1. 安装依赖

```powershell
npm install
```

1. 启动 MySQL（可选，若你已有实例则跳过）

```powershell
docker compose up -d db
```

1. 初始化数据库（在提供 .env 后）

```powershell
npm run prisma:generate -w apps/server
npm run prisma:migrate -w apps/server
```

1. 开发模式（前后端并行）

```powershell
npm run dev
```

## 环境变量（后端）

在 `apps/server/.env` 中设置：

```env
DATABASE_URL="mysql://USER:PASSWORD@localhost:3306/app_db"
PORT=5174
```

请将 USER/PASSWORD 替换为你的实际值。

## 常用脚本

- 根目录
  - `npm run dev`: 并行启动 client 与 server
  - `npm run build`: 构建前后端
  - `npm run start`: 启动后端（构建后）
- apps/server
  - `npm run prisma:generate`: 生成 Prisma Client
  - `npm run prisma:migrate`: 运行迁移

## 后续配置

- 你稍后提供的数据库与业务细节将用于更新 `schema.prisma`、迁移与 API 路由。
- 若需要 Docker 化前后端，可在后续添加对应服务。
