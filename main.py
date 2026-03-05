from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
import webbrowser
from database import Database
from datetime import datetime

# Data for workout plan
workout_plan = {
    "Day 1: Push": [
        ("Bench Press", "https://www.youtube.com/watch?v=HnQGKxU3eds"),
        ("Overhead Press", "https://www.youtube.com/watch?v=2yjwXTZQDDI"),
        ("Incline Dumbbell Press", "https://www.youtube.com/watch?v=8iPEnn-ltC8"),
        ("Tricep Dips", "https://www.youtube.com/watch?v=6kALZikXxLc"),
        ("Dumbbell Flyes", "https://www.youtube.com/watch?v=eozdVDA78K0"),
        ("Lateral Raises", "https://www.youtube.com/watch?v=3VcKaXpzqRo")
    ],
    "Day 2: Pull": [
        ("Deadlifts", "https://www.youtube.com/watch?v=ytGaGIn3SjE"),
        ("Pull-Ups", "https://www.youtube.com/watch?v=HRVfAt4hx38"),
        ("Barbell Rows", "https://www.youtube.com/watch?v=1u6KJxNmWe8"),
        ("T-Bar Rows", "https://www.youtube.com/watch?v=U_FpR3TFKek"),
        ("Face Pulls", "https://www.youtube.com/watch?v=rep-qVOkqgk"),
        ("Hammer Curls", "https://www.youtube.com/watch?v=TwD-YGVP4Bk")
    ],
    # Add more days similarly and update the video links accordingly
}

class MyGymApp(App):
    def build(self):
        self.db = Database()

        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.scroll_view = ScrollView()
        self.box = BoxLayout(orientation='vertical', size_hint_y=None)
        self.box.bind(minimum_height=self.box.setter('height'))

        # Add header and buttons for different functionalities
        header = Label(text='My Gym Plan', font_size=24, size_hint_y=None, height=50)
        self.main_layout.add_widget(header)
        
        profile_button = Button(text="User Profile", size_hint_y=None, height=50)
        profile_button.bind(on_release=self.show_profile)
        self.main_layout.add_widget(profile_button)

        log_button = Button(text="Log Workout", size_hint_y=None, height=50)
        log_button.bind(on_release=self.log_workout)
        self.main_layout.add_widget(log_button)

        view_button = Button(text="View Workouts", size_hint_y=None, height=50)
        view_button.bind(on_release=self.view_workouts)
        self.main_layout.add_widget(view_button)

        self.display_workout_plan()
        self.scroll_view.add_widget(self.box)
        self.main_layout.add_widget(self.scroll_view)
        return self.main_layout

    def display_workout_plan(self):
        for day, exercises in workout_plan.items():
            day_label = Label(text=day, font_size=20, size_hint_y=None, height=40)
            self.box.add_widget(day_label)
            for exercise, url in exercises:
                button = Button(text=f"{exercise}: Video Link", size_hint_y=None, height=40)
                button.bind(on_release=lambda btn, url=url: self.open_link(url))
                self.box.add_widget(button)

    def open_link(self, url):
        webbrowser.open(url)

    def show_profile(self, instance):
        profile_data = self.db.get_profile()
        if profile_data:
            name, age, weight, height = profile_data[1], profile_data[2], profile_data[3], profile_data[4]
            content = BoxLayout(orientation='vertical', padding=10, spacing=10)
            content.add_widget(Label(text=f"Name: {name}"))
            content.add_widget(Label(text=f"Age: {age}"))
            content.add_widget(Label(text=f"Weight: {weight} kg"))
            content.add_widget(Label(text=f"Height: {height} cm"))
        else:
            content = BoxLayout(orientation='vertical', padding=10, spacing=10)
            content.add_widget(Label(text="No profile found. Please create one."))

            name_input = TextInput(hint_text="Name")
            age_input = TextInput(hint_text="Age", input_filter='int')
            weight_input = TextInput(hint_text="Weight (kg)", input_filter='float')
            height_input = TextInput(hint_text="Height (cm)", input_filter='float')
            
            save_button = Button(text="Save Profile")
            save_button.bind(on_release=lambda x: self.save_profile(name_input.text, age_input.text, weight_input.text, height_input.text))
            
            content.add_widget(name_input)
            content.add_widget(age_input)
            content.add_widget(weight_input)
            content.add_widget(height_input)
            content.add_widget(save_button)

        popup = Popup(title='User Profile', content=content, size_hint=(0.9, 0.9))
        popup.open()

    def save_profile(self, name, age, weight, height):
        self.db.add_profile(name, int(age), float(weight), float(height))
        self.show_profile(None)

    def log_workout(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        day_spinner = Spinner(text="Select Day", values=tuple(workout_plan.keys()))
        exercise_spinner = Spinner(text="Select Exercise", values=[])

        def update_exercises(spinner, text):
            exercise_spinner.values = [exercise for exercise, _ in workout_plan[text]]

        day_spinner.bind(text=update_exercises)

        sets_input = TextInput(hint_text="Sets", input_filter='int')
        reps_input = TextInput(hint_text="Reps", input_filter='int')

        save_button = Button(text="Log Workout")
        save_button.bind(on_release=lambda x: self.save_workout(day_spinner.text, exercise_spinner.text, sets_input.text, reps_input.text))
        
        content.add_widget(day_spinner)
        content.add_widget(exercise_spinner)
        content.add_widget(sets_input)
        content.add_widget(reps_input)
        content.add_widget(save_button)

        popup = Popup(title='Log Workout', content=content, size_hint=(0.9, 0.9))
        popup.open()

    def save_workout(self, day, exercise, sets, reps):
        date = datetime.now().strftime("%Y-%m-%d")
        self.db.log_workout(day, exercise, int(sets), int(reps), date)
        self.log_workout(None)

    def view_workouts(self, instance):
        workouts = self.db.get_workouts()
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        for workout in workouts:
            workout_label = Label(text=f"{workout[1]} - {workout[2]}: {workout[3]} sets of {workout[4]} reps on {workout[5]}")
            content.add_widget(workout_label)

        popup = Popup(title='Workout Log', content=content, size_hint=(0.9, 0.9))
        popup.open()

if __name__ == '__main__':
    MyGymApp().run()
