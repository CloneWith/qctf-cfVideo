from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Request
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List, Optional
import os
from main import engine

router = APIRouter()

@router.get('/requests')
def list_requests():
    with engine.connect() as conn:
        rs = conn.execute(text('SELECT * FROM requests ORDER BY id DESC'))
        return [dict(row._mapping) for row in rs]

@router.post('/requests')
async def create_request(
    request: Request,
    username: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    theme: Optional[str] = Form(None),
    content: Optional[str] = Form(None),
    contact: Optional[str] = Form(None),
    fee: Optional[str] = Form(None),
    attachment: UploadFile = File(None)
):
    # 兼容 JSON body
    if None in [username, email, theme, content, contact, fee]:
        try:
            data = await request.json()
            username = data.get('username')
            email = data.get('email')
            theme = data.get('theme')
            content = data.get('content')
            contact = data.get('contact')
            fee = data.get('fee')
        except Exception:
            raise HTTPException(status_code=422, detail='参数缺失')
    if not all([username, email, theme, content, contact, fee]):
        raise HTTPException(status_code=422, detail='参数缺失')
    attachment_id = None
    if attachment is not None:
        uploads_dir = os.path.join("/srv/http", 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)
        filename: str = attachment.filename or 'upload.bin'
        file_path = os.path.join(uploads_dir, filename)
        with open(file_path, 'wb') as f:
            f.write(await attachment.read())
        with engine.begin() as conn:
            res = conn.execute(text('INSERT INTO attachments (filename) VALUES (:fn)'), { 'fn': attachment.filename })
            attachment_id = res.lastrowid
    with engine.begin() as conn:
        conn.execute(text('''
            INSERT INTO requests (username, email, theme, content, contact, fee, attachment_id)
            VALUES (:username, :email, :theme, :content, :contact, :fee, :attachment_id)
        '''), {
            'username': username,
            'email': email,
            'theme': theme,
            'content': content,
            'contact': contact,
            'fee': float(fee),
            'attachment_id': attachment_id
        })
        conn.execute(text('INSERT INTO budget (reason, amount) VALUES (:r, :a)'), { 'r': "视频订单", 'a': float(fee) })
    return { 'ok': True }

@router.get('/budget')
def list_budget():
    with engine.connect() as conn:
        rs = conn.execute(text('SELECT * FROM budget ORDER BY id DESC'))
        return [dict(row._mapping) for row in rs]

@router.post('/budget')
async def add_budget(request: Request, reason: Optional[str] = Form(None), amount: Optional[str] = Form(None)):
    if reason is None or amount is None:
        try:
            data = await request.json()
            reason = data.get('reason')
            amount = data.get('amount')
        except Exception:
            raise HTTPException(status_code=422, detail='参数缺失')
    if not reason or not amount:
        raise HTTPException(status_code=422, detail='参数缺失')
    with engine.begin() as conn:
        conn.execute(text('INSERT INTO budget (reason, amount) VALUES (:r, :a)'), { 'r': reason, 'a': float(amount) })
    return { 'ok': True }

@router.get('/budget/info')
def budget_info():
    with engine.connect() as conn:
        # 视图模拟：原生 SQL 汇总
        rs = conn.execute(text('SELECT SUM(CASE WHEN amount>0 THEN amount ELSE 0 END) AS `in`, SUM(CASE WHEN amount<0 THEN -amount ELSE 0 END) AS `out` FROM budget'))
        row = rs.fetchone()
        print(row)
        return dict(row._mapping) if row else { 'in': 0, 'out': 0 }

@router.get('/sponsorship')
def list_sponsorship():
    with engine.connect() as conn:
        rs = conn.execute(text('SELECT * FROM sponsorship'))
        return [dict(row._mapping) for row in rs]

@router.post('/sponsorship')
async def add_sponsorship(request: Request, username: Optional[str] = Form(None), amount: Optional[str] = Form(None)):
    if username is None or amount is None:
        try:
            data = await request.json()
            username = data.get('username')
            amount = data.get('amount')
        except Exception:
            raise HTTPException(status_code=422, detail='参数缺失')
    if not username or not amount:
        raise HTTPException(status_code=422, detail='参数缺失')
    with engine.begin() as conn:
        conn.execute(text('INSERT INTO sponsorship (username, amount) VALUES (:u, :a) ON DUPLICATE KEY UPDATE amount = amount + VALUES(amount)'), { 'u': username, 'a': float(amount) })
        conn.execute(text('INSERT INTO budget (reason, amount) VALUES (:r, :a)'), { 'r': "苹果赞助", 'a': float(amount) })
    return { 'ok': True }

@router.get('/users')
def view_users():
    with engine.connect() as conn:
        # 视图 users 模拟：聚合
        sql = text('''
            SELECT r.username, r.email, COUNT(*) AS order_num, IFNULL(s.amount>0, 0) AS is_sponsor
            FROM requests r
            LEFT JOIN sponsorship s ON s.username = r.username
            GROUP BY r.username, r.email
        ''')
        rs = conn.execute(sql)
        return [dict(row._mapping) for row in rs]
