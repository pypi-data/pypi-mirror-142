from setuptools import setup, find_packages

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name='stout',
    version='0.0.8',
    author='suckerpunched',
    author_email='',
    description='',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/suckerpunched/stout',
    project_urls = {
        "Bug Tracker": "https://github.com/suckerpunched/stout/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'click',
        'docker',
    ],

    package_data={'': ['dockerfile']},

    entry_points = {
        'console_scripts': ['stout=stout.command_line:main'],
    }
)

