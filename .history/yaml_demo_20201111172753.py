import yaml

# print(yaml.load("""
# - Hesperiidae
# - Papilionidae
# - Apatelodidae
# - Epiplemidae
# """,Loader=yaml.FullLoader))


# print(yaml.load("""
# a: 1
# b: 2
# """,Loader=yaml.FullLoader))

# print(yaml.load(open("demo.yaml"),Loader=yaml.FullLoader))

# print(yaml.load(open("demo.yaml"),Loader=yaml.FullLoader))

# print(yaml.dump({'a': [1, 2], 'b': [3, 4]}))

with open("demo2.yaml","w") as f:
    yaml.dump({'a': [1, 2], 'b': [3, 4]},str)