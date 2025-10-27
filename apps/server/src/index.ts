import 'dotenv/config'
import express from 'express'
import cors from 'cors'
import healthRouter from './routes/health'
import usersRouter from './routes/users'
import requestsRouter from './routes/requests'
import budgetRouter from './routes/budget'
import sponsorshipRouter from './routes/sponsorship'
import adminRouter from './routes/admin'

const app = express()
app.use(cors())
app.use(express.json())

app.use('/api/health', healthRouter)
app.use('/api/users', usersRouter)
app.use('/api/requests', requestsRouter)
app.use('/api/budget', budgetRouter)
app.use('/api/sponsorship', sponsorshipRouter)
app.use('/api/admin', adminRouter)

const port = Number(process.env.PORT ?? 5174)
app.listen(port, () => {
  console.log(`[server] listening on http://localhost:${port}`)
})
