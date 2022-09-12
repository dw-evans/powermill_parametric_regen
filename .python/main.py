"""
Daniel Evans
07 Sep 2022

Utilities to use with autoregen*.mac for parametric boundary etc regeneration

NTS: could do something with creo and trail files to generate the
assemblies for use in powermill...
"""

from pathlib import Path

from utils import create_copies
from utils import write_list_of_step_children

BASE = Path(r'L:\Daniel E\Documents\23 niv tube\11 retool\.powermillthings\626985_tool\626985_insert1')
base_name = "626985_tool_insert1_"
create_copies_settings = {
        "filenames_txt_path": BASE / (base_name + 'filenames.txt'),
        "copy_target_path": BASE / (base_name +'.prt.2'),
        "suffix": ".prt.1"
}
# create_copies(**create_copies_settings)

starts_with = base_name
write_list_of_step_children_settings = {
    "search_dir": BASE / "",
    "out_file_path": BASE / (base_name + "pwrm_models.txt"),
    "starts_with": base_name,
    "ignore_filename_list": [base_name + "asm.stp"],
}
write_list_of_step_children(**write_list_of_step_children_settings)


print("done")