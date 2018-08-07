from behave import when, then, given
from model.user import User
from model.post import Post



@given('we have a user id')
def step_impl(context):
    global random_user_id
    random_user_id = User.get_random_user_id()


@when('we call the API to save a new post using the user id')
def step_impl(context):
    global post_id
    response_post = Post.new_post(random_user_id, title="title", body="body")
    post_id = Post.get_post_id_from_response(response_post)


@then('the post is saved')
def step_impl(context):
    assert post_id == 101, "Post id was: " + post_id


@when('not informing a title')
def step_impl(context):
    global error_message
    try:
        Post.new_post(random_user_id, title="", body="body")
    except Exception as e:
        context.exception = e
        error_message = e


@then('API must return an error message')
def step_impl(context):
    assert error_message.message == 'Title should not be empty'

