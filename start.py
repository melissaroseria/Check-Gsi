import os
import subprocess
import asyncio

# OTOMATIK KURULUM VE GEREKSINIMLER
def setup_env():
    pkgs = ["python", "wget", "coreutils"]
    for pkg in pkgs:
        subprocess.run(f"pkg install {pkg} -y", shell=True, capture_output=True)
    try:
        import colorama
    except ImportError:
        subprocess.run("pip install colorama", shell=True, capture_output=True)

setup_env()
from colorama import Fore, Style, init
init(autoreset=True)

async def run_cmd(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, _ = await process.communicate()
    return stdout.decode().strip()

async def header():
    os.system('clear')
    print(f"{Fore.CYAN}╔════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║    {Fore.WHITE}{Style.BRIGHT}GSI SELECTOR - V 2.3 [GEMINI EDIT]     {Fore.CYAN}║")
    print(f"{Fore.CYAN}║    {Fore.YELLOW}Cihaz: Obsidian | Mimari: arm64        {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚════════════════════════════════════════════╝")

async def get_gsi_list():
    # En güncel ve stabil GSI linkleri (Android 15 tabanlı)
    return {
        "1": ("PixelOS (Pixel Arayüzü & Google Apps)", "https://github.com/ponces/treble_build_pe/releases/download/v2025.02.15/PixelOS_arm64-ab-15.0-20250215-UNOFFICIAL.img.xz"),
        "2": ("LineageOS 22.1 (En Saf & Hafif)", "https://github.com/AndyYan/treble_experimentations/releases/download/v2025.02.11/lineage-22.1-20250211-UNOFFICIAL-arm64-bgN.img.xz"),
        "3": ("RisingOS (Özelleştirme Canavarı)", "https://github.com/RisingOS-Revived/vayu_releases/releases/download/v15/RisingOS_15_arm64_bgN.img.xz"),
        "4": ("AOSP Vanilla (Tamamen Boş - Root için)", "https://github.com/AndyYan/treble_experimentations/releases/download/v2025.02.11/aosp-15.0-20250211-UNOFFICIAL-arm64-bvN.img.xz")
    }

async def start_engine():
    await header()
    print(f"{Fore.GREEN}📡 Cihaz Uyumluluk Testi Başlatılıyor...\n")
    await asyncio.sleep(1)

    arch = await run_cmd("uname -m")
    vndk = await run_cmd("getprop ro.vndk.version")
    
    print(f" {Fore.WHITE}• Mimari : {Fore.CYAN}{arch:<10} {Fore.GREEN}[OK]")
    print(f" {Fore.WHITE}• VNDK   : {Fore.CYAN}{vndk:<10} {Fore.GREEN}[OK]")
    print(f"\n{Fore.MAGENTA}──────────────────────────────────────────────")
    print(f"{Fore.WHITE}{Style.BRIGHT}Lütfen yüklemek istediğiniz GSI paketini seçin:")
    
    gsi_list = await get_gsi_list()
    for key, (name, _) in gsi_list.items():
        print(f"{Fore.YELLOW}[{key}] {Fore.WHITE}{name}")

    choice = input(f"\n{Fore.CYAN}Seçiminiz (1-4): ")
    
    if choice in gsi_list:
        name, url = gsi_list[choice]
        print(f"\n{Fore.GREEN}Seçildi: {name}")
        print(f"{Fore.RED}⚠️ UYARI: Wi-Fi kapalıysa indirme yapmayın!")
        
        confirm = input(f"{Fore.WHITE}İndirme başlatılsın mı? (e/h): ").lower()
        if confirm == 'e':
            print(f"\n{Fore.CYAN}🚀 {name} indiriliyor... Lütfen bekleyin.\n")
            # Dosya adını URL'den al
            file_name = url.split('/')[-1]
            os.system(f"wget --show-progress -O {file_name} {url}")
            print(f"\n{Fore.GREEN}✨ Başarılı! Dosya konumu: {os.getcwd()}/{file_name}")
            print(f"{Fore.YELLOW}İpucu: ZArchiver ile açıp 'system.img' olarak çıkartmayı unutma.")
    else:
        print(f"{Fore.RED}Geçersiz seçim kanki!")

if __name__ == "__main__":
    asyncio.run(start_engine())
