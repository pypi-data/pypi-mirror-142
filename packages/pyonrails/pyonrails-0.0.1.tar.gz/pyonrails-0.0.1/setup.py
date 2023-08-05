from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pyonrails',
    version='0.0.1',
    description='Python on rails?',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='',
    author='Ryan Johnson',
    author_email='jtronixdev@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='python',
    packages=find_packages(),
    install_requires=['']
)
