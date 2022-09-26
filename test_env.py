import os


def test_env_hello():
    assert os.environ["HELLO"]


def test_env_home():
    assert os.environ["HOME"]
