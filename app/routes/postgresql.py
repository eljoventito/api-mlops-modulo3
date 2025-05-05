from fastapi import APIRouter, HTTPException
import psycopg2
import os
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


@router.get("/check-db")
def check_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return {
            "status": "success",
            "message": "Connected to the database successfully."
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "message": f"Database connection failed: {str(e)}"
            }
        )
