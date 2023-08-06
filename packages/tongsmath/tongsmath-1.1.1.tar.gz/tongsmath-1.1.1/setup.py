import setuptools


ld = '''
tongsmath
|   setup.py
|   __init__.py
|
+---Primenumber
|       DPF.py-+
|              +DPF(n)->list or bool :Returns the prime factor (list) of n,if b is prime number return False.
|                                     e.g. DPF(48)->[2,2,2,2,3] means 48 = 2*2*2*2*3
|       DPN.py-+
|              +prime_number_list(n)->list or bool :Returns all prime numbers within n,
|              |                                    if there is no content in the prime number list return False.
|              +is_primenumber(n)->bool :Returns whether n is prime.
|
+---Simplify
        sim2ndrt.py-+
                    +sim2ndrt(n)->list or int :Returns the simplified result of sqrt(n).
                                               e.g. sim2ndrt(12)->[2,3] means sqrt(12) = 2 * sqrt(3)
'''
setuptools.setup(
    name='tongsmath',
    version='1.1.1',
    author='Tong',
    author_email='3231690635@qq.com',
    description='Tong\'s exclusive math library contains some junior high school math functions',
    long_description=ld,
    long_description_content_type='text/markdown',
    url='https://github.com/',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
