import { Router, Request, Response } from 'express'
import { prisma } from '../services/prisma'
import mysql from 'mysql2/promise'

const router = Router()

// 弱口令登录（CTF 漏洞点）
router.post('/login', async (req: Request, res: Response) => {
  const { username, password } = req.body
  // 漏洞：弱口令 hardcode
  if (username === 'admin' && password === '123456') {
    req.session = { isAdmin: true }
    res.json({ success: true })
  } else {
    res.status(401).json({ error: 'Invalid credentials' })
  }
})

// SQL 注入点：直接拼接 SQL
router.post('/query', async (req: Request, res: Response) => {
  if (!req.session?.isAdmin) return res.status(403).json({ error: 'Forbidden' })
  const { sql } = req.body
  try {
    // 允许任意 SQL 执行
    const pool = mysql.createPool({ uri: process.env.DATABASE_URL })
    const [rows] = await pool.query(sql)
    res.json(rows)
  } catch (e) {
    res.status(500).json({ error: String(e) })
  }
})

export default router
