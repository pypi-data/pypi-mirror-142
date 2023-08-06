
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
 [![Generic badge](https://img.shields.io/badge/Version-0.1.0-<COLOR>.svg)](https://shields.io/) [![Downloads](https://pepy.tech/badge/fputils)](https://pepy.tech/project/fputils)

# File Management Utilities (fmutils)

For easily accessing and managing large number of files and dirs in ML datasets.

## Implemented Functions
class `DirectoryTree` generator.  [source](https://github.com/Mr-TalhaIlyas/FPUtils)

generates a dir tree displaying the full structure of the root dir, showing all the sub-dirs and the files.

|||
| ----------- | ----------- |
| Parameters  | **root_dir** : absolute/relative path to root directory containing all files.|
|             | **dir_only** : whether to only show sub-dirs in the dir-tree (excluding the files inside of each dir and sub-dir, good for getting an overview of large databases). The default is False.  |
|             |**write_tree** : write the full dir-tree in a txt file in current working dir. The default is True.|
| Returns     |  *None*.  |

`get_all_files(main_dir, sort=True)` [source](https://github.com/Mr-TalhaIlyas/FPUtils)

returns the list of all files inside the root dir.
|||
| ----------- | ----------- |
| Parameters  | **main_dir** : absolute/relative path to root directory containing all files|
|             | **sort** : wether to sort the output lost in Alphabetical order.  |
| Returns     |  list containing full paths of all files.  |


`get_all_dirs(main_dir, sort=True)` [source](https://github.com/Mr-TalhaIlyas/FPUtils)

returns the list of all the sub-dirs inside the root dir.
|||
| ----------- | ----------- |
| Parameters  | **main_dir** : absolute/relative path to root directory containing all files|
|             | **sort** : wether to sort the output lost in Alphabetical order.  |
| Returns     |  list containing full paths of all sub directories in root.  |

`get_num_of_files(main_dir)` [source](https://github.com/Mr-TalhaIlyas/FPUtils)

counts the number of files inside each sub-dir of the root.
|||
| ----------- | ----------- |
| Parameters  | **main_dir** : absolute/relative path to root directory containing all files|
| Returns     | *num_per_class* : an array containing number of file in all sub dirs of root.|
||    *name_classes* : name of all the sub-dirs/classes inside the root.|
||    *total_files* : total number of files in all the sub-dir/classes.  |

`get_basename(full_path, include_extension=True)` [source](https://github.com/Mr-TalhaIlyas/FPUtils)

returns the basename of the file or the dir name at end of given path. In case of file you can choose wether to include the extension or not.
|||
| ----------- | ----------- |
| Parameters  | **full_path** : absolute/relative path of file or dir.|
|             | **sort** : if the input full_path leads to file the by default the the file's extension in included in output string.|
| Returns     |  name of the file with/without extension or the base dir.  |

`get_random_files(main_dir, count=1)` [source](https://github.com/Mr-TalhaIlyas/FPUtils)

returns a list of randomly selected files from the root dir.
|||
| ----------- | ----------- |
| Parameters  | **main_dir** : absolute/relative path to root directory containing all files|
|             | **count** : the number of files to get from root dir.  |
| Returns     |  list containing absolute path to the file(s).  |

`del_all_files(main_dir, confirmation=True)` [source](https://github.com/Mr-TalhaIlyas/FPUtils)

delete all files from root and all its sub-dirs.
|||
| ----------- | ----------- |
| Parameters  | **main_dir** : absolute/relative path to root directory containing all files|
|             | **confirmation** : confirm before deleting the files.  |
| Returns     |  None.  |

## Usage


For further details and more examples visit my [github](https://github.com/Mr-TalhaIlyas/FPUtils)
