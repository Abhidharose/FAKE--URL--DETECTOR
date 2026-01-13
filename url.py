def fake_url_detector(url):
    score=0
    reasons=[]
    if not url.startswith("https://"):
        score += 1
        reasons.append("Does not use HTTPS")
    
    if "@" in url:
        score+=1
        reasons.append("Contains @ symbol")
        
    suspicious_words=["login", "account", "verify", "secure", "update" , "activate"] 
    for word in suspicious_words:
        if word in url.lower():
            score+=1
            reasons.append("Suspicious word detected")
            break
    
    shorteners = ["bit.ly", "tinyurl", "t.co", "goo.gl"]
    for short in shorteners:
        if short in url:
          score += 2
          reasons.append("URL shortener detected")
          break
    
    if score <= 1:
        status = "LEGITIMATE"
    elif score <= 3:
        status = "SUSPICIOUS"
    else:
        status = "LIKELY FAKE"

    return status, score, reasons
    
url=input("enter the url:")
a,b,c=fake_url_detector(url)
print("\nScan Result:")
print("Status:", a)
print("Risk Score:", b)
if c:
    print("Reasons:")
    for r in c:
        print("-", r)
            