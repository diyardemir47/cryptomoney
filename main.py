import tkinter as tk
import requests

def get_crypto_data():
    # CoinGecko API'sinden veri çekme (Önceki kod ile aynı)
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum',  # İzlemek istediğiniz kripto paraları seçin
        'vs_currencies': 'usd',    # Döviz cinsini seçin (USD, EUR, vb.)
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        return None

def update_prices():
    crypto_data = get_crypto_data()
    if crypto_data:
        bitcoin_price_label.config(text=f"Bitcoin (BTC) Fiyatı: ${crypto_data['bitcoin']['usd']}")
        ethereum_price_label.config(text=f"Ethereum (ETH) Fiyatı: ${crypto_data['ethereum']['usd']}")
    else:
        bitcoin_price_label.config(text="Veriler alınamadı.")
        ethereum_price_label.config(text="Veriler alınamadı.")

# Tkinter penceresini oluşturma
window = tk.Tk()
window.title("Kripto Para Fiyatları")

# Etiketleri (Labels) oluşturma
bitcoin_price_label = tk.Label(window, text="", font=("Arial", 14))
ethereum_price_label = tk.Label(window, text="", font=("Arial", 14))

# Etiketleri pencereye yerleştirme
bitcoin_price_label.pack()
ethereum_price_label.pack()

# Fiyatları güncelleme düğmesi oluşturma
update_button = tk.Button(window, text="Fiyatları Güncelle", command=update_prices)
update_button.pack()

# Başlangıçta fiyatları güncelle
update_prices()

# Tkinter penceresini çalıştırma döngüsü
window.mainloop()
