import psycopg2

# Function to establish a connection to the PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname="python",
            user="postgres",
            password="sumit123",
        )
        print("Connected to the database")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Function to create tables if they don't exist
def create_tables(conn):
    try:
        cursor = conn.cursor()
        # Table for storing previous search results
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS search_results (
                id SERIAL PRIMARY KEY,
                city VARCHAR(100) NOT NULL,
                weather_data JSONB NOT NULL
            )
        """)
        # Table for storing favorite cities
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS favorite_cities (
                id SERIAL PRIMARY KEY,
                city VARCHAR(100) NOT NULL UNIQUE
            )
        """)
        conn.commit()
        print("Tables created successfully")
    except psycopg2.Error as e:
        print("Error creating tables:", e)

# Function to add a city to favorites
def add_to_favorites(conn, city):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO favorite_cities (city) VALUES (%s) ON CONFLICT DO NOTHING", (city,))
        conn.commit()
        print(f"{city} added to favorites")
    except psycopg2.Error as e:
        print("Error adding city to favorites:", e)

# Function to retrieve favorite cities
def get_favorite_cities(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT city FROM favorite_cities")
        favorite_cities = [row[0] for row in cursor.fetchall()]
        return favorite_cities
    except psycopg2.Error as e:
        print("Error retrieving favorite cities:", e)
        return []
