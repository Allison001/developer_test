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

printyaml.load(open("demo.yaml"),Loader=yaml.FullLoader)