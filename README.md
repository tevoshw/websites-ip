# 🔍 Site IP & Porta Scanner

Este é um script simples em Python que permite:

- Obter o **IP de um site/domínio** usando DNS.
- Exibir mensagens claras em caso de erro (DNS inválido, etc).

---

## 📂 Arquivos

- `get_ip.py` → script principal que realiza a verificação

---

## 🧪 Exemplo de uso (sem erro)

```bash
$ python scanner.py

Digite o nome do site: google.com
IP de google.com: 142.250.78.14
```

## 🧪 Exemplo de uso (com erro)

```bash
$ python scanner.py

Digite o nome do site: uoogle.com
Um erro aconteceu devido ao URL do site "uoogle.com" ser inválido. Deseja tentar novamente? [Y/n]: y

Digite o nome do site: google.com
Ip de google: 142.250.78.14



