import { Router, Request, Response } from 'express'
import { prisma } from '../services/prisma'

const router = Router()

router.get('/', async (_req: Request, res: Response) => {
  // 展示所有赞助记录
  const sponsors = await prisma.sponsorship.findMany()
  res.json(sponsors)
})

router.post('/', async (req: Request, res: Response) => {
  // 新增赞助记录
  const { username, amount } = req.body
  const sponsor = await prisma.sponsorship.upsert({
    where: { username },
    update: { amount: { increment: parseFloat(amount) } },
    create: { username, amount: parseFloat(amount) }
  })
  res.json(sponsor)
})

export default router
