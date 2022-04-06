from distutils.core import setup

setup(
    name="TypedBot",
    author="Roberto Arista",
    author_email="hello@robertoarista.it",
    version="0.2",
    packages=["typedBot"],
    package_data={"typedBot": ["py.typed"]},
    include_package_data=True,
    license=open("LICENSE").read(),
    long_description=open("README.md").read(),
    platforms=["macOS"],
    python_requires=">=3.9",
)
