from file_system_utils import file_system_utils as fsu


TRIMMED_VIDS_DIR_PATH = "C:\\Users\\Brandon\\Documents\\Personal_Projects\\vhs_convert\\big_data\\trimmed_vids"

if __name__ == "__main__":
    trimmed_vid_name_l = fsu.get_dir_content_l(TRIMMED_VIDS_DIR_PATH, 'file', 'name')
    print(trimmed_vid_name_l)
    
    for trimmed_vid_name in trimmed_vid_name_l:
        og_abs_path = TRIMMED_VIDS_DIR_PATH + '//' + trimmed_vid_name
        
        f1_trimmed_vid_name = trimmed_vid_name.replace('-----', '------')
        print(f1_trimmed_vid_name)
        f2_trimmed_vid_name = f1_trimmed_vid_name.replace('_Trim', '')
        print(f2_trimmed_vid_name)
        
        new_abs_path = TRIMMED_VIDS_DIR_PATH + '//' + f2_trimmed_vid_name
        
        print(og_abs_path)
        print(new_abs_path)
        
        wait()
        fsu.rename_file_overwrite(og_abs_path)



    print('done')