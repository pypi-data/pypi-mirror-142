# Unilogin API
Log ind på alle sider som bruger unilogin kun ved brug af Python

# Installation
```
pip install unilogin
```

# Brug
En fuld dokumentation er ikke udgivet endnu men her er basis
```python
from unilogin import Unilogin

uniloginClient = Unilogin(brugernavn="brugernavn", adgangskode="adganskode")
loginUrl = uniloginClient.login(href="login link fra side du prøver at logge in fra", referer="link fra side du prøver at logge in fra")

print(loginUrl) #Output: Url som du kan bruge til at logge ind
```

# Pakker som bruger Unilogin API
   - [Skoleintra API (ItsLearnings elev-intra)](https://github.com/jona799t/skoleintra-api)

# To Do
   - Kode oprydning
   - Billede-koder

# Dokumentation
Kommer snart!
