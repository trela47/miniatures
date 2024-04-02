#recursively check if all files in dir1 are in dir2 for completeness 
#as far as I know this does not check for file content, but checks name, location, and metadata
#source: https://stackoverflow.com/questions/4187564/recursively-compare-two-directories-to-ensure-they-have-the-same-files-and-subdi


dir1= 'C:/Users/trela/OneDrive/Desktop/mindspaceai/main_work'
dir2= 'C:/Users/trela/Desktop/mindspaceai/main_work'

import filecmp
#print('hi')

def same_folders(dcmp):
    if dcmp.diff_files or dcmp.left_only or dcmp.right_only:
        print(dcmp.report())
        return False
    for sub_dcmp in dcmp.subdirs.values():
        if not same_folders(sub_dcmp):
            print(sub_dcmp.report())
            return False
    return True

print(same_folders(filecmp.dircmp(dir1, dir2)))

