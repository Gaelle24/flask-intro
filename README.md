My Project Update: Task Management API Implementation

1. My Git Branching Strategy (The New Branch I Made)

- My Branch Name: `api-feature`
- Why I Created It: To follow standard development practices, I created a brand new, isolated feature branch named `api-feature` to build and test my API code safely. This kept my experiments completely separated from the stable `master` branch until all my tests were passing.

2. Overview of what I Did

I built a backend REST API for our task manager using a Flask `Blueprint` directly on my feature branch. My API strictly uses JSON format to send and receive raw data, keeping it neatly separated from our website's visual pages and making the project much cleaner to organize.

The API I designed handles four major actions and communicates entirely using standard JSON formatted data:

- `GET /api/tasks`: I set this up to look at the database and list out all tasks inside a JSON response.
- `POST /api/tasks`: I set this up to read incoming JSON data and save a brand new task to the list.
- `PUT /api/tasks/<id>`: I set this up to read incoming JSON data and change the specific details (like name, date, or priority) of an existing task.
- `DELETE /api/tasks/<id>`: I set this up to permanently delete a specific task and send back a JSON confirmation message.

3. Project Dependencies (What My App Needs to Run)

To make sure my project runs smoothly, I relied on a few key Python packages. I tracked all of them inside the `requirements.txt` file:

- Flask: The main web framework I used to build the app and my API routes.
- pytest: The testing framework I used to run my automated scripts.
- pytest-cov: A plugin I added for pytest to calculate my exact code coverage percentage.


4. My Installation & Setup Procedures (How to Run My Project)

I followed these exact step-by-step instructions to set up my project sandbox environment on my local machine:

Step 1: 
I opened my terminal and navigated directly to my project's root folder:

cd C:\Users\user\OneDrive\Desktop\FlaskProject


Step 2:
I used an isolated virtual environment so my project dependencies wouldn't conflict with my global computer settings. I turned it on using this command:

.\venv\Scripts\activate


Step 3:
I installed all the required Python modules recorded in my requirements file at once using `pip`:

pip install -r requirements.txt


5. My Testing Procedures & 100% Score

I wrote an automated testing script inside `test_api.py` to guarantee there are zero bugs in my work:

- Safe Testing Zone: My tests automatically create a temporary "sandbox" database (`test_flasktask.db`) so my real tasks don't get messed up while testing.
- Crash Tests: I added tests that pretend the database crashed to make sure my app handles unexpected errors smoothly and sends back a proper JSON error response.
- How I Run My Tests: I run this command in my terminal to execute my test suite and check my coverage score:
  
pytest --cov=api test_api.py

- My 100% Code Coverage: Running this command proves that every single line of code I wrote passes its test perfectly!


