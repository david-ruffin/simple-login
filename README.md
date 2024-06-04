# simple-login
# Simple Login Project Setup

Follow these steps to set up and run the Simple Login project.

## Step 1: Clone the Repository

```bash
git clone https://github.com/test/simple-login.git
```

## Step 2: Change to the Project Directory

```bash
cd simple-login
```

## Step 3: Create a Virtual Environment

```bash
python3 -m venv venv
```

## Step 4: Activate the Virtual Environment

### On Linux or MacOS

```bash
source venv/bin/activate
```

### On Windows

```bash
venv\Scripts\activate
```

## Step 5: Install Flask

```bash
pip install Flask
```

## Step 6: Set Up the Database

```bash
python db_setup.py
```

## Step 7: Run the Flask Application

```bash
python app.py
```

## Additional Notes

- Make sure your `db_setup.py` script is correctly creating the database and `users` table.
- Clear your browser cache if you do not see the latest changes.

