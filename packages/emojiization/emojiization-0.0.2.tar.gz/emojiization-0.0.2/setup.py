from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="emojiization",
    version="0.0.2",
    author="Dados ao Cubo",
    author_email="tiago@dadosaocubo.com",
    description="O pacote emojiization foi desenvolvido pelo time do dadosaocubo.com para tratamento de textos com Emojis",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dadosaocubo/emojiization-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)