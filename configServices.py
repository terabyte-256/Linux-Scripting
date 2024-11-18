from customfunctions import run_commands
from customfunctions import run_command
from customfunctions import cprint
from customfunctions import confirmation

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

def openssh_config() -> None:
    """
    Configs ssh
    """
    run_commands([
        "sed -i 's/LoginGraceTime .*/LoginGraceTime 60/g' /etc/ssh/sshd_config",
        "sed -i 's/PermitRootLogin .*/PermitRootLogin no/g' /etc/ssh/sshd_config",
        "sed -i 's/Protocol .*/Protocol 2/g' /etc/ssh/sshd_config",
        "sed -i 's/#PermitEmptyPasswords .*/PermitEmptyPasswords no/g' /etc/ssh/sshd_config",
        "sed -i 's/PasswordAuthentication .*/PasswordAuthentication yes/g' /etc/ssh/sshd_config",
        "sed -i 's/X11Forwarding .*/X11Forwarding no/g' /etc/ssh/sshd_config"
    ])
    run_command("systemctl restart openssh-server", capture_output=False)
    cprint("Openssh configured", color="green")

    confirmation()
    
def mysql_config() -> None:
    """
    Configs mysql
    """
    run_commands([
        "sed -i 's/bind-address .*/bind-address = 127.0.0.1/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/skip-external-locking .*/skip-external-locking = 1/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/key_buffer_size .*/key_buffer_size = 32M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/max_allowed_packet .*/max_allowed_packet = 16M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/thread_stack .*/thread_stack = 256K/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/thread_cache_size .*/thread_cache_size = 8/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/query_cache_limit .*/query_cache_limit = 1M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/tmp_table_size .*/tmp_table_size = 16M/g' /etc/mysql/mysql.conf.d/mysqld.cnf",
        "sed -i 's/max_heap_table_size .*/max_heap_table_size = 16M/g' /etc/mysql/mysql.conf.d/mysqld.cnf"
    ])
    run_command("systemctl restart mysql", capture_output=False)
    cprint("Mysql configured", color="green")

    confirmation()

def apache2_config() -> None:
    """
    Configs apache2
    """
    run_commands([
        "sed -i 's/ServerTokens .*/ServerTokens Prod/g' /etc/apache2/conf-available/security.conf",
        "sed -i 's/ServerSignature .*/ServerSignature Off/g' /etc/apache2/conf-available/security.conf"
    ])
    run_command("systemctl restart apache2", capture_output=False)
    cprint("Apache2 configured", color="green")

    confirmation()

def samba_config() -> None:
    """
    Configs samba
    """
    return

def vsftpd_config() -> None:
    """
    Configs vsftpd
    """
    return

def x11vnc_config() -> None:
    """
    Configs x11vnc
    """
    return
"""Todo:
- create config functions for each service
    - openssh-server
        - done
    - openssh-client
        - done
    - mysql
        - done
    - apache2
        - done
    - samba 
        - func declared needs to be done
    - vsftpd 
        - func declared needs to be done
    - x11vnc 
        - func declared needs to be done
"""