# 澄峰祝福视频平台

> “我受够他们了！”澄峰气冲冲地拿着一个小盒子前来。据他所说，他新近部署的服务屡屡被同事称为“安卓服务”，就连他本人也没能幸免成为“安卓人”。前几天晚上的攻击更是莫名其妙，测试完才过一个多小时，数据就丢失了...希望我们找到背后的真相。

于是...这是澄峰利用 AI 制作出的一个祝福视频平台，有一些稀松平常的功能。

---

以上是题目背景。这是一个**有缺陷的** Web 全栈项目，用于 **?CTF 2025** 的 Week 4 取证题“**安卓服务？安卓人？**”。

这个项目的基本结构与主要逻辑均由 Copilot 完成，但环境配置与前后端协调，以及让漏洞点利用达到预期，依然投入了大量的（人工）时间。如果对项目的生成过程感兴趣的话，可以看一眼[提示词](.github/prompts/main.prompt.md)。

在此依然祝各位取证愉快，?CTF 愉快，运维愉快，开发愉快，安卓苹果人都愉快~

## 结构

- [apps/client](apps/client/README.md): Vite + Vue 3 + TS 前端
- [apps/python-server](apps/python-server/README.md): FastAPI + Uvicorn + PyMySQL 后端
- [apps/server](apps/server/README.md): Express + TS 后端（Prisma 连接 MySQL，**已弃用**）

## 快速开始

项目根目录的 [`docker-compose.yml`](docker-compose.yml) 能够初始化一个 MySQL 容器，可按需使用。

建议查看[项目组成](#结构)中给出的 README 文件，按`数据库服务+依赖 -> 后端 -> 前端`的顺序进行配置，更多细节未来可能会补写。
