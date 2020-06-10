Feature: Test Trello API and UI
  Perform a basic test on Trello API, then one on the UI


  Scenario: Create a board and retrieve it
    Given a new board named New was created
    When I fetch the board by id
    Then I can verify the board name is New