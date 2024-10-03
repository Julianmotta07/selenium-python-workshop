Feature: Login Fb Feature
    Scenario: Successful login with valid credentials
    Given the user is on the facebook login page
    When the user logs in facebook with valid credentials
    Then the user should be redirected to the facebook dashboard page