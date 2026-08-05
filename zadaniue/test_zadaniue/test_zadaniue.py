import pytest
from zadaniue.fixture_zadaniue.applicationContact import ApplicationContact
from zadaniue.model_zadaniue.contact import Contact


@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_zadaniye3(app):
    app.session.login("admin", "secret")
    app.contact.open_page()
    app.contact.new_contact()
    app.contact.fill_contact(Contact(firstname="firstName",
        middlename="middlename",
        lastname="lastname",
        nickname="nickname",
        address="Pushkina",
        home="88005553535",
        mobile="88005553536",
        work="88005553537",
        email="mail1.ru",
        email2="mail2.ru",
        email3="mail3.ru"))
    app.contact.submit_contact()
    app.contact.return_to_home_page()
    app.session.logout()


def test_zadaniye3_empty(app):
    app.session.login("admin", "secret")
    app.contact.open_page()
    app.contact.new_contact()
    app.contact.fill_contact(Contact(firstname="",
        middlename="",
        lastname="",
        nickname="",
        address="",
        home="",
        mobile="",
        work="",
        email="",
        email2="",
        email3=""))
    app.contact.submit_contact()
    app.contact.return_to_home_page()
    app.session.logout()