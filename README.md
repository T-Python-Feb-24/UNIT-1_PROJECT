# UNIT-1_PROJECT


The script implements a basic parking management system. Here's an overview of what it does:

Registration of Cars: The script allows users to register cars by entering the license plate number and the start date of parking. It performs validation checks to ensure the license plate is unique and the format is correct.

Checking Car Status: Users can check the status of a car by entering its license plate number. The script searches the list of registered cars and informs the user whether the car is parked or not.

Car Leaving: When a car is ready to leave the parking lot, users can initiate the departure process by entering the license plate number. The script verifies if the car is parked, prompts for the end date of parking, and calculates the duration and cost of parking based on the hourly rate. It then displays this information to the user.

Parking Lot Status: The script checks if the parking lot is full by comparing the number of parked cars to a predefined limit. If the parking lot is full, no new cars can be registered.

Data Persistence: The script saves the information of parked cars to a JSON file so that it can be loaded and accessed later. This allows the parking lot's state to be preserved across different script executions.

Overall, the script provides a simple interface to manage parking operations, such as registering cars, checking their status, handling departures, and tracking parking duration and cost.