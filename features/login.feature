Feature: User login functionality

  Scenario: Successful login
    Given I am on the login page
    When I enter username as "testuser" and password as "password123"
    Then I should see the dashboard page
