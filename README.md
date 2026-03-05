# My Gym App

A mobile gym workout tracking application built with Kivy and Python. Track your workouts, manage your profile, and follow structured workout plans with integrated video tutorials.

## Features

- **User Profile Management**: Create and manage your profile with name, age, weight, and height
- **Workout Plan Display**: View structured workout plans organized by training days (Push, Pull, etc.)
- **Exercise Video Links**: Access YouTube video tutorials for each exercise directly from the app
- **Workout Logging**: Log your workouts with sets, reps, and dates
- **Workout History**: View all your logged workouts in one place
- **SQLite Database**: Local data storage for profiles and workout logs

## Requirements

- Python 3.x
- Kivy
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Mobile-App
```

2. Install dependencies:
```bash
pip install kivy
```

## Usage

Run the application:
```bash
python main.py
```

### Features Overview

- **User Profile**: Click "User Profile" to create or view your profile information
- **Log Workout**: Click "Log Workout" to record your training sessions
- **View Workouts**: Click "View Workouts" to see your workout history
- **Exercise Videos**: Click on any exercise button to open the YouTube tutorial video

## Project Structure

```
Mobile App/
├── main.py           # Main application file with Kivy UI
├── database.py       # Database operations and SQLite setup
├── gymapp.kv         # Kivy layout file
├── buildozer.spec    # Buildozer configuration for Android builds
├── gym_app.db        # SQLite database (created automatically)
└── README.md         # This file
```

## Building for Android

This app can be built for Android using Buildozer:

1. Install Buildozer:
```bash
pip install buildozer
```

2. Build the APK:
```bash
buildozer android debug
```

## Database Schema

### user_profile
- `id`: Primary key
- `name`: User's name
- `age`: User's age
- `weight`: User's weight in kg
- `height`: User's height in cm

### workouts
- `id`: Primary key
- `day`: Workout day (e.g., "Day 1: Push")
- `exercise`: Exercise name
- `sets`: Number of sets
- `reps`: Number of reps
- `date`: Workout date

## Technologies Used

- **Kivy**: Cross-platform Python framework for mobile app development
- **SQLite3**: Lightweight database for local data storage
- **Python**: Programming language

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Created as a personal gym tracking solution.
