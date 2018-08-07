Feature: List user info

    Scenario: Check if exists name, username and email
        When we get all users
        Then all users must have a name, username and email

    Scenario: Check if the email is valid
        When we get all users
        Then all users must have a valid email

    Scenario: Check if catchphrase has les than 50 characters
        When we get all users
        Then all company catchphrase must have less than 50 characters

    Scenario: Check if exists zip code
        When we get all users
        Then all users must have a zip code

    Scenario Outline: Check if the user name is correspondent to the user id
        When we use a specific <user_id>
        Then the <user_name> must be correspondent to the user id

    Examples:
       | user_id  | user_name                |
       | 1        | Leanne Graham            |
       | 2        | Ervin Howell             |
       | 3        | Clementine Bauch         |
       | 4        | Patricia Lebsack         |
       | 5        | Chelsey Dietrich         |
       | 6        | Mrs. Dennis Schulist     |
       | 7        | Kurtis Weissnat          |
       | 8        | Nicholas Runolfsdottir V |
       | 9        | Glenna Reichert          |
       | 10       | Clementina DuBuque       |
