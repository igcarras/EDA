# copy files from folders to
import glob, shutil
import os
import re

NIA_PATTERN = r"_\d{7}_"


def copy_files(scr_dir: str, dst_dir: str) -> None:
    """rename the files and copy them to a new folder"""
    print('source folder:', scr_dir)
    print('destine folder:', dst_dir)
    if not os.path.exists(dst_dir):
        print(dst_dir, " was created!!!")
        os.makedirs(dst_dir)

    i = 0
    for src_file in glob.glob(scr_dir, recursive=True):
        # print(src_file)
        try:
            nia = re.search(NIA_PATTERN, src_file)
            new_name = nia.group(0)[1:-1]
        except:
            print("error: " + src_file)
            new_name = 'unknown' + str(i)
            i += 1

        dst = dst_dir + new_name + '.py'
        # print("new file: ", dst)
        if os.path.exists(dst):
            os.remove(dst)
        shutil.copy(src_file, dst)

def clean_code(path, methods_remove = []):
    for name in glob.glob(path):
        print('cleaning', name)
        _clean_code(name, methods_remove)


def _clean_code(path, methods_remove):
    f = open(path, "r")
    # each sentence becomes an element in the list l
    lines = f.readlines()
    new_lines = []
    add_line = True
    for line in lines:
        # print(line)
        if line.find('if __name__ == ') != -1:
            break
        if len(line.strip()) > 0:
            if len(methods_remove)>0:
                found_method = False
                for name in methods_remove:
                    if line.find('def ' + name) != -1:
                        found_method = True
                        add_line = False
                        break
                if not found_method and \
                        (line.find('def ') != -1 or line.find('Class ') != -1):
                    add_line = True

            if add_line:
                new_lines.append(line.rstrip()+'\n')

    # acts as a counter to know the
    # index of the element to be replaced
    # print(new_lines)
    f.close()
    f = open(path, "w")
    f.writelines(new_lines)
    f.close()
    print(path + " successfully cleaned!!!")


if __name__ == '__main__':
    problem = 'p1'
    if problem == 'p2':
        copy_files('./p2/*/*/graphproblem*.py', './p2_clean/')
        methods_remove = ['compare_lists', '__init__', 'check_vertex',
                        'add_edge', '__eq__', '__str__']
        clean_code('./p2_clean/*.py', methods_remove)
    elif problem == 'p1':
        copy_files('./p1/*/*/dcproblem.py', './p1_clean/')
        clean_code('./p1_clean/*.py')

