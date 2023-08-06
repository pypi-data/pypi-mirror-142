from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Pygame-based game engine'
LONG_DESCRIPTION = 'Pygame-based game engine in python'

setup(
        name="limengine",
        version=VERSION,
        author="Enrike Churin",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=['pygame'],
        keywords=['pygame', 'game', 'game engine', 'graphics'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Environment :: MacOS X",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: MacOS",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Microsoft :: Windows :: Windows 10",
            "Operating System :: OS Independent",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Unix",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Games/Entertainment",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries :: pygame",
        ]
)
