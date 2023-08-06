from os import path
import setuptools

try:
    from bin import get_version

    def local_version():
        return get_version.get_version()
except Exception:
    def local_version():
        return "undefined"


def long_description():
    this_directory = path.abspath(path.dirname(__file__))
    try:
        with open(path.join(this_directory, 'README.md'),
                  encoding='utf-8') as f:
            return f.read()
    except TypeError:
        with open(path.join(this_directory, 'README.md')) as f:
            return f.read()


setuptools.setup(
    name="RabbitMQ Test Tool",
    version=local_version(),
    description="A simple test script to test a RabbitMQ cluster",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="Nicolas Bock",
    packages=['rabbitmqtesttool'],
    entry_points={
        "console_scripts": [
            "rabbitmq-test-tool = rabbitmqtesttool.main:main",
        ],
    }
)
