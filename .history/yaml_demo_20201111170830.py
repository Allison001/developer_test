import yaml

print(yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
""",Loader=yaml.FullLoader))


print(yaml.load("""
a :1
""")