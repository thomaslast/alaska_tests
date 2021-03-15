from pytest_bdd import scenario, given, when, then, steps
import pytest
from api_wrapper import ApiWrapper


@scenario('bdd_tests.feature', 'Happy day cases of bears api')
def test_publish():
    pass


@pytest.fixture
def api_wrapper():
    instance = ApiWrapper()
    yield instance


@given(u'there are no bears stored')
def check_no_bears(api_wrapper):
    bears = api_wrapper.get_all_bears()
    print(bears)
    assert bears == []


@then(u'there are no bears stored')
def check_no_bears_then(api_wrapper):
    check_no_bears(api_wrapper)


@given(u'the api wrapper object is created')
def create_api_wrapper(api_wrapper):
    if not api_wrapper:
        raise ConnectionError("not setup the api object")


@when(u'a bear is created with the following info')
def create_bear_table(api_wrapper):
    print(f"Values: {context.table[0]['bear_type']}")
    response = context.api_wrapper.add_a_bear(bear_type=context.table[0]["bear_type"],
                                   name=context.table[0]["name"],
                                   description=context.table[0]["description"],
                                   age=context.table[0]["age"])

    print(response)

    assert response == 200


@then(u'when the full bears list is requested, the bear is in the list')
def step_impl(context):
    pass





