import psycopg2
import sys
import socket
import ipaddress

# AWS RDS Configuration
DB_HOST = "database-1.cluster-cvmqke06kfad.ap-south-1.rds.amazonaws.com"
DB_USER = "profile_postgres" 
# Use the password provided by the user
DB_PASSWORD = "U<PiV|oq1_#[1M>:iy|x!pwb*1J5"
DB_NAME = "postgres"

print(f"Resolving DNS for: {DB_HOST}")
try:
    ip = socket.gethostbyname(DB_HOST)
    print(f"Resolved IP: {ip}")
    
    # Check if IP is private
    if ipaddress.ip_address(ip).is_private:
        print("\n\n⚠️  CRITICAL CONFIGURATION ISSUE ⚠️")
        print(f"The Database IP ({ip}) is a PRIVATE (Internal) address.")
        print("Your laptop cannot reach this address because 'Publicly Accessible' is set to NO.")
        print("\n✅ HOW TO FIX:")
        print("1. Go to RDS Console -> Databases.")
        print("2. Click on the WRITER Instance (database-1-instance-1).")
        print("3. Click 'Modify'.")
        print("4. Scroll down to 'Connectivity'.")
        print("5. Change 'Publicly accessible' from 'Not publicly accessible' to 'Publicly accessible'.")
        print("6. Scroll to bottom -> Continue -> Select 'Apply Immediately' -> Modify Instance.")
        print("\n(Note: Also ensure you clicked 'Save rules' on your Security Group!)")
    
    print("\nAttempting connection (this will fail if IP is private)...")
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        connect_timeout=5
    )
    print("\n✅ SUCCESS! Connected to Database.")
    conn.close()

except Exception as e:
    print(f"\n❌ CONNECTION FAILED: {e}")
