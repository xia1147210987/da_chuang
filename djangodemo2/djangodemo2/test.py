import subprocess
import webbrowser
import mysql.connector
import importlib.util

# 要执行的命令列表
commands = [
    "python manage.py makemigrations",
    "python manage.py migrate",
    "python manage.py runserver"
]

# 设置标志来检查命令执行是否成功
all_commands_successful = True



# 检查并安装 Django
try:
    import django
except ImportError:
    print("Django not found. Installing Django...")
    subprocess.run(["pip", "install", "django==2.1.4"])
    print("Django installed successfully!")

# 检查并安装 OS 库 (Python 标准库中的一部分，无需额外安装)

# 检查并安装 pymysql
try:
    import pymysql
except ImportError:
    print("pymysql not found. Installing pymysql...")
    subprocess.run(["pip", "install", "pymysql"])
    print("pymysql installed successfully!")

# 检查并安装 json 库 (Python 标准库中的一部分，无需额外安装)

# 检查并安装 mysql-connector-python
try:
    import mysql.connector
except ImportError:
    print("mysql-connector-python not found. Installing mysql-connector-python...")
    subprocess.run(["pip", "install", "mysql-connector-python"])
    print("mysql-connector-python installed successfully!")


# 连接到 MySQL 服务器
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
)

# 创建数据库游标
cursor = conn.cursor()

# 检查数据库是否存在
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
database_exists = False
for database in databases:
    if database[0] == 'sjk':
        database_exists = True
        break

# 如果数据库不存在，则创建数据库
if not database_exists:
    cursor.execute("CREATE DATABASE sjk")
    print("Database 'sjk' created successfully!")
else:
    print("Database 'sjk' already exists.")

# 关闭游标和数据库连接
cursor.close()
conn.close()

# 依次执行每个命令
for cmd in commands:
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，将标志设置为 False
        print(f"命令'{cmd}'执行失败:", e)
        all_commands_successful = False
        break

# 如果所有命令都执行成功，则跳转网页
if all_commands_successful:
    webbrowser.open('http://127.0.0.1:8000/index')
