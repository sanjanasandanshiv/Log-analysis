unknown_user = 0
auth_failure = 0
program_crash = 0
network_connections = 0
kerberos_fail = 0

login_users = {}
logout_users = {}


with open("logs/auth.log", "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        text = line.lower()

        if "check pass; user unknown" in text:
            unknown_user += 1
        
        elif "failure"  in text:
            auth_failure += 1
        
        elif "session opened for user" in text:
            user = text.split("user")[-1].strip()
            login_users[user] = login_users.get(user, 0) + 1

        elif "session closed for user" in text:
            user = text.split("user")[-1].strip()
            logout_users[user] = logout_users.get(user, 0) + 1

        elif "alert exited" in text:
            program_crash += 1

        elif "connection from" in text:
            network_connections += 1

        elif "kerberos authentication failed" in text:
            kerberos_fail += 1

print("Unknown user attempts →", unknown_user)
print("Authentication failures →", auth_failure)
print("Program crashes →", program_crash)
print("Network connections →", network_connections)
print("Kerberos failures →", kerberos_fail)


print("\nSuccessful logins:")
for user, count in login_users.items():
    print(user, "->", count)

print("\nLogouts:")
for user, count in logout_users.items():
    print(user, "->", count)