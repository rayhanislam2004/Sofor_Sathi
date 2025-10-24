Sofor Sathi - Your Travel Companion for Bangladesh

Sofor Sathi is a comprehensive, community-driven web application developed using the Django framework. It serves as an ultimate guide and planning tool designed specifically for travelers seeking to explore the diverse beauty of Bangladesh. The platform addresses the prevalent challenge of fragmented and often unreliable travel information by providing a centralized hub for discovering destinations, finding practical transportation routes, planning detailed itineraries, managing budgets, and sharing authentic travel experiences.

Project Repository: https://github.com/rayhanislam2004/rayhan81.git

The Problem Solved

Planning excursions within Bangladesh frequently involves navigating a complex landscape of outdated blogs, inconsistent social media advice, and disparate official websites. Sofor Sathi mitigates these difficulties by offering a singular, dependable resource that enables users to:

Discover verified and community-approved tourist locations.

Access detailed and practical transportation route information.

Consult authentic user reviews covering both destinations and the associated journeys.

Efficiently plan travel itineraries and estimate associated costs.

Actively contribute new information, ensuring the platform remains current and comprehensive through community engagement.

Key Features ✨

📍 Location Discovery: Browse or search an expanding database of tourist locations across Bangladesh, featuring detailed descriptions, high-quality images, user ratings, and categorization.

🗺️ Route Finder: A unique utility enabling users to filter transportation routes based on specified start and end points, complete with descriptive details submitted and verified by the community.

⭐ Dual Review System: A distinctive feature allowing users to submit separate reviews for both the Location (evaluating the destination experience) and the Route (assessing the transport and journey), providing a holistic perspective.

✈️ Trip Planner: Registered users can meticulously plan trips to specific locations, defining start and end dates.

💰 Budget Management: Integrates budget planning directly with trip plans, allowing users to track estimated expenditures across categories like transport, food, accommodation, and miscellaneous costs.

🪣 Bucket List: Enables users to curate a personalized list of desired travel destinations for future planning and inspiration.

👤 User Profiles: Offers personalized dashboards displaying planned trips, saved bucket list items, contributed reviews, and editable profile information.

🤝 Contribution System: Facilitates community growth by allowing logged-in users to suggest new locations and routes. Submissions undergo administrator review and approval via the Django Admin interface before public visibility, maintaining data integrity and quality.

🔍 Simple & Effective Search: Allows users to easily find locations based on name or geographical area.

Technology Stack 🛠️

Backend: Python 3.x, Django Framework 4.x

Frontend: HTML5, CSS3, Bootstrap 5

Database: SQLite (Default for Development), PostgreSQL recommended for Production

Image Handling: Pillow library

Installation and Setup (from GitHub) ⚙️

Follow these instructions to establish a local development environment for the project:

Prerequisites:

Python (Version 3.8 or higher recommended)

pip (Python package installer)

Git version control system

Clone the Repository:

git clone [https://github.com/rayhanislam2004/rayhan81.git](https://github.com/rayhanislam2004/rayhan81.git)
cd rayhan81 # Navigate into the cloned repository folder


Create and Activate Virtual Environment:

Strongly recommended for dependency isolation.

python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate


(Your terminal prompt should now indicate the active environment, e.g., (.venv))

Install Dependencies:

Ensure requirements.txt is present in the root directory.

pip install -r requirements.txt


Database Setup:

Initializes the database schema based on project models.

python manage.py makemigrations
python manage.py migrate


Create Superuser (Administrator Account):

Required for accessing the Django Admin interface.

python manage.py createsuperuser


(Follow the prompts to set username, email (optional), and password)

Run the Development Server:

python manage.py runserver


Access the Application:

Main Site: Open a web browser to http://127.0.0.1:8000/

Admin Panel: Navigate to http://127.0.0.1:8000/admin/ (Log in using superuser credentials)

Usage Instructions 🚶‍♀️

Explore: Navigate through locations using the "All Locations" page or utilize the homepage search bar.

Find Routes: Employ the "Route Finder" tool to filter available transport options based on departure and arrival points.

Authentication: Register for a new account or log in to utilize personalized features (Bucket List, Trip Planner, Contributions, Reviews).

Contribute: Access the "Contribute" section (requires login) to submit suggestions for new locations or routes, pending administrator approval.

Plan: Add appealing locations to your personal Bucket List or create comprehensive Trip Plans, complete with budget estimations, directly from location detail pages.

Review: Share valuable feedback by submitting reviews for both locations visited and transportation routes utilized.

Admin Management: Log in to the /admin/ interface as a superuser to review, approve, or manage user-submitted content (locations and routes) via the customized Django Admin configuration.

Project Structure 📁

The application employs a modular architecture, consisting of four primary Django apps:

userapp: Manages all user-related functions including authentication, registration, profile management, and session control.

tourismapp: Serves as the core content repository, managing data for locations, routes, categories, and associated user reviews.

tripapp: Contains features for personalized user planning, including the bucket list, trip itinerary creation, and detailed budget management.

contribution: Provides the user interface (forms and views) for submitting new content suggestions, interfacing with the admin approval workflow.

Developed By 🧑‍💻

This project is the collaborative effort of the following team members:

Rayhan Islam

Mehedi Hasan Khan Riyad

Md. Junaid Al Mahir

Nayem Ahmed

Thank you for your interest in Sofor Sathi. We are dedicated to making travel within Bangladesh more accessible, informed, and enjoyable for everyone.
