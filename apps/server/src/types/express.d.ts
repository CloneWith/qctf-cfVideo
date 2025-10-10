import 'express'

declare module 'express-serve-static-core' {
  interface Request {
    session?: {
      isAdmin?: boolean
    }
  }
  interface Response {
    // Add common helpers here if needed later
  }
}
