import os
import subprocess
import asyncio
from colorama import Fore, Style, init

init(autoreset=True)

async def run_cmd(cmd):
    try:
        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return stdout.decode().strip()
    except Exception:
        return None

async def start_tests():
    print(f"\n{Fore.CYAN}=== GSI Your Fork V 2.1 [Gemini Edition] ==={Style.BRIGHT}")
    print(f"{Fore.YELLOW}Cihaz analiz ediliyor, lütfen bekleyin...\n")
    await asyncio.sleep(1.5)

    # Testler
    arch = await run_cmd("uname -m")
    treble = await run_cmd("getprop ro.treble.enabled")
    vndk = await run_cmd("getprop ro.vndk.version")
    
    results = []
    
    # Mimari Testi
    if arch == "aarch64":
        print(f"[{Fore.GREEN}✓{Style.RESET_ALL}] Mimari: {arch} {Fore.GREEN}(Uyumlu)")
        results.append(True)
    else:
        print(f"[{Fore.RED}X{Style.RESET_ALL}] Mimari: {arch} {Fore.RED}(Uyumsuz!)")
        results.append(False)

    # Treble Testi
    if treble == "true":
        print(f"[{Fore.GREEN}✓{Style.RESET_ALL}] Treble Desteği: Aktif {Fore.GREEN}(Uyumlu)")
        results.append(True)
    else:
        print(f"[{Fore.RED}X{Style.RESET_ALL}] Treble Desteği: Pasif {Fore.RED}(Hata!)")
        results.append(False)

    # VNDK Testi
    if vndk:
        print(f"[{Fore.GREEN}✓{Style.RESET_ALL}] VNDK Sürümü: {vndk} {Fore.YELLOW}(Analiz Edildi)")
        results.append(True)
    else:
        print(f"[{Fore.RED}X{Style.RESET_ALL}] VNDK Sürümü: Bulunamadı!")
        results.append(False)

    if all(results):
        print(f"\n{Fore.GREEN}{Style.BRIGHT}RAPOR: CIHAZ GSI KURULUMUNA TAM UYUMLU!")
        print(f"{Fore.MAGENTA}Önerilen Paket: PixelOS Android 15 (arm64-bgN)")
        
        secim = input(f"\n{Fore.CYAN}Wget ile indirme başlatılsın mı? (e/h): ").lower()
        if secim == 'e':
            print(f"\n{Fore.RED}⚠️ UYARI: LÜTFEN WIFI KULLANDIĞINIZDAN EMIN OLUN! (Yaklaşık 2GB)")
            url = "https://github.com/ponces/treble_build_pe/releases/download/v2025.02.15/PixelOS_arm64-ab-15.0-20250215-UNOFFICIAL.img.xz"
            os.system(f"wget --show-progress {url}")
            print(f"\n{Fore.GREEN}İndirme tamamlandı! Dosyayı ZArchiver ile çıkartmayı unutma kanki. ❣️")
    else:
        print(f"\n{Fore.RED}HATA: Cihazınızda bazı uyumsuzluklar tespit edildi!")

if __name__ == "__main__":
    asyncio.run(start_tests())
