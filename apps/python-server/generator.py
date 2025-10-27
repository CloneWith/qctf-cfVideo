import random
import string
from faker import Faker

from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Request
from plumbum import local
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from main import engine
from faker.providers import DynamicProvider

MYSQL_URL = "mysql+pymysql://chenfeng:pingguochenfeng@192.168.119.139:3306/chenfeng-db"
engine = create_engine(MYSQL_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def add_budget(reason: str, amount: float):
    with engine.begin() as conn:
        conn.execute(text('INSERT INTO budget (reason, amount) VALUES (:r, :a)'), {'r': reason, 'a': float(amount)})
    return {'ok': True}


def add_sponsorship(username: str, amount: float):
    with engine.begin() as conn:
        conn.execute(text(
            'INSERT INTO sponsorship (username, amount) VALUES (:u, :a) ON DUPLICATE KEY UPDATE amount = amount + VALUES(amount)'),
                     {'u': username, 'a': float(amount)})
        conn.execute(text('INSERT INTO budget (reason, amount) VALUES (:r, :a)'), {'r': "苹果赞助", 'a': float(amount)})
    return {'ok': True}


# 初始化 Faker 生成器
fake = Faker()
localized_fake = Faker(["zh_CN"])

# 赞助数额生成器，同时也用于退款款项
sponsor_values_provider = DynamicProvider(
    provider_name="sponsor_values",
    elements=[50, 100, 10, 666, 1314, 520, 99, 999]
)

budget_name_provider = DynamicProvider(
    provider_name="budget_name",
    elements=[""]
)

spence_name_provider = DynamicProvider(
    provider_name="spence_name",
    elements=["媒体测评", "祝福视频制作", "水军", "招聘费", "物资", "代理", "违约金"]
)

fake.add_provider(sponsor_values_provider)
fake.add_provider(budget_name_provider)
fake.add_provider(spence_name_provider)


def generate_random_username():
    """生成随机用户名"""
    sc = random.randint(1, 2)
    words = fake.name() if sc == 1 else localized_fake.name()
    words = words.replace(" ", "")
    numbers = ''.join(random.choice(string.digits) for _ in range(random.randint(0, 5)))
    return words + numbers


def generate_random_email():
    """生成随机邮箱"""
    local_part = fake.user_name() + ''.join(random.choice(string.digits) for _ in range(random.randint(1, 5)))
    domain_name = fake.domain_name()
    return f"{local_part}@{domain_name}"


def generate_random_content():
    """生成随机内容"""
    words = localized_fake.words(nb=random.randint(5, 20))
    return ''.join(words)


def generate_data(num_records):
    """生成指定数量的随机数据"""
    data = []
    for _ in range(num_records):
        username = generate_random_username()
        email = generate_random_email()
        content = generate_random_content()
        data.append((username, email, content))
    return data


def gen_sponsorship(num):
    data = []
    for _ in range(num):
        username = generate_random_username()
        value = fake.sponsor_values()
        data.append((username, value))
    return data


def gen_budget(num):
    data = []
    for _ in range(num):
        sym = 1 if random.randint(0, 64) > 32 else -1
        amount = random.randint(1, 10)
        reason = "直播间礼物" if sym == 1 else "未成年退款"
        # reason = generate_random_username()
        value = fake.sponsor_values() * amount
        if sym == -1:
            value *= -1
        data.append((reason, value))
    return data


if __name__ == "__main__":
    num_records = 250
    random_data = gen_sponsorship(num_records)
    for record in random_data:
        print((record[0], record[1]))
        add_sponsorship(record[0], record[1])
