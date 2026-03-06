#!/bin/bash

# Renkler
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # Renksiz

echo -e "${CYAN}------------------------------------------${NC}"
echo -e "${YELLOW}🔄 GSI Selector Güncelleme Başlatıldı...${NC}"
echo -e "${CYAN}------------------------------------------${NC}"

# Geçici klasörü temizle
rm -rf temp_update

# Repoyu çek
git clone https://github.com/melissaroseria/Check-Gsi.git temp_update

# Dosyaları kopyala (Kendi script'ini ve python dosyasını güncelle)
cp -r temp_update/* .

# Temizlik
rm -rf temp_update

echo -e "${GREEN}✅ Tüm dosyalar başarıyla güncellendi!${NC}"
echo -e "${YELLOW}🚀 Tool yeniden başlatılıyor...${NC}"
sleep 1
python start.py
