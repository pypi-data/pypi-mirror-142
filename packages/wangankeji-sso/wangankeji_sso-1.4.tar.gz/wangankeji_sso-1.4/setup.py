import setuptools

version = '1.4'

setuptools.setup(
    name='wangankeji_sso',
    version=version,
    install_requires=[
        'requests>=2.21.0',
        'pycryptodome>=3.10.1',
    ]
)
