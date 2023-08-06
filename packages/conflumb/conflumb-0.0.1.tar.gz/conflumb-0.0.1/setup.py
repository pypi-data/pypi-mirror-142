from setuptools import setup, find_packages

setup(
    name='conflumb',         # How you named your package folder (MyLib)
    version='0.0.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Convert markdown document to confluence page',   # Give a short description about your library
    author='esunvoteb',                   # Type in your name
    author_email='esun@voteb.com',      # Type in your E-Mail
    url='https://github.com/ImagineersHub/conflumb',   # Provide either the link to your github or to your website
    # download_url='https://github.com/ImagineersHub/compipe/archive/v_01.tar.gz',    # I explain this later on
    keywords=['confluence', 'markdown'],   # Keywords that define your package best
    packages=find_packages(),
    install_requires=[            # I get to this in a second
        'requests>=2.27.*',
        'markdown>=3.3.6',
        'wrapt>=1.14.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.7',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
