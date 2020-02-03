# FolderLookup
This script will take a search term from the user and scan both possible directories for folders. Any folder name that includes the search term will be opened, up to a maximum of 5 as overload protection.If the user desires to open more folders at once to have a more thorough search, the search term can be preceded by an asterisk.

Useful if you regularly have to access large directories many levels deep within a storage system. the script can be used to pre-define the directories of interest, and then repeatedly take a search term to open any applicable folders therein.

# Installation
Just clone on download the repo.

# Usage

To modify the script for your own purposes, you must make the below changes:

1.  Revise dir_path on line 23 to whatever directory path you want to be the default.
2.  Add all paths you wish to be able to access from within the program to dirpaths on line 27.
3.  Change list of directories on lines 64-69 accordingly to set your user-input for which directories to search and open from.
4.  Clean up initial print statement on lines 38-53 to reflect your use-case.

# The Unlicense:

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
