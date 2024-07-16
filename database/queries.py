class ReviewQueries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS feedbacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number TEXT,
        visit_date DATE,
        food_rating REAL,
        cleanliness_rating REAL,
        extra_comments TEXT
    )
    """
    