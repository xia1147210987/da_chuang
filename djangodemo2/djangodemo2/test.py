import subprocess
import webbrowser

# 要执行的命令列表
commands = [
    "python manage.py makemigrations",
    "python manage.py migrate",
    "python manage.py runserver"
]

# 设置标志来检查命令执行是否成功
all_commands_successful = True

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
