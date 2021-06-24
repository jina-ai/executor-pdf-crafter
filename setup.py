__copyright__ = "Copyright (c) 2020-2021 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import setuptools

setuptools.setup(
    name='jinahub-executor-pdf-crafter',
    version='1',
    author='Jina Dev Team',
    author_email='dev-team@jina.ai',
    description='This executor extracts text and image data from PDF',
    url='https://github.com/jina-ai/executor-pdf-crafter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    py_modules=['jinahub.crafter.pdf_crafter'],
    package_dir={'jinahub.crafter': '.'},
    install_requires=open('requirements.txt').readlines(),
    python_requires='>=3.7',
)
