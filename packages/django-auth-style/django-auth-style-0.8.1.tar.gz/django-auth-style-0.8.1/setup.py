from pathlib import Path

from setuptools import find_packages, setup

readme_file = Path(__file__).parent / 'README.md'
with readme_file.open() as f:
    long_description = f.read()

setup(
    name='django-auth-style',
    description='Django template styling for django-allauth and django-oauth-toolkit.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    url='https://github.com/girder/django-auth-style',
    project_urls={
        'Bug Reports': 'https://github.com/girder/django-auth-style/issues',
        'Source': 'https://github.com/girder/django-auth-style',
    },
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    keywords='django style styling allauth django-allauth django-oauth-toolkit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python',
    ],
    packages=find_packages(include=['auth_style']),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=[
        'django',
    ],
    extras_require={
        'allauth': ['django-allauth'],
        'oauth-toolkit': ['django-oauth-toolkit'],
    },
)
