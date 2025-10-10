import { Router, Request, Response } from 'express'
import { prisma } from '../services/prisma.js'

const router = Router()

router.get('/', async (_req: Request, res: Response) => {
  try {
    const users = await prisma.user.findMany({ take: 10 })
    res.json(users)
  } catch (e) {
    res.status(500).json({ error: 'DB error', detail: String(e) })
  }
})

export default router
