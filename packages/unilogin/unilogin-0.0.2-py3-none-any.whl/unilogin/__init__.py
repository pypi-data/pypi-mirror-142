import httpx
import urllib.parse
from bs4 import BeautifulSoup

class Unilogin:
    def __init__(self, brugernavn, adgangskode):
        self.session = httpx.Client()

        self.brugernavn = brugernavn
        self.adgangskode = adgangskode

    def login(self, href, referer="https://www.google.com/"):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'host': 'sso.emu.dk',
            'referer': referer,
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = BeautifulSoup(resp.text, 'html.parser').find('a').get('href')

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'host': 'atlas.uni-login.dk',
            'referer': referer,
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = BeautifulSoup(resp.text, 'html.parser').find('a').get('href')
        simpleSAMLSessionID = resp.cookies["SimpleSAMLSessionID"]

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'host': 'broker.unilogin.dk',
            'referer': referer,
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = BeautifulSoup(resp.text, 'html.parser').find('form').get('action')
        #print(href)

        payload = f"username={self.brugernavn}"
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'content-length': str(len(payload)),
            'content-type': 'application/x-www-form-urlencoded',
            #'cookie': 'AUTH_SESSION_ID=0b7603aa-a646-4ed9-9601-0f527dee2e33.195.231.174.54; AUTH_SESSION_ID_LEGACY=0b7603aa-a646-4ed9-9601-0f527dee2e33.195.231.174.54; KC_RESTART=eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJkYWVhMDQxYS1kNTVmLTQyMTEtOTJjMy02ZmZhYmYxYWZkNGUifQ.eyJjaWQiOiJodHRwczovL2F0bGFzLnVuaS1sb2dpbi5kay9zaW1wbGVzYW1sL21vZHVsZS5waHAvc2FtbC9zcC9tZXRhZGF0YS5waHAvYXMtc3NvLXByb3h5IiwicHR5Ijoic2FtbC1zdGlsIiwicnVyaSI6Imh0dHBzOi8vYXRsYXMudW5pLWxvZ2luLmRrL3NpbXBsZXNhbWwvbW9kdWxlLnBocC9zYW1sL3NwL3NhbWwyLWFjcy5waHAvYXMtc3NvLXByb3h5IiwiYWN0IjoiQVVUSEVOVElDQVRFIiwibm90ZXMiOnsibGV2ZWxfb2ZfYXNzdXJhbmNlIjoiIiwiUmVsYXlTdGF0ZSI6Imh0dHBzOi8vYXRsYXMudW5pLWxvZ2luLmRrL3VuaWxvZ2luL2xvZ2luLmNnaT9pZD1za2lucHJvZCZhdXRoPTU4NTI2MWM4ZTNiYmM3ZmQxZGFjMGU4YzgxNDc5NTFkJnBhdGg9YUhSMGNITTZMeTlpWVdkcmIzTjBMbTB1YzJ0dmJHVnBiblJ5WVM1a2F5OUJZMk52ZFc1MEwxVnVhVXh2WjJsdVAzSnZiR1U5VUdGeVpXNTBKbkJoY25SdVpYSlRjRDExY200bE0wRnBkSE5zWldGeWJtbHVaeVV6UVc1emFTVXpRWE5oYld3bE0wRXlMakFsTTBGaVlXZHJiM04wTG0wdWMydHZiR1ZwYm5SeVlTNWthdz09IiwiU0FNTF9SRVFVRVNUX0lEIjoiXzhjZTFlNzM1MDBjYTU0MTNkMmY0YzIzN2U4Mzk1MDg2NjEyMWY0ZDU2MiIsInNhbWxfYmluZGluZyI6InBvc3QiLCJpc1Bhc3NpdmUiOiJmYWxzZSIsImZvcmNlX2F1dGhlbnRpY2F0aW9uIjoiZmFsc2UiLCJuc2lzX2xvZ2luX3R5cGUiOiJmYWxzZSJ9fQ.Isu5GuYX06ltCOQor30UI4ETh2L-9H7oWddyZze80RU',
            'host': 'broker.unilogin.dk',
            'origin': 'null',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.post(href, headers=headers, data=payload, allow_redirects=False)
        href = resp.headers['location']
        #print(href)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'host': 'broker.unilogin.dk',
            'referer': 'https://infomedia.dk/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = resp.headers['location']
        #print(href)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'host': 'idp.unilogin.dk',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = BeautifulSoup(resp.text, 'html.parser').find('form').get('action')
        #print(href)

        payload = f"password={self.adgangskode}&username="
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'content-length': str(len(payload)),
            'content-type': 'application/x-www-form-urlencoded',
            #cookie
            'host': 'idp.unilogin.dk',
            'origin': 'null',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.post(href, headers=headers, data=payload, allow_redirects=False)
        html = BeautifulSoup(resp.text, 'html.parser')
        href = html.find('form').get('action')
        samlResponse = [html.find("input", {"name": "SAMLResponse"}).get("name"), html.find("input", {"name": "SAMLResponse"}).get("value")]
        replayState = [html.find("input", {"name": "RelayState"}).get("name"), html.find("input", {"name": "RelayState"}).get("value")]
        payload = f"{samlResponse[0]}={urllib.parse.quote_plus(samlResponse[1])}&{replayState[0]}={urllib.parse.quote_plus(replayState[1])}"
        #print(href)
        #print(payload)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'content-length': str(len(payload)),
            'content-type': 'application/x-www-form-urlencoded',
            #'cookie': f'Måske cookie her',
            'host': 'broker.unilogin.dk',
            'origin': 'null',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.post(href, headers=headers, data=payload, allow_redirects=False)
        #print(resp.headers)
        #print(resp.status_code)
        #print(resp.text)
        href = resp.headers['location']
        #print(href)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'host': 'broker.unilogin.dk',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = BeautifulSoup(resp.text, 'html.parser').find('form').get('action')
        #print(href)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'host': 'broker.unilogin.dk',
            'origin': 'null',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.post(href, headers=headers, allow_redirects=False)
        href = resp.headers['location']
        #print(href)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'connection': 'keep-alive',
            'host': 'broker.unilogin.dk',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = BeautifulSoup(resp.text, 'html.parser').find("form", {"name": "saml-post-binding"}).get("action")

        html = BeautifulSoup(resp.text, 'html.parser')
        samlResponse = [html.find("input", {"name": "SAMLResponse"}).get("name"), html.find("input", {"name": "SAMLResponse"}).get("value")]
        replayState = [html.find("input", {"name": "RelayState"}).get("name"), html.find("input", {"name": "RelayState"}).get("value")]
        payload = f"{samlResponse[0]}={urllib.parse.quote_plus(samlResponse[1])}&{replayState[0]}={urllib.parse.quote_plus(replayState[1])}"

        #print(href)
        #print(resp.status_code)

        #print(payload)

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "connection": "keep-alive",
            "content-length": str(len(payload)),
            "content-type": "application/x-www-form-urlencoded",
            "cookie": f"SimpleSAMLSessionID={simpleSAMLSessionID}",
            "host": "atlas.uni-login.dk",
            "origin": "null",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "cross-site",
            "sec-gpc": "1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        }
        resp = self.session.post(href, headers=headers, data=payload, allow_redirects=False)

        href = resp.headers['location']
        #print(href)
        #print(resp.status_code)
        simpleSAMLAuthToken = resp.cookies["SimpleSAMLAuthToken"]
        #print(simpleSAMLAuthToken)

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "connection": "keep-alive",
            "cookie": f"SimpleSAMLSessionID={simpleSAMLSessionID}; SimpleSAMLAuthToken={simpleSAMLAuthToken}",
            "host": "atlas.uni-login.dk",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "cross-site",
            "sec-gpc": "1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        }
        resp = self.session.get(href, headers=headers, allow_redirects=False)
        href = resp.headers['location']
        return href