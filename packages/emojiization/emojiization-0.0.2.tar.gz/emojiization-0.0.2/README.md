# Emojiization

O pacote emojiization foi desenvolvido pelo time do [Dados ao Cubo](https://www.dadosaocubo.com/) para tratamento de textos com Emojis:
- Transformação de emojis em textos;
- Substituição de emojis por outro texto específico;
- Contagem de emojis presentes em texts.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install emojiization

```bash
pip install emojiization
```

## Usage

```python
from emojiization.functions.transform import emoji_transform, emoji_replace

emoji_transform(text)

emoji_replace(text, new_text)
```

```python
from emojiization.functions.metrics import emoji_count

emoji_count(text)
```
## Author
Dados ao Cubo

## License
[MIT](https://choosealicense.com/licenses/mit/)