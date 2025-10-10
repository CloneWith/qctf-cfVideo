import { Router, Request, Response } from 'express'
import { prisma } from '../services/prisma.js'
import multer from 'multer'
import path from 'path'
import fs from 'fs'

const router = Router()

// 任意文件上传漏洞点：不限制文件类型和路径
const upload = multer({ dest: path.join(process.cwd(), 'uploads') })

router.get('/', async (_req: Request, res: Response) => {
  // 展示所有订单
  const requests = await prisma.request.findMany({ include: { attachment: true } })
  res.json(requests)
})

router.post('/', upload.single('attachment'), async (req: Request, res: Response) => {
  // 创建订单，允许任意文件上传
  const { username, email, theme, content, contact, fee } = req.body
  let attachmentId: number | undefined
  if (req.file) {
    // 文件信息存入 DB
    const att = await prisma.attachment.create({ data: { filename: req.file.originalname } })
    attachmentId = att.id
    // 文件已存储在 uploads 目录
  }
  const order = await prisma.request.create({
    data: {
      username,
      email,
      theme,
      content,
      contact,
      fee: parseFloat(fee),
      attachmentId
    }
  })
  res.json(order)
})

export default router
