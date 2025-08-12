#FOR LOOP- YOU KNOW THE
# NUMBER OF PLATES
print("Using FOR loop to "
      "wash 5 plates!")
for plate in range(1, 6):
    print(f"Washing plate {plate}")
#WHILE LOOP - WASH UNTIL NO DIRTY PLATES
print("\n Using WHILE LOOP TO WASH "
      "PLATES TILL NONE IS LEFT")
dirty_plates = 5
while dirty_plates > 0:
    print(f"Washing plate"
          f" {dirty_plates}")
    dirty_plates -= 1