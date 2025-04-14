print("🔍 Welcome to the Website Checker! 🔍")

website_url = input("\nEnter the website URL: ")

if (website_url.__contains__("http://")):
    print("🔓 This website uses HTTP (not secure)")
elif website_url.__contains__("https://"):
    print("🔐 This website uses HTTPS (secure)")
else:
    print("❌ This does not look like a website")
