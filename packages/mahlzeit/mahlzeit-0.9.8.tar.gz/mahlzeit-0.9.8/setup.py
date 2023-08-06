from setuptools import setup, find_packages


setup(
    name='mahlzeit',
    version='0.9.8',
    url='https://gitlab.com/meschenbacher/mahlzeit',
    description='Mahlzeit Plaintextaccounting für Essen und Anderes',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='Maximilian Eschenbacher',
    author_email="qbzioxli@m.t.kajt.de",
    packages=find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=3',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
