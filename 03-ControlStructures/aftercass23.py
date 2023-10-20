dog_age_human_years = int(input("Enter dog's age in human years:"))
if dog_age_human_years <= 2:
    dog_age_dog_years = dog_age_human_years * 10.5
else:
    dog_age_dog_years = 21 + ((dog_age_human_years-2) * 4)
print(f'Dog age in dog years:{dog_age_dog_years}')
