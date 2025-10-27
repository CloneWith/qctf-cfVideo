# Python Backend Server

The backend currently used. Uses Uvicorn + FastAPI + PyMySQL modules.

## Usage

### Database Preparation

You need to set the database up first. The project uses **MariaDB** as the database manage system, and you could use MySQL though.

By default, to simulate our expected environment:

- The database server should run on port 3306.
- We have a schema naming `chenfeng-db`.
- We have a user calling `chenfeng`, who has **all** (yeah, that's right) privileges of the schema above.
- The database service allows all remote logins, which means you should add an access entry like `'chenfeng'@'%'`.

### Launching

Install dependencies:

```bash
pip install -r ./requirements.txt
```

Start the backend server:

- The `run.py` script is recommended and supported for the majority of platforms.
- On Windows, you can use `start.bat`.
- On Linux, you can use `start.sh`.
