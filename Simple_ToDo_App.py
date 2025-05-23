import json
import os

DOSYA_ADI = "todo.json"

# Dosya yoksa boş liste oluştur
def dosya_kontrol_et():
    if not os.path.exists(DOSYA_ADI):
        with open(DOSYA_ADI, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

# Dosyadan görevleri oku
def gorevleri_yukle():
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        return json.load(f)

# Görevleri kaydet
def gorevleri_kaydet(gorevler):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(gorevler, f, ensure_ascii=False, indent=2)

def gorev_ekle():
    gorev = input("Yeni görevi girin: ")
    liste = gorevleri_yukle()
    liste.append({"gorev": gorev, "tamamlandi": False})
    gorevleri_kaydet(liste)
    print("✅ Görev eklendi!")

def gorev_listele():
    liste = gorevleri_yukle()
    if not liste:
        print("📭 Henüz görev yok.")
    else:
        for i, g in enumerate(liste, 1):
            durum = "✔️" if g["tamamlandi"] else "❌"
            print(f"{i}. {g['gorev']} [{durum}]")

def gorev_tamamla():
    liste = gorevleri_yukle()
    gorev_listele()
    try:
        secim = int(input("Tamamlandı olarak işaretlemek istediğiniz görev numarası: "))
        liste[secim - 1]["tamamlandi"] = True
        gorevleri_kaydet(liste)
        print("✅ Görev tamamlandı!")
    except (IndexError, ValueError):
        print("⚠️ Geçersiz seçim!")

def menu():
    print("\n--- TODO LİSTESİ ---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamla")
    print("4. Çık")

# Ana döngü
dosya_kontrol_et()
while True:
    menu()
    secim = input("Seçiminiz: ")
    if secim == "1":
        gorev_ekle()
    elif secim == "2":
        gorev_listele()
    elif secim == "3":
        gorev_tamamla()
    elif secim == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")
