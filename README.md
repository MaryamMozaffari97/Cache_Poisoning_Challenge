# Cache_Poisoning_Challenge
Cache poisoning vulnerability scenario
ctf_challenge is Django's original code, which contains 2 scenarios for cache poisoning.

Scenario 1: Django Basic Web includes login and forget _password pages.

in this challenge the vulnerable application allow to the each user to cache the file that contain sensitive information. this issue will be allow to attacker to make the link and send it to the admin to cache the admin sensitive information in the cache server . so the admin(victim ) authentication is accessible for attacker or every one that request it form the cache server . and attacker use this authentication information to login to the admin panel and capture the flag .

Scenario 2:
