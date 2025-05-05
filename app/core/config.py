# app/core/config.py
import yaml
import os


def cargar_config():
    config_path = os.path.join("app", "core", "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config
