import yaml

print(yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
""",Loader=yaml.FullLoader))


yaml.load("""
a :1
""")