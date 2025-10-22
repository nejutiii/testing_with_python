import datetime

def greeting_app():
    print("🌟 Welcome to the Ultimate Greeting App! 🌟")
    print("=" * 50)
    
    
    name = input("What's your name? ").strip()
    favorite_food = input("What's your favorite food? ").strip()
    
    current_year = datetime.datetime.now().year
    use_current_year = input(f"Use current year ({current_year})? (y/n): ").strip().lower()
    
    if use_current_year == 'y':
        year = current_year
    else:
        year = int(input("Enter the year: "))
    
    band_age = int(input("How many years have you been a fan of your favorite band? "))
    
    
    birth_year = year - band_age
    
    
    print("\n" + "=" * 50)
    print("🎉 HERE'S YOUR PERSONALIZED GREETING! 🎉")
    print("=" * 50)
    print(f"Hello {name}! 👋")
    print(f"It's awesome that you love {favorite_food}! 🍕")
    print(f"Based on your {band_age} years of being a band fan,")
    print(f"you likely started around {birth_year}! 🎸")
    print(f"That's {datetime.datetime.now().year - birth_year} years of amazing music! 🎵")
    print("\nThanks for using our greeting app! Have a great day! 🌈")

if name == "main":
    greeting_app()
