Weather Checking Application Documentation
Overview
This is a command-line weather checking application built using Python. It allows users to check the weather by city name, add or remove cities to/from their favorites list, view their favorite cities, and exit the application.

Features
Check Weather by City: Users can enter a city name to retrieve the current weather information for that city.

Add City to Favorites: Users can add a city to their favorites list.

Remove City from Favorites: Users can remove a city from their favorites list.

View Favorite Cities: Users can view the list of cities they have marked as favorites.

Exit: Users can exit the application.

Usage
Check Weather by City: Enter option 1, followed by the city name when prompted. The application will display the current weather information for the specified city.

Add City to Favorites: Enter option 2, followed by the city name when prompted. The city will be added to your list of favorite cities.

Remove City from Favorites: Enter option 3, followed by the city name when prompted. The city will be removed from your list of favorite cities if it exists.

View Favorite Cities: Enter option 4 to view your list of favorite cities. You can choose to check the weather for any city in your favorites list or exit back to the main menu.

Exit: Enter option 5 to exit the application.

Requirements
Python 3.x
PostgreSQL
psycopg2 library (pip install psycopg2)
requests library (pip install requests)
Setup
Ensure you have Python installed on your system.

Install PostgreSQL and create a database named "python".

Install the required Python libraries using pip.

Installation
Clone the repository from GitHub:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd Techplement/week1-tasks
Run the weather_app.py script:

Copy code
python weather_app.py
Additional Notes
The application uses the Weather API to fetch weather data for cities.
Ensure that you have a valid API key for the Weather API and update the API_KEY variable in the weather_app.py script.
The application will automatically connect to the PostgreSQL database named "python" using the provided credentials.
The database.py file contains functions related to database operations such as connecting to the database, creating tables, adding cities to favorites, and retrieving favorite cities.
The weather_app.py file contains the main application logic including the menu-driven interface and weather checking functionality.
Contact Information
For any questions or support, please contact:

Kasle Sumit Sandipam
sumitkasle007@gmail.com
