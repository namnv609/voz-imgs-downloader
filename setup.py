from setuptools import setup

setup(
    name='voz-images-downloader',
    version='0.1',
    description='vOzForums Images Downloader by Python',
    url='https://github.com/namnv609/voz-imgs-downloader',
    author='NamNV609',
    author_email='namnv609@gmail.com',
    license='MIT',
    packages=['voz-images-downloader'],
    install_requires=[
        'beautifulsoup4',
        'requests',
        'html5lib',
    ],
    zip_safe=False
)
