import yaml
import logging

def load_settings():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def setup_logging(settings):
    logging.basicConfig(level=settings["logging"]["level"])
