from pathlib import Path
import shutil

def create_copies(
    filenames_txt_path:Path, 
    copy_target_path:Path,
    suffix="prt.1",
    ):
    """
    Creates copies of a copy_target_path with names from filenames_txt_path
    where filenames txt is a .txt or similar with each filename separated by
    newlines
    """
    copy_to_dir = copy_target_path.parent
    with open(filenames_txt_path, 'r') as f:
        for filename in f.readlines():
            filename = filename.strip('\n') + suffix
            try:
                shutil.copy(copy_target_path, copy_to_dir / filename)
            except shutil.SameFileError:
                continue

def write_list_of_step_children(
    search_dir:Path, 
    out_file_path:Path,
    starts_with:str,
    ignore_filename_list:list,
    ):
    """
    writes list of *_asm.stp children *.stp files to txt file for
    model import in powermill
    """

    with open(out_file_path, 'w') as f:
        step_file_list = search_dir.glob('*.stp')
        for step_file in step_file_list:
            step_file_name = step_file.parts[-1]
            if step_file_name.startswith(starts_with):
                if not step_file_name in ignore_filename_list:
                    f.write(step_file.__str__() + "\n")
        
