import os
import subprocess
import asyncio

# ... (setup_env ve diğer kısımlar aynı kalıyor) ...

async def check_update():
    print(f"{Fore.YELLOW}🔄 Gemini Sunucuları Kontrol Ediliyor...")
    await asyncio.sleep(1.5)
    
    print(f"\n{Fore.CYAN}✨ Google Gemini'den Mesaj:")
    print(f"{Fore.WHITE}'Kanki, update.sh üzerinden tam kapsamlı güncelleme hazır!'")
    
    confirm = input(f"\n{Fore.GREEN}Güncelleme (update.sh) başlatılsın mı? (e/h): ").lower()
    if confirm == 'e':
        # update.sh dosyasını Python içinden tetikliyoruz
        if os.path.exists("update.sh"):
            print(f"{Fore.MAGENTA}🚀 update.sh çalıştırılıyor...")
            os.system("bash update.sh")
        else:
            print(f"{Fore.RED}❌ update.sh bulunamadı! Repo klonlanıyor...")
            os.system("git clone https://github.com/melissaroseria/Check-Gsi.git temp && cp -r temp/* . && rm -rf temp")
            if os.path.exists("update.sh"):
                os.system("bash update.sh")
        
        return True
    return False

# ... (start_engine ve diğer kısımlar devam eder) ...
