import os

# Define paths for your project
PROJECT_ROOT = os.getcwd()
DB_DIR = os.path.join(PROJECT_ROOT, "database")
os.makedirs(DB_DIR, exist_ok=True)

# SQLite database path
db_path = os.path.join(DB_DIR, "multimodal_rag.db")
print(f"Database path: {db_path}")