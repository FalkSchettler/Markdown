from setuptools import setup, find_packages

setup(
    name="Markdown",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Deine Abhängigkeiten
    ],
    entry_points={
        'console_scripts': [
            'markdown=markdown_gen.markdown:main_function',
        ],
    },
)
