import requests

URLS = [
    "https://exemplo1.com.br",
    "https://exemplo2.com.br",

]  # adicione quantas URLs quiser

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "DNT": "1"
}

def ping(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        print(f"[OK] {url} respondeu com status {resp.status_code}")
    except Exception as e:
        print(f"[ERRO] Falha ao pingar {url}: {e}")

if __name__ == "__main__":
    for url in URLS:
        ping(url)
