'''Count Vowels and Consonants'''
def function(a):
    vowels = "aeiou"
    vowels_count = 0
    consonants_count = 0
    for ch in a:
        if ch.isalpha:
            if ch.lower() in vowels:
                vowels_count +=1
            else:
                consonants_count +=1
    print("number of vowels:",vowels_count )
    print("number of consonants:",consonants_count )
function("pythOn is a multi purpOse programming langUage")
