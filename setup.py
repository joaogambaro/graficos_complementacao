
from setuptools import find_packages, setup

setup(
    name="graficos_complementacao", #1*
    version="1.0.0",
    description="Pacote com funções para complementar \
                 a consttrução de gráficos",
    author= "Joao Paulo Gambaro",
    author_email="joaopaulogambaro@gmail.com",
    python_requires= ">=3.10",
    install_requires=['matplotlib>=3.6.0'],
    packages=find_packages(
        include=['graficos*'],
        exclude=['tests','0_*'],
        ),

)


