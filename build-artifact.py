# Gera artifact.html a partir do index.html.
#
# O index.html é a versão que roda local (basta abrir no navegador).
# O artifact.html é a mesma coisa sem <!doctype>/<html>/<head>/<body>, que é o
# formato exigido pelo publicador de Artifacts — ele embrulha o arquivo no
# próprio esqueleto. Rode "python build-artifact.py" depois de mexer no jogo.

import io, re, os

base = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(base, "index.html"), encoding="utf-8").read()

# tudo que está dentro do <head>, menos os metas que o esqueleto já fornece
head = re.search(r"<head>(.*?)</head>", src, re.S).group(1)
head = re.sub(r"<meta[^>]*>\s*", "", head)

body = re.search(r"<body>(.*?)</body>", src, re.S).group(1)

out = head.strip() + "\n\n" + body.strip() + "\n"

# no artifact o :root já vem com padding de safe-area: medir em % evita estouro
out = out.replace("#app{width:100vw; height:100vh; height:100dvh;",
                  "#app{width:100%; height:100%;")

# o artifact não deixa a página falar com outros sites, então lá o jogo roda sem ranking
out, n = re.subn(r'const RANKING_URL = "[^"]*";', 'const RANKING_URL = "";', out)
assert n == 1, "não achei o RANKING_URL no index.html"

io.open(os.path.join(base, "artifact.html"), "w", encoding="utf-8", newline="").write(out)
print("artifact.html gerado com", len(out), "caracteres")
