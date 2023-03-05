import os

import allure
from dotenv import load_dotenv
from selene import have
from faker import Faker

from selene.support.shared import browser


load_dotenv()

SHOP_URL = os.getenv("SHOP_URL")
#LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")

fake = Faker()
email = fake.email()

@allure.step("Open browser")
def test_register():
    browser.open(SHOP_URL)

    with allure.step("Fill information"):
        browser.element(".ico-register").click()
        browser.element("[id=gender-male]").click()
        browser.element("[id=FirstName]").type("Ivan")
        browser.element("[id=LastName").type("Egorov")
        browser.element("[id=Email]").type(email)
        browser.element("[id=Password]").type(PASSWORD)
        browser.element("[id=ConfirmPassword]").type(PASSWORD)

    with allure.step("Confirm"):
        browser.element("[id=register-button]").click()

        browser.element(".account").should(have.text(email))


def test_sigh_in(demoshop):
    response = demoshop.post("/login", json={"Email": "ivan_egor@mail.ru", "Password": "123456"}, allow_redirects=False)
    authorization_cookie = response.cookies.get("Nop.customer")
    print(authorization_cookie)
    print(response.status_code)


def test_sigh_in_with_wrong_password(demoshop):
    response = demoshop.post("/login", json={"Email": "ivan_egorov@mail.ru", "Password": "223343"},
                             allow_redirects=False)
    response.cookies.get("Nop.customer")
    print(response.status_code)


def test_register_with_api(demoshop):
    response = demoshop.post("/login", json={"Gender": "M", "FirstName": "Anton", "LastName": "Ivanov",
                                             "Email": "anton_ivanov@mail.ru", "Password": "111111",
                                             "ConfirmPassword": "111111", "register-button": "Register"},
                             allow_redirects=False)
    response_header = response.cookies.get("NOPCOMMERCE.AUTH")
    print(response_header)
    print(response.status_code)
    assert response.status_code == 302


def test_register_with_different_passwords(demoshop):
    response = demoshop.post("/login", json={"Gender": "M", "FirstName": "Igor", "LastName": "Ivanov",
                                             "Email": "igor_ivanov@mail.ru", "Password": "111222",
                                             "ConfirmPassword": "222222", "register-button": "Register"},
                             allow_redirects=False)
    response_header = response.cookies.get("NOPCOMMERCE.AUTH")
    print(response_header)
    print(response.status_code)


def test_add_item_to_cart(demoshop):
    response = demoshop.post("/cart", json={"product_attribute_75_5_31": "96",
                                            "product_attribute_75_6_32": "100",
                                            "product_attribute_75_3_33": "102",
                                            "addtocart_75.EnteredQuantity": "1"}, allow_redirects=False)
    response_header = response.cookies.get("Nop.customer")
    print(response_header)
    print(response.status_code)


def test_remove_from_cart(demoshop):
    response = demoshop.post("/addproducttocart/details/75/1", json={"removefromcart": "3058714",
                                                                     "itemquantity3058714": "0",
                                                                     "updatecart": "Update shopping cart",
                                                                     "discountcouponcode": "",
                                                                     "giftcardcouponcode": "",
                                                                     "CountryId": "0",
                                                                     "StateProvinceId": "0",
                                                                     "ZipPostalCode": ""}, allow_redirects=False)
    response_header = response.cookies.get("Nop.customer")
    print(response_header)
    print(response.status_code)
