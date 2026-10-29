# Vai dá PT

Jogo de travessia no estilo do [cadeflavio.run](https://cadeflavio.run/), só que
mais simples: a personagem atravessa a academia desviando de pote de whey, saco
de creatina e lata de pré-treino. Junte 3 estrelas e a Dilma entra na frente
segurando os potes.

## Arquivos

- `index.html` — o jogo inteiro (HTML, CSS, canvas e sprites num arquivo só).
  Sem build, sem dependência: é só abrir no navegador.
- `artifact.html` — a mesma coisa sem as tags de documento, no formato que o
  publicador de Artifacts exige. **Não edite este arquivo**, ele é gerado.
- `build-artifact.py` — gera o `artifact.html` a partir do `index.html`.
- `doge.png` — o meme do swole doge, que aparece emoldurado nas janelas da
  academia. Ele vai embutido no HTML como data URI, então o jogo continua
  sendo um arquivo só; esse png fica aqui como original.

## Rodar

Abrir o `index.html` no navegador resolve. Para servir por HTTP:

```bash
python -m http.server 8123
```

## Publicar a versão nova

```bash
python build-artifact.py
```

Depois é só republicar o `artifact.html` no mesmo link do Artifact.

## Como funciona

- **Controles:** no celular, toque e arraste para mover o personagem
  livremente entre as raias; arrastar para os lados acelera ou segura.
  Toque curto tambem troca de raia. No teclado: ↑ ↓ (ou W/S) trocam de
  raia, → corre, ← segura, P pausa, M silencia. O personagem sempre
  corre sozinho para frente.
- **Inimigos:** creatina (segue o chão), whey (vem mais devagar, então você
  alcança) e pré-treino (mais rápido e muda de raia sozinho, a partir de 150 m
  no normal e difícil).
- **Itens:** frango vale 50 pontos, banana devolve uma vida.
- **Spawn:** a cada onda sorteia uma raia que fica livre, então sempre existe
  saída. A dificuldade controla vidas, velocidade, densidade e a distância da
  saída.
- **Tela:** a altura lógica é fixa (540) e a largura acompanha a proporção da
  tela; a velocidade é multiplicada pela mesma escala, então o jogo corre igual
  no monitor e no celular deitado. Em pé, aparece o aviso para girar.
- **Estrelas:** cada 3 estrelas chamam a Dilma por 9 segundos; enquanto ela
  estiver na frente, todo pote que encostar é destruído e ainda vale 15 pontos.
- Atalhos de teste na URL: `?meta=300` encurta a travessia e `?escudo=1` já
  começa com a Dilma em campo.

## Ranking da galera

Cada um digita o nome na tela inicial (o celular lembra). No fim da partida o
placar vai pro ranking e a tela final mostra o top 3 e a sua posição; o botão
RANKING abre o top 10 de cada dificuldade, com um lugar por pessoa.

Os placares ficam numa planilha do Google, a mesma do Jamaica Versions, mas
numa aba só deste jogo (`placares vai da pt`). O código da planilha está em
`ranking/Code.gs`, no repositório do Jamaica Versions. Cada jogo manda a sua
chave (`RANKING_CHAVE`) em todo pedido, e a planilha só mostra e grava o ranking
do jogo dono da chave: daqui não dá pra ver o ranking do Jamaica, nem de lá o
deste. O `artifact.html` sai sem ranking, porque o Artifact não deixa a página
falar com outros sites.

## Publicar uma atualização

O jogo está no ar em
<https://vaidar-pt-eng.github.io/vaidar-pt/> pelo GitHub Pages,
servido direto do `index.html` na raiz do branch `main`. Para atualizar:

```bash
git add -A && git commit -m "o que mudou" && git push
```

O Pages reconstrói sozinho em cerca de um minuto.
