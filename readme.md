# Ping de URLs

Este é um script Python simples para verificar se uma lista de URLs está online, retornando o status HTTP de cada uma.

## Requisitos

* Python 3.x
* Biblioteca `requests`

Você pode instalar a biblioteca `requests` usando:

```bash
pip install requests
```

## Uso

1. Abra o arquivo `worker.py`
2. Adicione ou remova URLs na lista `URLS`.
3. Execute o script:

```bash
python worker.py
```

## Funcionamento

* O script envia uma requisição HTTP GET para cada URL da lista.
* Exibe no console se a URL respondeu com sucesso (`[OK]`) ou se houve algum erro (`[ERRO]`).

## Exemplo de saída

```
[OK] https://exemplo1.com.br respondeu com status 200
[ERRO] Falha ao pingar https://exemplo2.com.br: HTTPSConnectionPool(host='exemplo2.com.br', port=443): Max retries exceeded with url: /
```

## Personalização

Você pode ajustar os cabeçalhos HTTP (`HEADERS`) ou o tempo limite (`timeout`) conforme necessário.
