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
A = []
for Day in Days:
     print(random.choices(Mood))
for Time in Times:
      A = [Days[0],Time,random.choices(Mood), Days[1],Time,random.choices(Mood), Days[2],Time,random.choices(Mood), Days[3],Time,random.choices(Mood), Days[4],Time,random.choices(Mood),Days[5],Time,random.choices(Mood),Days[6],Time,random.choices(Mood)] 
      print(A)  
# Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, 
# all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected.

