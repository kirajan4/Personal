# Created by kamatchi at 30-03-2020
Feature: URL Validation
  Validate the WURL Home page

  Scenario: URL Launch test
    Given I opened browser page
    Then I validate present in Search page
    When I enter the wurl.com in Search box
    And click on the I’m feeling lucky button
    Then I validate the wurl is present