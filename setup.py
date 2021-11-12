from distutils.core import setup

setup(
    name='NoteBot',
    author='Roberto Arista',
    version='0.1',
    packages=['noteBot'],
    package_data={"noteBot": ["py.typed"]},
    include_package_data=True,
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
)
