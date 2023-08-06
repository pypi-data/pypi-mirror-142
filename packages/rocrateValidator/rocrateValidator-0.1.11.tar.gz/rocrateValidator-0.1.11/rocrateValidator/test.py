import validate as validate
import syntaxCheck as syn
import semanticCheck as sem
import os

# def file_size_check1(tar_file):
    
#     NAME = "File size"
#     error_message = {
#         "FileSizeError": "Syntax Error: Empty File or Directory. Validation Aborted."
#     }
    
#     file_size = os.path.getsize(tar_file)
#     if file_size == 0:
#         return "0"
#     else:
#         return file_size


v = validate.validate("Directory")
print(v.get_final_result()["json check"])
