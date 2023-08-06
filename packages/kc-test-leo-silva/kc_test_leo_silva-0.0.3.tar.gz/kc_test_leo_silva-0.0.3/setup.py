import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="kc_test_leo_silva",
    version="0.0.3",
    author="leosilva",
    author_email="leonardonevado.silva@gmail.com",
    description="primera practica",
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