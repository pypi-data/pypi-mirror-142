from setuptools import setup

setup(
    name='autoDropbox',
    version='0.9.1',
    author='Tiancheng Jiao',
    author_email='jtc1246@outlook.com',
    url='https://github.com/jtc1246/autoDropbox',
    description='A simple API for Dropbox',
    packages=['autoDropbox'],
    install_requires=['myHttp>=1.1.0','mySecrets'],
    python_requires='>=3',
    platforms=["all"],
    license='GPL-2.0 License',
    entry_points={
        'console_scripts': [
            'setAccount=autoDropbox:setAccount',
            'setPassword=autoDropbox:setPassword',
            'ls=autoDropbox:ls',
            'mkdir=autoDropbox:mkdir',
            'rm=autoDropbox:rm',
            'cp=autoDropbox:cp',
            'mv=autoDropbox:mv',
            'rename=autoDropbox:rename',
            'download=autoDropbox:download',
            'downloadFolder=autoDropbox:downloadFolder',
            'upload=autoDropbox:upload',
            'InputError=autoDropbox:InputError'
        ]
    }
)