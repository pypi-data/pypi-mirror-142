#!/usr/bin/env python3

'''
# Git Parent gitp CLI Utility

A git wrapper script to help manage multi-repo projects. 
See https://gitlab.com/d2463/gitp for more information.
'''

import os, sys, fcntl, time, argparse, subprocess, shutil, enum, re, glob, shlex, datetime, socket, threading, functools, pkg_resources
import yaml
from subprocess import Popen, PIPE, STDOUT
from filelock import FileLock

try:
    VERSION = pkg_resources.require('gitparent')[0].version
except:
    VERSION = 'unknown'
DEFAULT_DEBUG_LEVEL = 0
DEBUG_LEVEL = DEFAULT_DEBUG_LEVEL
FORCE_COLORS = False
GIT_FALLBACK = False
CLI_RETURN_CODE = 0
PARSERS = {}

#ANCHOR: Utility Types
class Style(enum.Enum):
    '''
    Enumeration used for text styles.
    '''
    BOLD    = enum.auto()
    ITALIC  = enum.auto()
    BLUE    = enum.auto()
    CYAN    = enum.auto()
    GREEN   = enum.auto()
    RED     = enum.auto()
    YELLOW  = enum.auto()
    GRAY    = enum.auto()
    BLACK   = enum.auto()


#ANCHOR: Utility Methods
def gitp_operation(f):
    '''
    Decorator for all command-line operations of `gitp`. Handles argument parsing and debug message verbosity.
    '''
    PARSERS[f.__name__] = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, prog=f'{os.path.basename(__file__)} {f.__name__}', add_help=True)
    def wrapper(*argv, **kwargs):
        preprocess_method = getattr(PARSERS[f.__name__], '_preprocess_method', None)
        if preprocess_method:
            preprocess_method(PARSERS[f.__name__])
        my_args, unknowns = PARSERS[f.__name__].parse_known_args()
        global DEBUG_LEVEL
        global FORCE_COLORS
        if my_args.verbosity != DEFAULT_DEBUG_LEVEL:
            DEBUG_LEVEL = my_args.verbosity
        if my_args.color != False:
            FORCE_COLORS = my_args.color
        sys.argv = [sys.argv[0], '-v', str(DEBUG_LEVEL), '--color', str(FORCE_COLORS)]
        return f(my_args, unknowns, *argv, **kwargs)
    wrapper.__doc__ = f.__doc__
    return wrapper

def style(string, style_types, force=False):
    '''
    Apply text styling to a given string. Does nothing if the `stdout` is not a terminal.

    Args:
        string: string to style
        style_types: a list of `Style` types to apply to `string
        force: removes all existing styling prior to applying new style
    
    Returns:
        Styled string
    '''
    if not sys.stdout.isatty() and FORCE_COLORS != 'always':
        return string
    if force:
        # while re.search('\\033\[\d+m(.*?)\\033\[0m', string):
        string = re.sub('\\033\[\d+m(.*?)\\033\[0m', r'\1', string)
    if not isinstance(style_types, list):
        style_types = [style_types]
    for style_type in style_types:
        if style_type == Style.BOLD:
            string = f"\033[1m{string}\033[0m"
        if style_type == Style.ITALIC:
            string = f"\033[3m{string}\033[0m"
        if style_type == Style.BLUE:
            string = f"\033[94m{string}\033[0m"
        if style_type == Style.CYAN:
            string = f"\033[96m{string}\033[0m"
        if style_type == Style.GREEN:
            string = f"\033[92m{string}\033[0m"
        if style_type == Style.RED:
            string = f"\033[91m{string}\033[0m"
        if style_type == Style.YELLOW:
            string = f"\033[93m{string}\033[0m"
        if style_type == Style.GRAY:
            string = f"\033[97m{string}\033[0m"
        if style_type == Style.BLACK:
            string = f"\033[30m{string}\033[0m"
    return string

def debug(msg, level=0):
    '''
    Debug message print wrapper.

    Args:
        msg: message to print
        level: verbosity level of message
    '''
    if level <= DEBUG_LEVEL:
        print(msg)

def error(msg, level=0):
    '''
    Error message print wrapper.

    Args:
        msg: message to print
        level: verbosity level of message
    '''
    if level <= DEBUG_LEVEL:
        print(style(msg, Style.RED, force=True))
    global CLI_RETURN_CODE
    CLI_RETURN_CODE += 1

