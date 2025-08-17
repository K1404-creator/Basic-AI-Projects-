import sqlite3

conn = sqlite3.connect("customer_data.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS faq (question TEXT, response TEXT)")

faq_data = [
    ("How do I reset my password?", "To reset your password, go to Settings > Security."),
    ("What is your refund policy?", "We offer a 30-day refund policy for unused services."),
    ("How can I contact customer support?", "You can reach us via email at support@example.com."),
]

cursor.executemany("INSERT INTO faq (question, response) VALUES (?, ?)", faq_data)
conn.commit()
conn.close()

print("Database setup complete!")
