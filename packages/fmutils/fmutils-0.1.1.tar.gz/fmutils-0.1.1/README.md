
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
 [![Generic badge](https://img.shields.io/badge/Version-0.1.1-red.svg)](https://shields.io/) [![Downloads](https://pepy.tech/badge/fmutils)](https://pepy.tech/project/fmutils)

# File Management Utilities (fmutils)

For easily accessing and managing large number of files and dirs in ML datasets.

## Implemented Functions
class `DirectoryTree` generator.  [source](https://github.com/Mr-TalhaIlyas/FMUtils/blob/722bf3f7312eb076b1be5108601ba32a8d2339dc/scripts/utils/directorytree.py#L20)

generates a dir tree displaying the full structure of the root dir, showing all the sub-dirs and the files.

<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>root_dir</strong> – absolute/relative path to root directory containing all files.</li>
<li><strong>dir_only</strong> – whether to only show sub-dirs in the dir-tree (excluding the files inside of each dir and sub-dir, good for getting an overview of large databases). The default is False.</li>
<li><strong>write_tree</strong> – write the full dir-tree in a txt file in current working dir. The default is True.</li>
</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first last"><li>None.</li></p>
</td>
</tr>
</tbody>


`get_all_files(main_dir, sort=True)` [source](https://github.com/Mr-TalhaIlyas/FMUtils/blob/main/scripts/fmutils.py#L23)

returns the list of all files inside the root dir.
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>main_dir</strong> – absolute/relative path to root directory containing all files.</li>
<li><strong>sort</strong> – wether to sort the output lost in Alphabetical order.</li>
</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first last"><li>list containing full paths of all files..</li></p>
</td>
</tr>
</tbody>



`get_all_dirs(main_dir, sort=True)` [source](https://github.com/Mr-TalhaIlyas/FMUtils/blob/722bf3f7312eb076b1be5108601ba32a8d2339dc/scripts/fmutils.py#L46)

returns the list of all the sub-dirs inside the root dir.
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>main_dir</strong> – absolute/relative path to root directory containing all files.</li>
<li><strong>sort</strong> – wether to sort the output lost in Alphabetical order.</li>
</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first last"><li> list containing full paths of all sub directories in root.</li></p>
</td>
</tr>
</tbody>


`get_num_of_files(main_dir)` [source](https://github.com/Mr-TalhaIlyas/FMUtils/blob/722bf3f7312eb076b1be5108601ba32a8d2339dc/scripts/fmutils.py#L69)

counts the number of files inside each sub-dir of the root.

<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>main_dir</strong> – absolute/relative path to root directory containing all files.</li>

</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first last">
<li><strong>num_per_class</strong> –  an array containing number of file in all sub dirs of root.</li>
<li><strong>name_classes</strong> –  name of all the sub-dirs/classes inside the root.</li>
<li><strong>total_files</strong> –  total number of files in all the sub-dir/classes.</li>
</p>
</td>
</tr>
</tbody>


`get_basename(full_path, include_extension=True)` [source](https://github.com/Mr-TalhaIlyas/FMUtils/blob/722bf3f7312eb076b1be5108601ba32a8d2339dc/scripts/fmutils.py#L97)

returns the basename of the file or the dir name at end of given path. In case of file you can choose wether to include the extension or not.
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>full_path</strong> – absolute/relative path to root directory containing all files.</li>
<li><strong>include_extension</strong> – if the input full_path leads to file the by default the the file's extension in included in output string.</li>
</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first last"><li> name of the file with/without extension or the base dir.</li></p>
</td>
</tr>
</tbody>


`get_random_files(main_dir, count=1)` [source](https://github.com/Mr-TalhaIlyas/FMUtils/blob/722bf3f7312eb076b1be5108601ba32a8d2339dc/scripts/fmutils.py#L117)

returns a list of randomly selected files from the root dir.

<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>main_dir</strong> – absolute/relative path to root directory containing all files.</li>
<li><strong>count</strong> – the number of files to get from root and its sub-dir.</li>
</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first last"><li> list containing full paths to randomly selected files.</li></p>
</td>
</tr>
</tbody>


`del_all_files(main_dir, confirmation=True)` [source](https://github.com/Mr-TalhaIlyas/FMUtils/blob/722bf3f7312eb076b1be5108601ba32a8d2339dc/scripts/fmutils.py#L137)

delete all files from root and all its sub-dirs.

<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first simple">
<li><strong>main_dir</strong> – absolute/relative path to root directory containing all files.</li>
<li><strong>confirmation</strong> – confirm before deleting the files.</li>
</ul>
</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body"><p class="first last"><li> None.</li></p>
</td>
</tr>
</tbody>


## Usage


For further details and more examples visit my [github](https://github.com/Mr-TalhaIlyas/FPUtils)

