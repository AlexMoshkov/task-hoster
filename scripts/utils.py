import subprocess
import string
import random


def run_command(cmd: str):
    _ = subprocess.run(
        cmd,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

def generate_random_str(length: int) -> str:
    chs = string.ascii_letters + string.digits
    return ''.join(random.choice(chs) for _ in range(length))

