# Import Module
import whois
import validators

def domain_check(dm):
    if validators.domain(dm):
        try:
            dm_info = whois.whois(dm)
            return dm_info
        except:
            return f"{dm} is not registered"
        
    else:
        return f"Enter a valid domain"
    
d_i = whois.whois("https://www.tryhackme.com")
print(d_i)