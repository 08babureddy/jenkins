Feature: User login functionality
  @TC_001
  Scenario: Successful login
    Given I am on the login page
    When I enter username as "testuser" and password as "password123"
    Then I should see the dashboard page
