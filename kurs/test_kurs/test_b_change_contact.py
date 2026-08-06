from kurs.model_kurs.contact import Contact


def test_change_group(app):
    app.session.login("admin", "secret")
    app.contact.change_contact(Contact(firstname="izmeneno",
        middlename="izmeneno",
        lastname="izmeneno",
        nickname="izmeneno",
        address="izmeneno",
        home="88005553535",
        mobile="88005553536",
        work="88005553537",
        email="izmeneno.ru",
        email2="izmeneno.ru",
        email3="izmeneno.ru"))
    app.session.logout()