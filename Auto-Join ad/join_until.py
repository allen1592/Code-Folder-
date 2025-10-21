import subprocess
import sys

def join_domain(domain, username, password, computer_name):
    try:
        command = [
            "netdom", "join", computer_name,
            "/domain:{}".format(domain),
            "/userd:{}".format(username),
            "/passwordd:{}".format(password),
            "/reboot"
        ]

        subprocess.run(command, check=True)
        print(f"Successfully joined the domain {domain} as {computer_name}. The machine will reboot now.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to join the domain: {e}")
        sys.exit(1)