import os
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_scan(target, result):
    data = {
        "target": target,
        "result": result
    }
    supabase.table("scans").insert(data).execute()
