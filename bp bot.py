#GET THE DIFFERENT BP READINGS FROM THE USER
user_input = input("input the systolic blood pressure of the sample "
                   "patients (e.g 112, 113, 115, 117):\n")
bp_readings = [int(bp.strip()) for bp in user_input.split(",")]

#TO GET THE INITIAL COUNT OF THE DIFF. CATEGORIES OF BP
normal = 0
prehypertensive = 0
hypertensive = 0

#TO ANALYSE THE READINGS AND GROUP THEM INTO THE DIFFERENT CATEGORIES
for reading in bp_readings:
  if reading <= 120 and reading >= 100:
      normal += 1
  elif reading >= 120 and reading <= 139:
      prehypertensive += 1
  else:
      hypertensive += 1

#TO CALCULATE TOTAL PATIENTS
total = len(bp_readings)

#TO CALCULATE %
normal_pct = (normal/ total) * 100
prehypertensive_pct = (prehypertensive/ total) * 100
hypertensive_pct = (hypertensive/ total) * 100

#Those who are at risk of ischemic heart disease
ischaemic_risk = hypertensive

#FINAL OUTPUT
print(f"Here is Your final output:\n"
      f"Out of a total number of {total} patients:\n"
      f"NORMAL BP: {normal}({normal_pct:.1f}%)\n"
      f"PREHYPERTENSIVE: {prehypertensive}({prehypertensive_pct:.1f}%)\n"
      f"HYPERTENSIVE: {hypertensive}({hypertensive_pct:.1f}%)\n"
      f"{ischaemic_risk} patients are at risk of an ischaemic Heart disease")
