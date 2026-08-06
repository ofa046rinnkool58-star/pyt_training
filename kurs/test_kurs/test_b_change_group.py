from kurs.model_kurs.group import Group


def test_change_group(app):
    app.session.login("admin", "secret")
    app.group.change_group(Group("pomenyalos", "pomenyalos2", "pomenyalos3"))
    app.session.logout()