print("Welcome To Dr. palazzo's Health & Wellness Check Bot!")
user_name = input("What is your name?")
sleep_hours =int(input("Hi " + user_name + "! How many hours of sleep did you have today?"))
water_intake = float(input("What is the estimated amount of water in litres you take in a day?"))
walked = input("Did you take a walk today? (yes/no):")
took_walk = walked.lower()
print("\nHERE'S YOUR MINI HEALTH & WELLNESS SNAPSHOT📷!")
print(f"🛌😴Sleep Hours : {sleep_hours}hours.\n💧🥤Estimated daily water Intake: {water_intake}L.\n 🚶‍♂️Took A Walk Today: {took_walk}.")
print("\nKeep taking care of you," + user_name + "! You got this. A little progress is still progress🥇" )
user_input = input( "input the systolic pressures of the patients (e.g 112, 114, 148):\n")


