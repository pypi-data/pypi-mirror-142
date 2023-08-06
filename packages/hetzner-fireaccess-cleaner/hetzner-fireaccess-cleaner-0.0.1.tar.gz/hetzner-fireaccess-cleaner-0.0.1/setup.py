import setuptools

with open('README.md', 'r') as r:
    long_description = r.read()

setuptools.setup(
    name='hetzner-fireaccess-cleaner',
    version='0.0.1',
    author='DigitalArc Studio',
    description='A simple CLI for cleaning automated access to hetzner firewalls',
    keywords='simple hetzner tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/digitalarc/hetzner-fireaccess-cleaner',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hetzner-fireaccess-cleaner=hetzner_fireaccess_cleaner.hetzner_fireaccess_cleaner:cli',
        ],
    },
    install_requires=[
        'toml>=0.10.2',
        'click>=8.0.0',
        'hcloud>=1.16.0'
    ]
)
