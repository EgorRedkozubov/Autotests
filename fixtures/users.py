import pytest

@pytest.fixture(scope='module')
def user_with_my_personal_number_xd():
    login = '9379919514'
    password = 'test123'
    return login, password