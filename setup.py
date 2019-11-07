from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pyspark"]

setup(
    name="mock_tt",
    version=open("version.txt").read(),
    author="Raul Martins/Leandro Soares",
    author_email="raul.wanderlei-ess@parceiros-kroton.com.br",
    description="Nova estrutura da trusted-transformation",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rauljm/mock_tt/",
    packages=["ktrusted.source",
              "ktrusted.target",
              "ktrusted.transformation",
              "ktrusted.surrogate",
              "config"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
