def test_delete_first_groups(app):
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()