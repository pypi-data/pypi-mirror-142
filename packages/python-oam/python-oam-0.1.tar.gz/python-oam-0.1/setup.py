from setuptools import setup


setup(
    name='python-oam',
    version='0.1',
    description='OAM toolbox made by the community to the community',
    author=['Rodrigo Faria', 'Tiago Colli'],
    author_email='rodrigo.f.ss@uol.com.br',
    keywords=['oam', 'outlier', 'aspect', 'mining',
              'data', 'explicability', 'outlying'],
    license='MIT',
    install_requires=[
        'pandas==1.3.2',
        'seaborn==0.11.2',
        'tqdm==4.62.0'
    ],
    packages=['oam'],
    zip_safe=False
)
