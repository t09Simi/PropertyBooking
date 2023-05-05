Feature: Booking a Room

    Scenario: User books a room
        Given the user is on the property page
        When the user selects the check-in and check-out dates
        And the user clicks on the "Book Now" button
        Then the user should see a confirmation message
        