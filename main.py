import requests
import socket
import socks
import time

url = "https://discord.com/api/v9/channels/909123979082625034/messages"

tokens = {
    "Mjc5MjU3Nzk5NzE4OTkzOTIx.Gzp824.6RSM27cO1ml8PeDGoI-l6_XXXXXXXXXXXXXXXX": {
        "proxy": ("166.1.180.204", 64439, True, 'Rq2NWWhY', 'QLafkCa4'),
        "payload": {"content": "!faucet bbn1rsdfp850s2aqj368f490cXXXXXXXXXXXXXXXXX"}
    },
    "OTc4MzQwMDc5ODgzOTE1MzQ3.Gqp__i.g_t9DRZxlIuKYPNmdeRF7-XXXXXXXXXXXXXXXX": {
        "proxy": ("154.195.136.129", 64837, True, 'Rq2NWWhY', 'QLafkCa4'),
        "payload": {"content": "!faucet bbn1hyre3uekv33vz2fu4kvwuXXXXXXXXXXXXXXXXX"}
    }
}

while True:
    for token in tokens:
        headers = {
            "Authorization": f"{token}"
        }

        socks.set_default_proxy(socks.SOCKS5, *tokens[token]["proxy"])
        socket.socket = socks.socksocket
        print(requests.get('http://ifconfig.me/ip').text)

        try:
            res = requests.post(url, tokens[token]["payload"], headers=headers)
            if res.status_code == 200:
                print("Сообщение успешно отправлено на сервер Discord.")
            else:
                print(f"Произошла ошибка {res.status_code} при отправке сообщения.")
        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при выполнении запроса: {e}")

    time.sleep(60)
