from setuptools import setup

setup(
    name="detox-tracker",
    version="1.0",
    py_modules=["tracker"],
    install_requires=[], #Add 'rich' here later if you use colors
    entry_points={
        'console_scripts': [
            'detox=tracker:update_tracker',
        ],
    },
)
