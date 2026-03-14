# Python Built-in Modules from 3.14 version from A to Z

- Note: Some modules are platform-specific (e.g., fcntl, posix, pty are Unix-only; winreg, winsound are Windows-only). A few older modules (like aifc, cgi, telnetlib) have been deprecated and removed in Python 3.11–3.13. Always check the official Python docs for your specific version. (<https://docs.python.org/3/py-modindex.html>)

abc – Abstract Base Classes
aifc – Read/write AIFF and AIFC audio files
argparse – Command-line argument parsing
array – Efficient arrays of numeric values
ast – Abstract Syntax Trees
asynchat – Asynchronous command/response handler
asyncio – Asynchronous I/O
asyncore – Asynchronous socket handler
atexit – Exit handlers
audioop – Raw audio data operations

base64 – Base16, Base32, Base64 encoding
bdb – Debugger framework
binascii – Binary and ASCII conversions
binhex – BinHex4 files encoding/decoding
bisect – Array bisection algorithm
builtins – Built-in functions and exceptions
bz2 – bzip2 compression

calendar – Calendar-related functions
cgi – Common Gateway Interface support
cgitb – CGI traceback manager
chunk – Read IFF chunked data
cmath – Math functions for complex numbers
cmd – Line-oriented command interpreters
code – Interpreter base classes
codecs – Codec registry and base classes
codeop – Compile Python code
collections – Container data types
colorsys – Color system conversions
compileall – Byte-compile Python files
concurrent – Concurrent computation (futures)
configparser – Configuration file parser
contextlib – Utilities for with-statement contexts
contextvars – Context variables
copy – Shallow and deep copy operations
copyreg – Register pickle support
cProfile – C extension for deterministic profiling
csv – CSV file reading and writing
ctypes – Foreign function library
curses – Terminal handling for character-cell displays

dataclasses – Data classes
datetime – Date and time types
dbm – Interfaces to Unix databases
decimal – Decimal fixed-point and floating-point arithmetic
difflib – Helpers for computing deltas
dis – Disassembler for Python bytecode
doctest – Test interactive Python examples

email – Email and MIME handling
encodings – Character encoding support
enum – Enumerations
errno – Standard errno system symbols

faulthandler – Dump Python tracebacks
fcntl – Unix fcntl and ioctl calls
filecmp – File and directory comparisons
fileinput – Iterate over lines from multiple input streams
fnmatch – Unix filename pattern matching
fractions – Rational numbers
ftplib – FTP protocol client
functools – Higher-order functions and operations

gc – Garbage collector interface
getopt – C-style parser for command-line options
getpass – Portable password input
gettext – Multilingual internationalization
glob – Unix style pathname pattern expansion
grp – Unix group database
gzip – gzip file support

hashlib – Secure hash and message digest algorithms
heapq – Heap queue (priority queue) algorithm
hmac – Keyed-hashing for message authentication
html – HTML support
http – HTTP modules (client, server, cookies)

idlelib – IDLE support
imaplib – IMAP4 protocol client
imghdr – Determine image type
importlib – The import system
inspect – Inspect live objects
io – Core tools for working with streams
ipaddress – IPv4/IPv6 manipulation
itertools – Functions creating iterators for efficient looping

json – JSON encoder and decoder

keyword – Python keyword testing

lib2to3 – Python 2 to 3 code translator
linecache – Random access to text lines
locale – Internationalization services
logging – Logging facility
lzma – LZMA compression

mailbox – Manipulate mailboxes
marshal – Internal Python object serialization
math – Mathematical functions
mimetypes – Map filenames to MIME types
mmap – Memory-mapped file support
modulefinder – Find modules used by a script
multiprocessing – Process-based parallelism

netrc – Netrc file processing
nis – Sun's NIS (yellow pages)
nntplib – NNTP protocol client
numbers – Numeric abstract base classes

operator – Standard operators as functions
optparse – Command-line option parser
os – Miscellaneous operating system interfaces
ossaudiodev – Access OSS audio devices

pathlib – Object-oriented filesystem paths
pdb – Python debugger
pickle – Python object serialization
pickletools – Tools for pickle developers
pipes – Unix shell pipeline interface
pkgutil – Package extension utility
platform – Platform identification
plistlib – Apple .plist file generator/parser
poplib – POP3 protocol client
posix – POSIX system calls
pprint – Data pretty-printer
profile – Python source profiler
pstats – Statistics object for profiler
pty – Pseudo-terminal utilities
pwd – Unix password database
py_compile – Compile Python source files
pyclbr – Python class browser support
pydoc – Documentation generator

queue – Synchronized queue class
quopri – MIME quoted-printable encoding

random – Generate pseudo-random numbers
re – Regular expression operations
readline – GNU readline interface
reprlib – Alternate repr() implementation
resource – Resource usage information
rlcompleter – GNU readline completion

sched – Event scheduler
secrets – Generate secure random numbers
select – Waiting for I/O completion
selectors – High-level I/O multiplexing
shelve – Python object persistence
shlex – Lexical analysis
shutil – High-level file operations
signal – Set handlers for asynchronous events
site – Site-specific configuration hook
smtpd – SMTP server
smtplib – SMTP protocol client
sndhdr – Determine sound file type
socket – Low-level networking interface
socketserver – Framework for network servers
spwd – Shadow password database
sqlite3 – SQLite database interface
sre_compile / sre_parse – Regex internals
ssl – TLS/SSL wrapper for socket objects
stat – Interpret stat() results
statistics – Mathematical statistics functions
string – Common string operations
stringprep – Internet string preparation
struct – Interpret bytes as packed binary data
subprocess – Subprocess management
sunau – Read/write Sun AU files
symtable – Access compiler symbol tables
sys – System-specific parameters and functions
sysconfig – Python configuration information
syslog – Unix syslog library routines

tabnanny – Detection of ambiguous indentation
tarfile – Read/write tar archive files
telnetlib – Telnet client
tempfile – Generate temporary files and directories
termios – POSIX style tty control
test – Regression test package
textwrap – Text wrapping and filling
threading – Thread-based parallelism
time – Time access and conversions
timeit – Measure execution time
tkinter – GUI toolkit (Tcl/Tk interface)
token – Constants used in Python parse trees
tokenize – Tokenizer for Python source
tomllib – Parse TOML files (Python 3.11+)
traceback – Print/retrieve stack traces
tracemalloc – Trace memory allocations
tty – Terminal control functions
turtle – Turtle graphics
turtledemo – Demo viewer for turtle
types – Dynamic type creation
typing – Support for type hints

unicodedata – Unicode database
unittest – Unit testing framework
urllib – URL handling modules
uu – uuencode/decode files
uuid – UUID objects

venv – Creation of virtual environments

warnings – Warning control
wave – Read/write WAV files
weakref – Weak references
webbrowser – Web browser controller
wsgiref – WSGI utilities and reference implementation

xdrlib – XDR data encoding/decoding
xml – XML processing modules
xmlrpc – XML-RPC client and server
xrplib – XML-RPC library

zipapp – Manage executable Python zip archives
zipfile – Work with ZIP archives
zipimport – Import from ZIP archives
zlib – Compression using the zlib library
zoneinfo – IANA time zone support (Python 3.9+)
