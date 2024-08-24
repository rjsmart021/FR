import random
#Module 2 Lesson 4: Assignments | Python Loop Statements
#The Range Riddle
#Task 1:Your Mood Today Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it.Ensure that your program includes the use of the random module to select the mood.
import random
Mood = ["Happy", "Sad", "Energetic","Calm"]
Days = ["Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday", "Sunday"]
for Day in Days:
    print(random.choices(Mood))
#Double Scoop with Nested Loops
#Task 1: Your Mood Tracker Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
#for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate 
#over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.
Times = ["Morning", "Afternoon" ,"Evening"]
for Day in Days: 
        Schedule = [Day, Time]
        print(Schedule)
        for Times in Schedule:
              print(random.choices(Mood))
# Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected.

