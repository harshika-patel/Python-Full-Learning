# list Comprehension---
# loop tranform and filtering(this one is optional)
domains=['www.google.com','openai.com','localhost','WWW.DATAWITHHARSHIKA>COM']

# for list compression we do 3 thing=[we combine 3 things
#     Data transformation,
#     # Loop -1st i make loop here because it is easy for d in domains:
#     DAta filtering
# ]
cleaned=[
    d.lower().replace("www.",'')
    for d in domains
    if '.' in d
]
print(domains)
print(cleaned)
cleaned=[
   d
    for d in domains
    if '.' in d
]
print(cleaned)