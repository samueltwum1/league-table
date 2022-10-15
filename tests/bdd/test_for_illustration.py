"""
Verify that group table standings update with live score
"""

import json
import logging
import time
import requests

import pytest
from pytest_bdd import given, scenario, then, when
from pytest_bdd.parsers import parse

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def the_application():
    # app is run from another terminal session
    pass


@scenario("group_table.feature", "Group table from match results")
def test_league_standings_update():
    pass


@given("an example league table application")
def example_league_application(the_application):
    pass


@when(parse("fresh {match_results} come through"))
def fresh_match_results(match_results):
    requests.post("http://localhost:8080/league_table", data=match_results)


@then(parse("group table should reflect the {new_standings}"))
def league_table(new_standings):
    group_table = requests.get("http://localhost:8080/league_table")
    group_table = group_table.json()
    # apply delays between get requests to avoid to case of
    # exceeding periodic request quota. replace sleep with better solution
    time.sleep(1)

    # convert string dict to dict
    new_standings = json.loads(new_standings)

    assert group_table == new_standings
