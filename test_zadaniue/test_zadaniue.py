import pytest
from fixture_zadaniue.ContactHelper import ContactHelper
from model_zadaniue.contact import Contact


@pytest.fixture
def app(request):
    fixture = ContactHelper()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_zadaniye3(app):
    app.open_page()
    app.session.login("admin", "secret")

    contact = Contact(
        firstname="firstName",
        middlename="middlename",
        lastname="lastname",
        nickname="nickname",
        address="Pushkina",
        home="88005553535",
        mobile="88005553536",
        work="88005553537",
        email="mail1.ru",
        email2="mail2.ru",
        email3="mail3.ru"
    )

    app.create_contact(contact)

    app.session.logout()


def test_zadaniye3_empty(app):
    app.open_page()
    app.session.login("admin", "secret")

    app.create_contact(Contact())

    app.session.logout()


def test_zadaniye3_minimal(app):
    app.open_page()
    app.session.login("admin", "secret")

    contact = Contact(
        firstname="John",
        lastname="Doe"
    )

    app.create_contact(contact)

    app.session.logout()