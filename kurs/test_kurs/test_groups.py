import pytest
from kurs.fixture_kurs.application import Application
from kurs.model_kurs.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_groups(app):
    app.session.login("admin", "secret")

    app.group.open_groups()
    app.group.new_group_creation()
    app.group.fill_forms(Group("zadaniye2", "header2", "footer2"))
    app.group.submitting()
    app.group.return_to_group_page()

    app.session.logout()


def test_groups_empty(app):
    app.session.login("admin", "secret")

    app.group.create()
    app.group.fill_forms(Group("", "", ""))
    app.group.submitting()
    app.group.return_to_group_page()

    app.session.logout()