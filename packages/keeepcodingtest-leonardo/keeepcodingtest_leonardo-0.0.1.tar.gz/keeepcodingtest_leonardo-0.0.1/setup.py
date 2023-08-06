import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="keeepcodingtest_leonardo",
    version="0.0.1",
    author="keepcoder",
    author_email="kcpypitest@gmail.com",
    description="Ejemplo de artefacto",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[
       'build',
       'twine'
   ],
)