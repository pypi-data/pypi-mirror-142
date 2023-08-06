from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='Metodo GaussJordan',
    packages=['Gauss'], 
    version='0.1',
    description='Con este paquete puedes resolver matrices nxn por GaussJordan',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Miguel Acevedo',
    author_email='',
    # use the URL to the github repo
    url='https://github.com/IsoT0P0S/Metodo-GaussJordan.git',
    download_url='https://github.com/IsoT0P0S/Metodo-GaussJordan.git',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    install_requires=['numpy'],
    license='MIT',
    include_package_data=True
)