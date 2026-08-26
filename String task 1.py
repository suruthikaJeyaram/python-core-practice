#counts the number of vowels and consonants in a string.
a = "pythOn is a multi purpOse programming langUage"
vowels = "aeiou"
vowels_count = 0
consonants_count = 0

for ch in a:
    if ch.isalpha():
      if ch.lower() in vowels:
        vowels_count += 1
      else:
         consonants_count += 1

print("Number of vowels:",vowels_count)
print("Number of consonants:",consonants_count)
