import yaml

# Open the YAML file and load its contents
with open('./config.yaml', 'r') as file:
    config = yaml.safe_load(file)