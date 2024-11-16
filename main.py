import getpass
from customfunctions import *


def main():
    ufw()  # Gets Firewall

    update()  # Updating system

    change_password(input("Enter a password (Default: CyberPatriot123!@#): "))  # Changing user passwords

    remove_unauthorized_users()  # Removes unauthorized users

    create_new_users()  # Creates new users

    secure_root()  # Secures root

    secure_etc_files()  # Secures etc files

    remove_hacking_tools()  # Removes hacking tools

    possible_critical_services()  # Removes or keeps possible critical services in ReadMe


def ufw() -> None:
    """
    Installs ufw if it isn't already installed

    Enables ufw and checks if it is running

    :return: None
    """
    run_commands(["apt-get install ufw", "ufw enable", "ufw status"])
    cprint("ufw installed and enabled", color="green")

    confirmation()


def update() -> None:
    """
    Running update and upgrade to update the system

    Getting unattended-upgrades to enable automatic updates

    :return: None
    """
    cprint("Updating system...", color="yellow")
    run_commands(["apt update -y", "apt upgrade -y"])
    cprint("System updated", color="green")

    confirmation(False)

    cprint("Installing unattended-upgrades...", color="yellow")
    run_commands(["apt-get install unattended-upgrades -y", "systemctl start unattended-upgrades"])
    cprint("Auto updates started", color="green")

    confirmation()


def media_files() -> None:
    """
    Finds all media files
    :return:
    """
    cprint("Pictures: ", color="magenta", bold=True)
    for extension in "jpeg jpg png tiff gif svg bmp webp".split(" "):
        run_command(f"locate /home *.{extension}")
    confirmation()

    cprint("Videos: ", color="magenta", bold=True)
    for extension in "mov mp4 wmv avi mkv webm flv avchd".split(" "):
        run_command(f"locate /home *.{extension}")
    confirmation()

    cprint("Audio: ", color="magenta", bold=True)
    for extension in "wav mp3 aiff aac alac m4a flac wma".split(" "):
        run_command(f"locate /home *.{extension}")
    confirmation()

    cprint("Others: ", color="magenta", bold=True)
    for extension in "tar.gz php".split(" "):
        run_command(f"locate / *.{extension}")
    confirmation()


def change_password(password: str = "CyberPatriot123!@#") -> None:
    """
    :param password: Password to change to (Default: CyberPatriot123!@#)

    :return: None
    """
    return



def remove_unauthorized_users() -> None:
    """
    Removes unauthorized users not listed in normal_users.txt

    Valid users are provided in the CyberPatriot ReadMe file

    :return: None
    """
    normal_users = open("normal_users.txt", "r").read().splitlines()
    sudoers = open("admins.txt", "r").read().splitlines()

    if not normal_users or not sudoers:
        cprint("ADD USERS TO normal_users.txt AND admins.txt BEFORE DOING THIS COMMAND", color="red", bold=True)
        confirmation()
        return

    confirmation()


def create_new_users() -> None:
    """
    Creates users from normal_users.txt
    """
    return
    # new_users = open("new_users.txt", "r").read().splitlines()
    #
    # confirmation()


def secure_root() -> None:
    """
    Secures Root

    :return: None
    """
    cprint("Secure Root...", color="yellow")
    run_command("sudo passwd -l root")
    cprint("Root Secured", color="green")

    confirmation()


def secure_etc_files() -> None:
    """
    Securing /etc/shadow
    
    :return: None
    """
    run_commands(["sudo chmod 640 /etc/shadow", "ls -l /etc/shadow",
                  "sudo chmod 644 /etc/passwd", "ls -l /etc/passwd",
                  "sudo chmod 644 /etc/group", "ls -l /etc/group",
                  "sudo chmod 644 /etc/gshadow", "ls -l /etc/gshadow"])

    confirmation()


def remove_hacking_tools() -> None:
    """
    Removes all hacking tools

    :return: None
    """
    hacking_tools = ["john", "hydra", "nginx", "wireshark", "ophcrack", "nikto", "tcpdump", "nmap", "zenmap", "deluge"]
    for i in range(len(hacking_tools)):
        cprint(f"Removing {hacking_tools[i]}", color="blue")
        run_command(f"apt-get purge {hacking_tools[i]} -y", capture_output=False)

    run_command("apt-get autoremove -y", capture_output=False)
    cprint("Hacking tools removed!", color="green")

    confirmation()


def possible_critical_services() -> None:
    """
    Removes unneeded services that aren't listed on the ReadMe

    Installs and updates services that are needed

    :return: None
    """
    services = ["openssh-server", "openssh-client", "samba", "apache2", "vsftpd", "snmp", "x11vnc"]
    exclusion = input("Critical services to add to exclusion list (must be program name and seperated by comma): ").split(", ")

    for i in range(len(services)):
        if services[i] not in exclusion:
            cprint(f"Removing {services[i]}", color="yellow")
            run_command(f"apt-get purge {services[i]} -y", capture_output=False)
            cprint(f"Removed {services[i]}", color="green")
        else:
            cprint(f"Ignoring {services[i]}...", color="blue")

    cprint("Finishing up...", color="yellow")
    run_command("apt-get autoremove -y")
    cprint("Unneeded Services Removed!", color="green")

    for i in range(len(exclusion)):
        cprint(f"Installing and upgrading {exclusion[i]}", color="yellow")
        run_commands([f"apt-get install {exclusion[i]} -y", f"apt-get upgrade {exclusion[i]}"], capture_output=False)
        cprint(f"Done installing and upgrading {exclusion[i]}", color="green")

    cprint("Critical Services Installed!", color="green")
    cprint(f"\nMake sure to SECURE these services: {', '.join(exclusion)}", color="red", bold=True, underline=True)

    confirmation()

def config_sysctl() -> None:
    """
    Configs sysctl

    :return: None
    """
    run_commands([
        "sed -i '$a net.ipv6.conf.all.disable_ipv6 = 1' /etc/sysctl.conf",
        "sed -i '$a net.ipv6.conf.default.disable_ipv6 = 1' /etc/sysctl.conf",
        "sed -i '$a net.ipv6.conf.lo.disable_ipv6 = 1' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.all.rp_filter=1' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.all.accept_source_route=0' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_max_syn_backlog = 2048' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_synack_retries = 2' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_syn_retries = 5' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.tcp_syncookies=1' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.ip_foward=0' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.all.send_redirects=0' /etc/sysctl.conf",
        "sed -i '$a net.ipv4.conf.default.send_redirects=0' /etc/sysctl.conf"
    ])

    run_command("sysctl -p", capture_output=False)
    cprint("Sysctl configured", color="green")

    confirmation()

# Todo: create config functions for each service
# -openssh-server
# -openssh-client
# -mysql
# -apache2
# -samba?
# -vsftpd?
# -x11vnc?
# Todo: Password Policy config function

if __name__ == "__main__":
    _username = getpass.getuser()
    _password = getpass.getpass()

    main()
