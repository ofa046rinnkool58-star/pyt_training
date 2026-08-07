from kurs.model_kurs.group import Group


def test_change_group_name(app):
    app.session.login("admin", "secret")
    app.group.change_first_group(Group(groupName="NewGroup"))
    app.session.logout()

def test_change_group_header(app):
    app.session.login("admin", "secret")
    app.group.change_first_group(Group(headerName="NewHeader"))
    app.session.logout()