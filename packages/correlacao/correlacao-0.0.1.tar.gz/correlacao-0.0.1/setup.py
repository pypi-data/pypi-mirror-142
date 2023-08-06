from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="correlacao",
    version="0.0.1",
    author="Nicodemos Freitas",
    author_email="nicodemosfreitas@gmail.com",
    description="Pacote para correlacionar Variáveis e Alvo - Análise de Dados",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nicodemos/correlacao_variaveis_alvo",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)