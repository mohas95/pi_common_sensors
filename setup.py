import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi_common_sensors",
    keywords = 'Raspberry Pi, Raspi, Python, GPIO, USB, Mass storage, API, non-blocking',
    version="0.3.0",
    author="Mohamed Debbagh",
    author_email="moha.debbagh95@gmail.com",
    description="""This package provides additional suite of python based rpi abstraction for handling rpi hardware control.
                    The package currently includes an abstraction layer and API engine for the RPi.GPIO package for python, which allows for multi-process and non-blocking control of GPIO pins.
                    The package also includes a module for handling usb mass storage device mounting, data dumping, and unmounting,and other data handling. Finally the Package also includes a module for common sensors.
                    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohas95/pi_common_sensors",
    project_urls={
        "Bug Tracker": "https://github.com/mohas95/pi_common_sensors/issues",
        "Github": "https://github.com/mohas95/pi_common_sensors"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
    ],
    license='GNU GPLv3',
    packages=['pi_common_sensors','pi_common_sensors.gravity'],
    python_requires=">=3.6",
    install_requires=[
          'logzero',
          'RPi.GPIO',
          'pigpio',
          'smbus',
          'spidev',
          'pyserial'
      ]
)