def _git(args, cwd=None, interactive=False, out_post_process=None):
    '''
    Utility method to execut a git command.

    Args: 
        args: arguments of the git command to run
        cwd: directory in which to execute the command
        interactive: interactive mode (stdin and stdout passthrough)
        out_post_process: string post processor for return value (run per-line of output)

    Returns:
        The stdout and stderr output of the command
    '''
    if sys.stdout.isatty() and FORCE_COLORS != 'always':
        args = '-c color.ui=always ' + args
    return _exec(['git'] + shlex.split(args), cwd, interactive, out_post_process)

def _exec(cmd, cwd=None, interactive=False, out_post_process=None):
    '''
    Utility method to execute an arbitrary system command.

    Args:
        cmd: command to execute
        cwd: directory in which to execute the command
        interactive: interactive mode (stdin and stdout passthrough)
        out_post_process: string post processor for return value (run per-line of output)

    Returns:
        The stdout and stderr output of the command
    '''
    cwd = cwd or '.'
    cwdstr = '' if cwd == '.' else f'({cwd})>'
    debug(f'${cwdstr} {cmd}', level=3)

    #Babysit interactive command
    if interactive:
        with Popen(cmd, cwd=cwd, stdin=sys.stdin, stdout=PIPE if out_post_process else sys.stdout, stderr=STDOUT) as p:
            ans = ''
            #STDOUT is piped -- handle output manually
            if out_post_process:
                newline = True
                while True:
                    exit = True if p.poll() is not None else False
                    #Perform non-blocking read
                    fd = p.stdout.fileno()
                    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
                    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
                    try:
                        out = p.stdout.read().decode('utf-8')
                    except:
                        out = ''
                    #Mirror stdout
                    else:
                        msg = out
                        if (newline or exit) and callable(out_post_process):
                            msg = out_post_process(msg)
                        newline = True if re.search(r'(?<!(\\))\n', out) else False
                        if newline or (not newline and out.strip() != ''): #this prevents corner cases from creeping in causing malformed output
                            print(msg, end='')
                        ans += msg
                    if exit:
                        if not ans.endswith('\n'):
                            print('')
                        break
                    time.sleep(0.1)
            #STDOUT is connected to sys.stdout -- wait for process to end
            else:
                p.wait()
        
            if p.returncode:
                raise subprocess.CalledProcessError(p.returncode, cmd, b'Failed running interactive command')
            return ans

    #Run non-interactive cmd in one go
    else:
        ans = subprocess.check_output(cmd, cwd=cwd, stderr=STDOUT).decode('utf-8')
        debug(ans.strip(), level=4)
        return '\n'.join([out_post_process(x) for x in ans.split('\n')]) if callable(out_post_process) else ans


#ANCHOR: help()
@gitp_operation
def help(args, unknowns, query=None):
    '''
    Prints the help message.
    '''
    query_found = True if query is None else False
    if query is None:
        print(getattr(sys.modules[__name__], '__doc__'))
        print(f"## Operations\n")

    for name,p in PARSERS.items():
        if query is None or name == query:
            print(f'### {name}')
            print('\n    '.join(p.format_help().split('\n')).replace('usage: ', '', 1))
            query_found = True
    if not query_found:
        raise Exception(f"Unknown gitp command '{query}' specified")


#ANCHOR: Universal Arguments
for name,p in PARSERS.items():
    p.add_argument('--verbosity', '-v', dest='verbosity', action='store', const=1, default=DEFAULT_DEBUG_LEVEL, nargs='?', type=int, help=argparse.SUPPRESS)
    p.add_argument('--color', dest='color', action='store', default=None, help=argparse.SUPPRESS)
    p.description = getattr(sys.modules[__name__], name).__doc__ or ''
    p.description = p.description.strip()


#ANCHOR: Main
def main():
    if len(sys.argv) == 1:
        help()
        sys.exit(0)
    orig_argv = [x for x in sys.argv]
    cmd = sys.argv.pop(1)

    if cmd == '--version':
        print(VERSION)
        sys.exit(0)

    #Intercept the git command with the gitp implementation
    if cmd in PARSERS:
        try:
            getattr(sys.modules[__name__], cmd)()
        except Exception as e:
            if DEBUG_LEVEL:
                raise
            print(style('Error: ' + str(e), Style.RED))
            sys.exit(1)

    #Run bare git command if it is not being intercepted by gitp
    if cmd not in PARSERS or GIT_FALLBACK:
        sys.argv.insert(1, cmd)
        try: 
            out = _git(('-c color.ui=always ' if sys.stdout.isatty() else '') + ' '.join(orig_argv[1:]))
            print(out, end='')
        except subprocess.CalledProcessError as e:
            print(e.output.decode('utf-8'), end='')
            sys.exit(1)

    sys.exit(CLI_RETURN_CODE)

if __name__ == '__main__':
    main()