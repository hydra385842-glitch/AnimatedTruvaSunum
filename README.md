# Truva Savaşı · İlyada Sunumu

Streamlit + PIXI.js ile sinematik Truva Savaşı sunumu. 220 saniyelik epik kuşatma animasyonu, 45 saniyelik Akhilleus vs Hektor düellosu, full-skeletal animasyon sistemi içerir.

## Özellikler

- 11 sahneli kuşatma animasyonu (220 saniye)
- 45 saniye full-skeletal düello (Akhilleus vs Hektor)
- Yumruk yumruğa, mızrak mızrağa savaş sahneleri
- YouTube tarzı scrub-bar, sahne atlama, fullscreen
- PIXI.js v7 ile WebGL render
- Sabit dağ renkleri (yangında değişmez)
- Trauma-based kamera shake + zoom

## Yerel Çalıştırma

```bash
pip install -r requirements.txt
streamlit run app.py
```

Tarayıcıda `http://localhost:8501` açılacak.

## Streamlit Cloud Deploy

1. GitHub'a push et:
```bash
git init
git add .
git commit -m "Truva sunumu"
git remote add origin https://github.com/KULLANICI/REPO.git
git push -u origin main
```

2. [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Repo, branch, main file: `app.py` seç
4. Deploy → 1-2 dakikada hazır

## Dosya Yapısı

```
truva_streamlit/
├── app.py              # Streamlit uygulaması
├── truva.html          # PIXI.js animasyonu + React sunumu
├── requirements.txt    # Bağımlılıklar
└── README.md           # Bu dosya
```

## Kontroller

- `▶ / ⏸` Oynat/Duraklat
- `↻` Baştan başlat
- **Scrub-bar** (tıkla/sürükle) İstediğin saniyeye atla
- **I–XI** Sahne butonları
- `⛶` Tam ekran

## Sahne Akışı (220 sn)

| # | Sahne | Süre |
|---|-------|------|
| I | Şafak | 0-12s |
| II | Akhalar Yürüyor | 12-30s |
| III | Ok Yağmuru | 30-52s |
| IV | Süvari Hücumu | 52-75s |
| V | Düello Girişi | 75-90s |
| VI | Düello Meydan | 90-120s |
| VII | Düello Final | 120-135s |
| VIII | Koçbaşı | 135-155s |
| IX | Kapı Yıkıldı | 155-170s |
| X | Şehir Yanıyor | 170-195s |
| XI | Truva Düştü | 195-220s |

## Düello Sahnesi (45 sn)

1. Giriş + daire çizme
2. Akhilleus mızrak fırlatma → Hektor kalkanı çatlar
3. Hektor mızrak fırlatma → Akhilleus kalkanı parçalanır
4. Yakın savaş
5. **Mızrak mızrağa çarpışma** (alternatif thrust/parry)
6. **Yumruk yumruğa** (4 farklı punch animasyonu)
7. Son darbe windup → ölümcül darbe
8. Hektor düşüyor → Akhilleus zafer pozu

## Stack

- **Frontend:** React 18 + Tailwind (CDN) + PIXI.js 7.3
- **Backend:** Streamlit 1.32+
- **Render:** WebGL (canvas) inline iframe
