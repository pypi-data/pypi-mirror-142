from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='email-router',
    version='1.0.0',
    author='Evan Zhang',
    install_requires=['pyyaml', 'mail-parser', 'html2text'],
    include_package_data=True,
    description='A straightforward and efficient inbound email router.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Ninjaclasher/email-router',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
