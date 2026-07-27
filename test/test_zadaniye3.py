import pytest
from fixture.ContactHelper import ContactHelper
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = ContactHelper()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_zadaniye3(app):
    # Логинимся
    app.open_page().login("admin", "secret")

    # Создаем контакт
    contact = Contact(
        firstName="firstName",
        middleName="middlename",
        lastName="lastname",
        nickName="nickname",
        Adress="Pushkina",
        Phone1="88005553535",
        Phone2="88005553536",
        Phone3="88005553537",
        Mail1="mail1.ru",
        Mail2="mail2.ru",
        Mail3="mail3.ru"
    )

    app.contact.create_contact(contact)

    # Выходим из системы
    app.cont_session.logout()


def test_zadaniye3_empty(app):
    # Логинимся
    app.session.login("admin", "secret")

    # Создаем контакт с пустыми полями
    app.contact.create_contact(Contact())

    # Выходим из системы
    app.session.logout()


def test_zadaniye3_minimal(app):
    # Логинимся
    app.session.login("admin", "secret")

    # Создаем контакт только с именем и фамилией
    contact = Contact(
        firstName="John",
        lastName="Doe"
    )

    app.contact.create_contact(contact)

    # Выходим из системы
    app.session.logout()