import requests
import random
import time

# ── URLs alvo ──────────────────────────────────────────────────────────────────
URLS = [
    "https://exemplo1.com.br",
    "https://exemplo2.com.br",
]

# ── Pool de User-Agents ────────────────────────────────────────────────────────
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
]

# ── Headers base (sem User-Agent — é rotacionado dinamicamente) ────────────────
BASE_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "DNT": "1",
}

# ── Proxies (opcional — deixe lista vazia para desativar) ──────────────────────
PROXIES_LIST = [
    # {"http": "http://user:pass@proxy1:porta", "https": "http://user:pass@proxy1:porta"},
    # {"http": "http://user:pass@proxy2:porta", "https": "http://user:pass@proxy2:porta"},
]

# ── Sessão persistente (mantém cookies entre requisições) ─────────────────────
session = requests.Session()


def get_headers() -> dict:
    """Retorna headers com User-Agent aleatório."""
    return {**BASE_HEADERS, "User-Agent": random.choice(USER_AGENTS)}


def get_proxy() -> dict | None:
    """Retorna um proxy aleatório da lista, ou None se a lista estiver vazia."""
    return random.choice(PROXIES_LIST) if PROXIES_LIST else None


def ping(url: str, retries: int = 3) -> None:
    """
    Faz GET na URL com rotação de UA, jitter de delay, proxy e
    tratamento de rate-limit (429) e erros transitórios.
    """
    for attempt in range(1, retries + 1):
        # Delay com jitter antes de cada tentativa (exceto a 1ª do 1º URL)
        delay = random.uniform(2.0, 6.0)
        print(f"  ↳ aguardando {delay:.1f}s antes de {url} (tentativa {attempt}/{retries})")
        time.sleep(delay)

        session.headers.update(get_headers())
        proxy = get_proxy()

        try:
            resp = session.get(url, proxies=proxy, timeout=10)

            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 60))
                print(f"[429] Rate limit em {url} — aguardando {wait}s...")
                time.sleep(wait)
                continue  # tenta novamente após espera

            print(f"[{resp.status_code}] {url}")
            return  # sucesso — sai do loop de tentativas

        except requests.exceptions.Timeout:
            print(f"[TIMEOUT] {url} — tentativa {attempt}/{retries}")
        except requests.exceptions.ConnectionError as e:
            print(f"[CONEXÃO] {url} — {e} — tentativa {attempt}/{retries}")
        except Exception as e:
            print(f"[ERRO] {url} — {e} — tentativa {attempt}/{retries}")

    print(f"[FALHOU] {url} após {retries} tentativas.")


# ── Execução ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    for url in URLS:
        ping(url)