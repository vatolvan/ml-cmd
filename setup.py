from setuptools import setup

setup(
    name='ml-cmd',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'ml-cmd=mlcmd:run'
        ]
    }
)