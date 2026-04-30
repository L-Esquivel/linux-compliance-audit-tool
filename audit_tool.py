import subprocess
import os

# Definición de colores para la salida en terminal
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def check_ssh_root_login():
    """CIS-1.1: Verifica si el login de root por SSH está deshabilitado."""
    print("Checking CIS-1.1: Disable SSH Root Login...")
    try:
        # Ejecuta grep para buscar la configuración en el archivo de sshd
        result = subprocess.check_output("grep '^PermitRootLogin' /etc/ssh/sshd_config", shell=True).decode()
        if "no" in result.lower():
            print(f"{GREEN}[PASS]{RESET} Root login is disabled.")
            return "PASS"
        else:
            print(f"{RED}[FAIL]{RESET} Root login is enabled or not explicitly set to 'no'.")
            return "FAIL"
    except subprocess.CalledProcessError:
        print(f"{YELLOW}[WARN]{RESET} PermitRootLogin directive not found. Default might be risky.")
        return "WARN"

def check_shadow_permissions():
    """CIS-1.2: Verifica que los permisos de /etc/shadow sean restrictivos (640 o menos)."""
    print("\nChecking CIS-1.2: Permissions on /etc/shadow...")
    stat = os.stat('/etc/shadow')
    mode = oct(stat.st_mode & 0o777)
    
    # El estándar CIS sugiere que solo root pueda leerlo (600 o 640)
    if mode in ['0o640', '0o600', '0o400']:
        print(f"{GREEN}[PASS]{RESET} Permissions are secure ({mode}).")
        return "PASS"
    else:
        print(f"{RED}[FAIL]{RESET} Permissions are too permissive ({mode}).")
        return "FAIL"

def run_audit():
    print(f"{'='*40}")
    print("LINUX COMPLIANCE AUDIT TOOL - BETA")
    print(f"{'='*40}\n")
    
    results = {
        "CIS-1.1": check_ssh_root_login(),
        "CIS-1.2": check_shadow_permissions()
    }
    
    print(f"\n{'='*40}")
    print("AUDIT SUMMARY")
    for check, status in results.items():
        print(f"{check}: {status}")
    print(f"{'='*40}")

if __name__ == "__main__":
    # Nota: Este script debe ejecutarse con sudo para acceder a /etc/shadow
    if os.getuid() != 0:
        print(f"{RED}[ERROR]{RESET} This script must be run as root (sudo).")
    else:
        run_audit()
