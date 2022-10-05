from tinytag import TinyTag as tt
import sys, os


extensions: str = [".mp3", ".flac", ".aac"]
arg: list = sys.argv
cwd: str = ""
format: list = ["%track%", ". ", "%artist%", " - ", "%title%", "%ext%"]


# Return a file's extension
def getExt(s: str) -> str:
	for i in range(len(s) - 1, 0, -1):
		if s[i] == '.':
			return s[i:]
	return "INVALID"


# Return the given string within quotes
def quoted(s: str) -> str:
	return '"'+s+'"'


# Print help for the script
if "--help" in arg:
	print("Options:")
	print("  --help                            -> display this page")
	print("  --dir [DIR_NAME]                  -> set specific directory as the working directory")
	print("  --ext \"[EXT1],[EXT2],[EXT3]...\" -> add other extensions to the valid extension list")
	print("  \t(use only if the script doesn't recognize your file)")
	print("  --format \"[FORMAT]\"             -> set the format that you want the new files to be in")
	print("  \tpossible format options:", list(tt(None, 0).__dict__.keys())[3:-4])
	print("  \tformat example:\n\t\t\"%track%. %artist% - %title% (released in %year%)\"\n\tturns into\n\t\t\"03. Blur - Parklife (released in 1994)\"")
	quit()


# If the --recurse argument is given, the script will search within folders (not implemented yet)
# recurse: bool = False
# if "--recurse" in arg:
# 	recurse = true


# Replace the current working directory with a given directory
if "--dir" in arg:
	cwd = arg[arg.index("--dir") + 1]


# Add other extensions to the valid extension list
if "--ext" in arg:
	exts: str = arg[arg.index("--ext") + 1].split(',')
	for e in range(len(exts)):
		if exts[e][0] != '.':
			exts[e] = '.' + exts[e]
	extensions += exts


# Set the format for the new file names (there is also a default format)
if "--format" in arg:
	format = arg[arg.index("--format") + 1].split('%')

	# Check if string starts with '%' (used to properly modify format list contents)
	startp: int = int(arg[arg.index("--format") + 1][0] == '%')

	# If it does start with '%', delete the first element, which is ''
	if startp == 1:
		format = format[1:]
	
	# If the last element in the format list is '', delete it
	if format[-1] == '':
		format = format[:-1]
	
	# Modify each element to add '%' to commands
	for i in range(len(format)):
		if i % 2 != startp:
			format[i] = '%'+format[i]+'%'
	
	format.append("%ext%")


# Set the list of files in the directory
flist: list = []
if cwd == "":
	cwd = os.getcwd()
flist = os.listdir(cwd)


# Actual rename of file
for f in flist:
	# Check if file has valid extension
	if getExt(f) in extensions:
		audio = tt.get(cwd + f)
		newfname: str = ""
		# Add components of the format to the new file name
		for comp in format:
			if comp == "%ext%":
				newfname += getExt(f)
			elif comp[0] == '%':
				if comp == "%track%" and int(getattr(audio, comp[1:-1])) <= 9 and getattr(audio, comp[1:-1])[0] != '0':
					newfname += '0'
				newfname += getattr(audio, comp[1:-1])
			else:
				newfname += comp
		
		# Rename the file
		os.rename(cwd + f, cwd + newfname)
		print(quoted(f), "->", quoted(newfname))
	else:
		# Specify skipped files due to invalid extension
		print(quoted(f), "-> skipped")
