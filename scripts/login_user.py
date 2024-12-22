#!/usr/bin/env python3

from utils import run_command, generate_random_str


if __name__ == "__main__":
    username = generate_random_str(10)
    run_command(f"useradd -m {username}")

    run_command(f"usermod -aG users {username}")

    run_command(f"sudo -u {username}")

