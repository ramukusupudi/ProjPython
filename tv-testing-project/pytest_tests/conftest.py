import pytest

# Shared pytest fixtures can be added here

@pytest.fixture(scope="class")
def set():
    print("")
    yield
    print("")


def dataLoad():
    print("user profiles data is being created")
    return ["Ramu","kusupudi","learning Fixtures"]

