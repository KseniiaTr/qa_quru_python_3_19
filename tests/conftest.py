import os

import pytest
from dotenv import load_dotenv

from tests.utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope="session")
def demoshop():
    shop_url = os.getenv("SHOP_URL")
    return BaseSession(shop_url)


@pytest.fixture(scope="session")
def regres():
    regres_url = os.getenv("REGRES_URL")
    return BaseSession(regres_url)






