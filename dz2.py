def cm_to_inches(length_cm):
    if length_cm < 0:
        return -1 * length_cm
    else:
        return round(length_cm / 2.54, 2)
try:
    length_cm = float(input("Введіть довжину в сантиметрах: "))
except ValueError:
    print("Будь ласка, введіть числове значення.")
else:
    length_inches = cm_to_inches(length_cm)
    print(f"{length_cm} см = {length_inches} дюймів")
