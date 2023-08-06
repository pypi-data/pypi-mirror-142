import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="amoragon-test",
    version="0.1.0",
    author="amoragon",
    author_email="antonio.moragon@gmail.com",
    description="Un ejemplo sencillo",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[
       'build',
       'twine',
       'coloredlogs'
   ],
)






