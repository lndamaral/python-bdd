from behave import when, then
from model.user import User


@when('we get all users')
def step_impl(context):
    global jsonString
    jsonString = User.get_users()


@then('all users must have a name, username and email')
def step_impl(context):
    User.check_name(jsonString)
    User.check_username(jsonString)
    User.check_email(jsonString)


@then('all users must have a valid email')
def step_impl(context):
    User.check_valid_email(jsonString)


@then('all company catchphrase must have less than 50 characters')
def step_impl(context):
    User.check_catchphrase_length(jsonString)


@then('all users must have a zip code')
def step_impl(context):
    User.check_zip_code(jsonString)


@when('we use a specific {user_id}')
def step_impl(context, user_id):
    global userInfo
    userInfo = User.get_user_by_id(user_id)


@then('the {user_name} must be correspondent to the user id')
def step_impl(context, user_name):
    assert userInfo['name'] == user_name
