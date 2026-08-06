from kurs.model_kurs.contact import Contact


def test_contacts(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact(firstname="firstName",
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
    app.session.logout()


def test_contacts_empty(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact(firstname="",
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
    app.session.logout()