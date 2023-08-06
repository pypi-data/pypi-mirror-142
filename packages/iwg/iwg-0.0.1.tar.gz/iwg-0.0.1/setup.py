import setuptools


if __name__ == "__main__":
    setuptools.setup(
        name="iwg",
        version="0.0.1",
        description="An in-house website generator",
        long_description="",
        author="B.Ozdogan",
        author_email="boraozdogan99@gmail.com",
        url="http://github.com/bozdogan/iwg",
        license="MIT",
        packages=setuptools.find_packages(),
        install_requires=["pytoml"],
        extras_require={
            "dev": [
                "pytest"
            ]
        }
    )
