import { Router, Request, Response } from 'express'
import { prisma } from '../services/prisma.js'

const router = Router()

router.get('/', async (_req: Request, res: Response) => {
  // 展示所有收支记录
  const budget = await prisma.budget.findMany()
  res.json(budget)
})

router.post('/', async (req: Request, res: Response) => {
  // 新增收支记录
  const { reason, amount } = req.body
  const record = await prisma.budget.create({ data: { reason, amount: parseFloat(amount) } })
  res.json(record)
})

// budget_info 视图（用原生 SQL 查询，方便 CTF 注入点）
router.get('/info', async (_req: Request, res: Response) => {
  // SQL 注入点：拼接 SQL 字符串
  const sql = 'SELECT SUM(CASE WHEN amount > 0 THEN amount ELSE 0 END) AS `in`, SUM(CASE WHEN amount < 0 THEN -amount ELSE 0 END) AS `out` FROM budget'
  const [info] = await prisma.$queryRawUnsafe(sql)
  res.json(info)
})

export default router
