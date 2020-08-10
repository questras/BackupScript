import os

import utils


def print_filepath_to_backup(filepath):
    size_formatted = utils.format_size(os.path.getsize(filepath))
    utils.colored(f'{filepath} ', 'green')
    utils.colored(f'{size_formatted}\n', 'blue')


def print_list_of_files_to_backup(filepaths_list):
    files_limit = 50
    size_sum = utils.format_size(
        sum([os.path.getsize(path) for path in filepaths_list]))
    
    for i in range(min(files_limit, len(filepaths_list))):
        print_filepath_to_backup(filepaths_list[i])
    
    if len(filepaths_list) > files_limit:
        remaining = len(filepaths_list) - files_limit
        utils.colored(f'...and ', 'green')    
        utils.colored(f'{remaining} ', 'blue')    
        utils.colored(f'more.\n', 'green')    
    
    utils.colored(f'Size: ', 'green')
    utils.colored(f'{size_sum}\n', 'blue')