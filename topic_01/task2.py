def StrFunc():
    origin = "  Hello world!  "
    stripped = origin.strip()
    print(f"strip():'{stripped}'") 
    capitalized = stripped.capitalize()
    print(f"capitalize():'{capitalized}'") 
    titled = origin.title()
    print(f"title():'{titled}'") 
    uppercased = origin.upper()
    print(f"upper():'{uppercased}'") 
    lowercased = origin.lower()
    print(f"lower():'{lowercased}'")
StrFunc()
