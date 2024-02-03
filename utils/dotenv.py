from dotenv import load_dotenv
import os

load_dotenv()


def get_dotenv_variable(variable_name):
    variable_value = os.getenv(variable_name)
    return variable_value
