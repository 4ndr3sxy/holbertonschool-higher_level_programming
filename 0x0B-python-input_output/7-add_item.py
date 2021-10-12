#!/usr/bin/python3
"""Imports"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    file_name = "add_item.json"
    information = load_from_json_file(file_name)
except:
    information = []
for obj in sys.argv[1:]:
    information.append(obj)
save_to_json_file(information, file_name)
