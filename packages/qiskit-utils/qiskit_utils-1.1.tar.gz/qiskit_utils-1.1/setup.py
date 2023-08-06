from setuptools import setup


setup(
    name='qiskit_utils',
    version='1.1',
    license='MIT',
    author="Marek Grzesiuk",
    packages=['qiskit_utils'],
    url='https://github.com/mgrzesiuk/qiskit-utils',
    keywords='utility-methods qiskit',
    install_requires=[
          'qiskit',
      ],
)