from behave import *
import requests
from api_wrapper import ApiWrapper

@given(u'the api wrapper object is created')
def step_impl(context):
    if not context.api_wrapper:
        context.api_wrapper = ApiWrapper()

@given(u'there are no bears stored')
def step_impl(context):
    bears = context.api_wrapper.get_all_bears()
    assert bears == []

@when(u'a bear is created with the following info')
def step_impl(context):
    print(f"Values: {context.table[0]['bear_type']}")
    response = context.api_wrapper.add_a_bear(bear_type=context.table[0]["bear_type"],
                                   name=context.table[0]["name"],
                                   description=context.table[0]["description"],
                                   age=context.table[0]["age"])

    assert response == 200

@then(u'when the full bears list is requested, the bear is in the list')
def step_impl(context):
    pass





