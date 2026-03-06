import os
import subprocess
import asyncio
from colorama import Fore, Style, init

init(autoreset=True)

async def run_cmd(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, _ = await process.communicate()
    return stdout.decode().strip()

async def get_device_report():
    os.system('clear')
    print(f"{Fore.MAGENTA}📋 CİHAZ ANALİZ RAPORU - OBSIDIAN EDITION")
    print(f"{Fore.MAGENTA}═" * 45)
    
    # Detaylı bilgi toplama
    arch = await run_cmd("uname -m")
    vndk = await run_cmd("getprop ro.vndk.version")
    brand = await run_cmd("getprop ro.product.brand")
    model = await run_cmd("getprop ro.product.model")
    security = await run_cmd("getprop ro.build.version.security_patch")
    
    print(f"{Fore.WHITE}• Üretici/Model : {Fore.CYAN}{brand.upper()} {model}")
    print(f"{Fore.WHITE}• Mimari        : {Fore.CYAN}{arch}")
    print(f"{Fore.WHITE}• VNDK Seviyesi : {Fore.CYAN}{vndk}")
    print(f"{Fore.WHITE}• Güvenlik Yaması: {Fore.CYAN}{security}")
    
    # Uyumluluk Kontrolü
    print(f"\n{Fore.YELLOW}🛠 UYUMLULUK DENETİMİ:")
    if arch == "aarch64" and vndk:
        print(f"{Fore.GREEN}✅ Cihazınız GSI mimarisine %100 uygundur.")
        print(f"{Fore.GREEN}💡 NOT: Android sürümü ne olursa olsun 'arm64' paketlerini kurabilirsiniz.")
    else:
        print(f"{Fore.RED}❌ Kritik uyumsuzluk tespit edildi!")

    print(f"{Fore.MAGENTA}═" * 45)
    input(f"\n{Fore.YELLOW}Devam etmek için ENTER'a bas kanki...")

async def start_engine():
    while True:
        os.system('clear')
        print(f"{Fore.CYAN}╔════════════════════════════════════════════╗")
        print(f"{Fore.CYAN}║    {Fore.WHITE}{Style.BRIGHT}GSI SELECTOR - V 2.7 [ENGINEER]        {Fore.CYAN}║")
        print(f"{Fore.CYAN}╚════════════════════════════════════════════╝")
        print(f"{Fore.YELLOW}[1] {Fore.WHITE}GSI Market (Custom & Official)")
        print(f"{Fore.YELLOW}[2] {Fore.WHITE}Cihazı Test Et & Raporla (Obsidian Mode)")
        print(f"{Fore.YELLOW}[3] {Fore.WHITE}Manuel URL ile İndir")
        print(f"{Fore.RED}[Q] {Fore.WHITE}Çıkış")
        
        choice = input(f"\n{Fore.CYAN}Seçimin: ").lower()

        if choice == "1":
            # GSI Listesi ve indirme mantığı buraya...
            pass
        elif choice == "2":
            await get_gsi_report() # Yukarıdaki detaylı raporu çağırır
        elif choice == "3":
            url = input(f"\n{Fore.WHITE}GSI Linkini Yapıştır: ")
            os.system(f"wget --show-progress {url}")
        elif choice == "q":
            break

if __name__ == "__main__":
    asyncio.run(start_engine())
