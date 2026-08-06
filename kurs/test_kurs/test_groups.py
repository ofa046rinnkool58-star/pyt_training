from kurs.model_kurs.group import Group



def test_groups(app):
    app.session.login("admin", "secret")
    app.group.create(Group("zadaniye2", "header2", "footer2"))
    app.session.logout()


def test_groups_empty(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()