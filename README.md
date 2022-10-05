# Music-Rename
Utility for renaming music files using their metadata

# Dependencies
- `python 3.10` and `pip`
- `tinytag`
  - installed with `python -m pip install tinytag`

# Usage
- run with `python mren {options}`
- `--help` display the help menu
- `--dir` set working directory
  - by default, this is the directory you ran the command in
  - example: `--dir "path/to/local/dir"` or `--dir "/path/to/dir/from/root"`
- `--ext` add extensions to the list of compatible extensions
  - write the extensions separated by `,`, without any spaces
  - example: `--ext "flac,mp3,aac"`
- `--format` set the file naming format you want to use for the new names
  - possible format options: `filesize` `album` `albumartist` `artist` `audio_offset` `bitrate` `channels` `comment` `composer` `disc` `disc_total` `duration` `extra` `genre` `samplerate` `title` `track` `track_total` `year`
  - format example: `"%track%. %artist% - %title% (released in %year%)"` turns into `"03. Blur - Parklife (released in 1994).mp3"`
  - default format: `"%track%. %artist% - %title%"`
