# Play-Sound
Play music via hotkeys


## Feature

- Custom user-defined songs
- Custom user-defined song shortcut keys
- ...


## Define shortcut

**Usage**<br>
- Configure audio in the *config.ini* file. 
- Configure one audio per line. Format: shortcut key (space) audio file full name (space) audio description information.
- Do not use spaces in audio file names or audio descriptions.
- The `#` sign at the beginning of the line indicates that the line is a note information and will not be read.

**Example**
```
# notice: this is a description.
1 1.flac this-is-music1
2 2.flac this-is-music2
```

**Tips**<br>
- By default, the Ctrl + User Defined shortcut is used to play user-configured audio.
- Do not define shortcuts such as `a`, `c`, `v`, etc. to avoid affecting the system default operation.
- Shortcut key `~` default is to stop audio playback


## Packaging
Execute the following code in this project directory.
```shell script
pyinstaller --onefile main.py
```
