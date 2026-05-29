Project Update: Task Management API Implementation

Overview of What I Did:
I built a backend REST API for our task manager using a Flask `Blueprint`. This keeps our raw data code neatly separated from our website's visual pages, making the project much cleaner and easier to organize.

1. Changes to the Project Structure
- New API File: Created a brand new `api.py` file to handle all data requests.
- Connecting the Files: Connected this new API file directly to our main app inside `routes.py` using the `/api` web prefix.
- Database Connection: Connected the API safely to our SQLite database so it can read, save, and delete tasks.

2. The 4 New Routes Added
The API can now handle four major actions using standard JSON data:
- `GET /api/tasks`: Looks at the database and lists out all your tasks.
-`POST /api/tasks`: Saves a brand new task to your list.
- `PUT /api/tasks/<id>`: Changes the details (like name, date, or priority) of a specific task.
- `DELETE /api/tasks/<id>`: Permanently deletes a specific task from your list.

3. Testing and 100% Score
I wrote an automated testing script inside `test_api.py` to make sure there are zero bugs:
- Safe Testing Zone: The tests automatically create a temporary "sandbox" database so your real tasks don't get messed up during testing.
- Crash Tests: I added tests that pretend the database crashed to make sure our app handles unexpected errors smoothly.
- 100% Code Coverage: Running `pytest` proves that every single line of my new code passes its test perfectly!