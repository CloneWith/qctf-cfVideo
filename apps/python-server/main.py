from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# MySQL 连接配置
MYSQL_URL = "mysql+pymysql://chenfeng:pingguochenfeng@127.0.0.1:3306/chenfeng-db"
engine = create_engine(MYSQL_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.post("/api/admin/login")
async def admin_login(req: Request):
  username = None
  password = None
  # 尝试 JSON
  try:
    data = await req.json()
    username = data.get("username")
    password = data.get("password")
  except Exception:
    pass
  # 回退到表单
  if username is None or password is None:
    form = await req.form()
    username = form.get("username")
    password = form.get("password")
  if username == "admin" and password == "123456":
    return {"success": True}
  raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/api/admin/query")
async def admin_query(req: Request):
  sql = None
  try:
    data = await req.json()
    sql = data.get("sql")
  except Exception:
    pass
  if not sql:
    form = await req.form()
    sql = form.get("sql")
  with engine.connect() as conn:
    try:
      result = conn.execute(text(str(sql)))
      # 使用 row._mapping 转换为 dict，兼容 SQLAlchemy 2.x
      return [dict(row._mapping) for row in result]
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))


# 健康检查
@app.get("/api/health")
def health():
  return {"status": "ok"}


# 挂载业务路由
try:
  from routes import router as api_router  # 同一目录下导入

  app.include_router(api_router, prefix="/api")
except Exception as e:
  # 路由导入失败不影响基础启动（便于逐步开发）
  print("[warn] routes import failed:", e)
