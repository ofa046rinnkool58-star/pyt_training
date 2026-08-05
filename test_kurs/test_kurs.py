import pytest
from fixture_kurs.application import Application
from model_kurs.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_zadaniye2(app):
    app.session.login("admin", "secret")

    app.group.create()
    app.fill_forms(Group("zadaniye2", "header2", "footer2"))
    app.submitting()
    app.return_to_group_page()

    app.session.logout()


def test_zadaniye2_empty(app):
    app.session.login("admin", "secret")

    app.group.create()
    app.fill_forms(Group("", "", ""))
    app.submitting()
    app.return_to_group_page()

    app.session.logout()