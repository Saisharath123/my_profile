# skill_analyzer_registration.py
import psycopg2
from flask import request, redirect, url_for, flash, render_template_string

# AWS RDS Configuration (Aurora PostgreSQL)
DB_HOST = "database-1.cluster-cvmqke06kfad.ap-south-1.rds.amazonaws.com"
DB_USER = "profile_postgres" 
DB_PASSWORD = "U<PiV|oq1_#[1M>:iy|x!pwb*1J5"
DB_NAME = "postgres"  # Default DB name. Change if you created a specific one like 'skill_analyzer_db'

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            connect_timeout=5
        )
        return connection
    except Exception as e:
        print(f"Error connecting to RDS (Postgres): {e}")
        return None

def init_db():
    """Creates the registrations table if it doesn't exist."""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                create_table_query = """
                CREATE TABLE IF NOT EXISTS registrations (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    institution VARCHAR(255),
                    mobile VARCHAR(20),
                    email VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW()
                )
                """
                cursor.execute(create_table_query)
            conn.commit()
        except Exception as e:
            print(f"Error initializing DB: {e}")
        finally:
            conn.close()

def register_routes(app, render_page_func):
    # Initialize DB table on startup (optional, or call manually)
    init_db()

    @app.route("/skill-registration", methods=["GET", "POST"])
    def skill_registration():
        if request.method == "POST":
            # Extract form data
            name = request.form.get("name")
            institution = request.form.get("institution")
            mobile = request.form.get("mobile")
            email = request.form.get("email")
            
            # Save to RDS
            conn = get_db_connection()
            if conn:
                try:
                    with conn.cursor() as cursor:
                        sql = "INSERT INTO registrations (name, institution, mobile, email) VALUES (%s, %s, %s, %s)"
                        cursor.execute(sql, (name, institution, mobile, email))
                    conn.commit()
                    flash(f"Thank you, {name}! Your registration has been saved to the database.", "success")
                except Exception as e:
                    print(f"DB Insert Error: {e}")
                    flash("An error occurred while saving your data. Please try again.", "error")
                finally:
                    conn.close()
            else:
                flash("Database connection failed. Please check configuration.", "error")

            return redirect(url_for("skill_analyzer"))

        # Render the registration form
        form_html = """
        <style>
            .reg-container {
                max-width: 600px;
                margin: 40px auto;
                background: #fff;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.05);
                border: 1px solid #e2e8f0;
            }
            .reg-header {
                text-align: center;
                margin-bottom: 30px;
            }
            .reg-header h2 {
                font-family: 'Outfit', sans-serif;
                font-size: 2rem;
                color: #1e293b;
                margin-bottom: 10px;
            }
            .reg-header p {
                color: #64748b;
            }
            .form-group {
                margin-bottom: 20px;
            }
            .form-label {
                display: block;
                font-weight: 600;
                color: #334155;
                margin-bottom: 8px;
                font-size: 0.95rem;
            }
            .form-control {
                width: 100%;
                padding: 12px 16px;
                border: 1px solid #cbd5e1;
                border-radius: 10px;
                font-size: 1rem;
                color: #0f172a;
                transition: border-color 0.2s, box-shadow 0.2s;
                box-sizing: border-box;
            }
            .form-control:focus {
                border-color: #3b82f6;
                outline: none;
                box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
            }
            .submit-btn {
                width: 100%;
                background: linear-gradient(135deg, #3b82f6, #2563eb);
                color: white;
                border: none;
                padding: 14px;
                border-radius: 10px;
                font-size: 1rem;
                font-weight: 700;
                cursor: pointer;
                transition: transform 0.1s, box-shadow 0.2s;
                margin-top: 10px;
            }
            .submit-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(37,99,235,0.2);
            }
            .submit-btn:active {
                transform: translateY(0);
            }
        </style>

        <div class="reg-container">
            <div class="reg-header">
                <h2>Registration</h2>
                <p>Register to access the Live Test or Virtual Interview.</p>
            </div>
            
            <form method="POST" action="/skill-registration">
                <div class="form-group">
                    <label class="form-label" for="name">Full Name</label>
                    <input type="text" id="name" name="name" class="form-control" placeholder="Enter your full name" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="institution">Institution / College</label>
                    <input type="text" id="institution" name="institution" class="form-control" placeholder="University or Company Name" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="mobile">Mobile Number</label>
                    <input type="tel" id="mobile" name="mobile" class="form-control" placeholder="+91 XXXXX XXXXX" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="email">Email Address</label>
                    <input type="email" id="email" name="email" class="form-control" placeholder="you@example.com" required>
                </div>
                
                <button type="submit" class="submit-btn" id="regSubmitBtn">Register Now</button>
            </form>
        </div>
        """
        return render_page_func(form_html, active="skill-analyzer")
