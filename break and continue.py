patients = ["john", "sarah",
            "No Form", "James",
            "Allergic to penicillin", "Maria" ]
for patient in patients:
    if patient == "No Form":
        print("Skipping - No Medical "
              "Form Submitted")
        continue
    if patient == "Allergic to penicillin":
        print("Alert! Allergy detected."
              " Stopping Check.")
        break
        print(f"checking {patient}'s record... ")