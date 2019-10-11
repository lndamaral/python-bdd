Feature: Save posts
save post descriptions

    Scenario: Saving a new post
        Given we have a user id
        When we call the API to save a new post using the user id
        Then the post is saved

    Scenario: Saving a new post without title
        Given we have a user id
        When we call the API to save a new post using the user id
        And not informing a title
        Then API must return an error message
