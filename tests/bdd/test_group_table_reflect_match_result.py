"""
Verify that group table standings update with live score
"""

import json
import logging

import pytest
from pytest_bdd import given, scenario, then, when
from pytest_bdd.parsers import parse

from league_table.flask_app import app

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def client():
    return app.test_client()


@scenario("group_table.feature", "Group table from match results")
def test_league_standings_update():
    pass


@given("an example league table application")
def example_league_application(client):
    pass

@when(parse("fresh {match_results} come through"))
def fresh_match_results(match_results, client):
    client.post("/league_table", data=match_results)


@then(parse("group table should reflect the {new_standings}"))
def league_table(new_standings, client):
    group_table = client.get("/league_table")
    group_table = group_table.json

    # convert string dict to dict
    new_standings = json.loads(new_standings)

    assert group_table == new_standings
