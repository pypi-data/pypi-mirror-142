from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='Taller-Programacion-PierrOspina',
    packages=['Taller Programacion'], 
    version='1.0.0',
    description='Trabajo y manejo de matrices con operaciones basicas en phyton con el lenguaje numpy',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Jean Pierr Ospina',
    author_email='',
    url='https://github.com/FadeFruit/RepositorioProgramacionII',
    download_url='https://github.com/FadeFruit/RepositorioProgramacionII',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    install_requires=['numpy'],
    license='MIT',
    include_package_data=True
)