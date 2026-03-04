failed_logins: int = 0
successful_logins: int = 0

with open("logs/auth.log", "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        text = line.lower()

        if "authenticaton failure" in text or "invalid user" in text:
            failed_logins += 1
        
        if "session opened" in text:
            successful_logins += 1

print("Total Failed Logins:", failed_logins)
print("Total Successful Logins:", successful_logins)