from venv import logger

from helper import validate_and_execute, user_input_message
import os
import logging

logging.getLogger("MAIN")
logger.error("error happended in app")

user_input = 1
while user_input != "exit":
    user_input = input(user_input_message)
    # list_of_days = user_input.split(": ")
    days_and_unit = user_input.split(":")
    days_and_unit_dic = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dic)
