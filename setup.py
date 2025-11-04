from setuptools import setup, find_packages

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt','r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='my_package',      
    version='0.1.0',
    author='Mahir Tajuar Akash',
    author_email= "tajuar.akash@gmail.com" ,
    description='A sample Python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url = 'your-github-repo-link' ,
    packages=find_packages(), #it search for __init__.py

    classifiers=[
        'Development Status :: 3 - Beta',
        'intended audience :: ML Engineers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.8',
    install_requires=requirements,
    extras_require={
        'dev':[
            'pytest>=6.2.5',
            'pytest-cov>=2.12.1',
            'flake8>=3.9.2',
            'black>=21.9b0',
            'isort>=5.9.3',
            'mypy>=0.942', ]
    }


)
