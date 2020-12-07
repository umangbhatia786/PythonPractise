val_kms = input('How many kilometers did you run today?\n')

val_miles = round(0.621 * float(val_kms), 2)

print(f'Your {val_kms} km run was {val_miles} miles')