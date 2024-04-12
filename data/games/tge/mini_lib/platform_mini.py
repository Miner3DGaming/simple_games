import itertools
import os
import sys
import functools
import collections
import re

_uname_cache = None

_ver_output = re.compile(r'(?:([\w ]+) ([\w.]+) '
                         r'.*'
                         r'\[.* ([\d.]+)\])')

_WIN32_SERVER_RELEASES = {
    (5, 2): "2003Server",

    (6, 0): "2008Server",
    (6, 1): "2008ServerR2",
    (6, 2): "2012Server",
    (6, 3): "2012ServerR2",
    (6, None): "post2012ServerR2",
}

_WIN32_CLIENT_RELEASES = {
    (5, 0): "2000",
    (5, 1): "XP",
    # Strictly, 5.2 client is XP 64-bit, but platform.py historically
    # has always called it 2003 Server
    (5, 2): "2003Server",
    (5, None): "post2003",

    (6, 0): "Vista",
    (6, 1): "7",
    (6, 2): "8",
    (6, 3): "8.1",
    (6, None): "post8.1",

    (10, 0): "10",
    (10, None): "post10",
}

def system():

    """ Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.

        An empty string is returned if the value cannot be determined.

    """
    return uname().system

def _unknown_as_blank(val):
    return '' if val == 'unknown' else val

def _node(default=''):

    """ Helper to determine the node name of this machine.
    """
    try:
        import socket
    except ImportError:
        # No sockets...
        return default
    try:
        return socket.gethostname()
    except OSError:
        # Still not working...
        return default

def _syscmd_ver(system='', release='', version='',

               supported_platforms=('win32', 'win16', 'dos')):

    """ Tries to figure out the OS version used and returns
        a tuple (system, release, version).

        It uses the "ver" shell command for this which is known
        to exists on Windows, DOS. XXX Others too ?

        In case this fails, the given parameters are used as
        defaults.

    """
    if sys.platform not in supported_platforms:
        return system, release, version

    # Try some common cmd strings
    import subprocess
    for cmd in ('ver', 'command /c ver', 'cmd /c ver'):
        try:
            info = subprocess.check_output(cmd,
                                           stdin=subprocess.DEVNULL,
                                           stderr=subprocess.DEVNULL,
                                           text=True,
                                           encoding="locale",
                                           shell=True)
        except (OSError, subprocess.CalledProcessError) as why:
            #print('Command %s failed: %s' % (cmd, why))
            continue
        else:
            break
    else:
        return system, release, version

    # Parse the output
    info = info.strip()
    m = _ver_output.match(info)
    if m is not None:
        system, release, version = m.groups()
        # Strip trailing dots from version and release
        if release[-1] == '.':
            release = release[:-1]
        if version[-1] == '.':
            version = version[:-1]
        # Normalize the version and build strings (eliminating additional
        # zeros)
        version = _norm_version(version)
    return system, release, version

def _norm_version(version, build=''):

    """ Normalize the version and build strings and return a single
        version string using the format major.minor.build (or patchlevel).
    """
    l = version.split('.')
    if build:
        l.append(build)
    try:
        strings = list(map(str, map(int, l)))
    except ValueError:
        strings = l
    version = '.'.join(strings[:3])
    return version


def java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', '')):

    """ Version interface for Jython.

        Returns a tuple (release, vendor, vminfo, osinfo) with vminfo being
        a tuple (vm_name, vm_release, vm_vendor) and osinfo being a
        tuple (os_name, os_version, os_arch).

        Values which cannot be determined are set to the defaults
        given as parameters (which all default to '').

    """
    # Import the needed APIs
    try:
        import java.lang
    except ImportError:
        return release, vendor, vminfo, osinfo

    vendor = _java_getprop('java.vendor', vendor)
    release = _java_getprop('java.version', release)
    vm_name, vm_release, vm_vendor = vminfo
    vm_name = _java_getprop('java.vm.name', vm_name)
    vm_vendor = _java_getprop('java.vm.vendor', vm_vendor)
    vm_release = _java_getprop('java.vm.version', vm_release)
    vminfo = vm_name, vm_release, vm_vendor
    os_name, os_version, os_arch = osinfo
    os_arch = _java_getprop('java.os.arch', os_arch)
    os_name = _java_getprop('java.os.name', os_name)
    os_version = _java_getprop('java.os.version', os_version)
    osinfo = os_name, os_version, os_arch

    return release, vendor, vminfo, osinfo

def win32_ver(release='', version='', csd='', ptype=''):
    try:
        from sys import getwindowsversion
    except ImportError:
        return release, version, csd, ptype

    winver = getwindowsversion()
    try:
        major, minor, build = map(int, _syscmd_ver()[2].split('.'))
    except ValueError:
        major, minor, build = winver.platform_version or winver[:3]
    version = '{0}.{1}.{2}'.format(major, minor, build)

    release = (_WIN32_CLIENT_RELEASES.get((major, minor)) or
               _WIN32_CLIENT_RELEASES.get((major, None)) or
               release)

    # getwindowsversion() reflect the compatibility mode Python is
    # running under, and so the service pack value is only going to be
    # valid if the versions match.
    if winver[:2] == (major, minor):
        try:
            csd = 'SP{}'.format(winver.service_pack_major)
        except AttributeError:
            if csd[:13] == 'Service Pack ':
                csd = 'SP' + csd[13:]

    # VER_NT_SERVER = 3
    if getattr(winver, 'product_type', None) == 3:
        release = (_WIN32_SERVER_RELEASES.get((major, minor)) or
                   _WIN32_SERVER_RELEASES.get((major, None)) or
                   release)

    try:
        try:
            import winreg
        except ImportError:
            import _winreg as winreg
    except ImportError:
        pass
    else:
        try:
            cvkey = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
            with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, cvkey) as key:
                ptype = winreg.QueryValueEx(key, 'CurrentType')[0]
        except OSError:
            pass

    return release, version, csd, ptype


def _java_getprop(name, default):

    from java.lang import System
    try:
        value = System.getProperty(name)
        if value is None:
            return default
        return value
    except AttributeError:
        return default

def uname():

    """ Fairly portable uname interface. Returns a tuple
        of strings (system, node, release, version, machine, processor)
        identifying the underlying platform.

        Note that unlike the os.uname function this also returns
        possible processor information as an additional tuple entry.

        Entries which cannot be determined are set to ''.

    """
    global _uname_cache

    if _uname_cache is not None:
        return _uname_cache

    # Get some infos from the builtin os.uname API...
    try:
        system, node, release, version, machine = infos = os.uname()
    except AttributeError:
        system = sys.platform
        node = _node()
        release = version = machine = ''
        infos = ()

    if not any(infos):
        # uname is not available

        # Try win32_ver() on win32 platforms
        if system == 'win32':
            release, version, csd, ptype = win32_ver()
            machine = machine or _get_machine_win32()

        # Try the 'ver' system command available on some
        # platforms
        if not (release and version):
            system, release, version = _syscmd_ver(system)
            # Normalize system to what win32_ver() normally returns
            # (_syscmd_ver() tends to return the vendor name as well)
            if system == 'Microsoft Windows':
                system = 'Windows'
            elif system == 'Microsoft' and release == 'Windows':
                # Under Windows Vista and Windows Server 2008,
                # Microsoft changed the output of the ver command. The
                # release is no longer printed.  This causes the
                # system and release to be misidentified.
                system = 'Windows'
                if '6.0' == version[:3]:
                    release = 'Vista'
                else:
                    release = ''

        # In case we still don't know anything useful, we'll try to
        # help ourselves
        if system in ('win32', 'win16'):
            if not version:
                if system == 'win32':
                    version = '32bit'
                else:
                    version = '16bit'
            system = 'Windows'

        elif system[:4] == 'java':
            release, vendor, vminfo, osinfo = java_ver()
            system = 'Java'
            version = ', '.join(vminfo)
            if not version:
                version = vendor

    # System specific extensions
    if system == 'OpenVMS':
        # OpenVMS seems to have release and version mixed up
        if not release or release == '0':
            release = version
            version = ''

    #  normalize name
    if system == 'Microsoft' and release == 'Windows':
        system = 'Windows'
        release = 'Vista'

    vals = system, node, release, version, machine
    # Replace 'unknown' values with the more portable ''
    _uname_cache = uname_result(*map(_unknown_as_blank, vals))
    return _uname_cache

class uname_result(
    collections.namedtuple(
        "uname_result_base",
        "system node release version machine")
        ):
    """
    A uname_result that's largely compatible with a
    simple namedtuple except that 'processor' is
    resolved late and cached to avoid calling "uname"
    except when needed.
    """

    _fields = ('system', 'node', 'release', 'version', 'machine', 'processor')

    @functools.cached_property
    def processor(self):
        return _unknown_as_blank(_Processor.get())

    def __iter__(self):
        return itertools.chain(
            super().__iter__(),
            (self.processor,)
        )

    @classmethod
    def _make(cls, iterable):
        # override factory to affect length check
        num_fields = len(cls._fields) - 1
        result = cls.__new__(cls, *iterable)
        if len(result) != num_fields + 1:
            msg = f'Expected {num_fields} arguments, got {len(result)}'
            raise TypeError(msg)
        return result

    def __getitem__(self, key):
        return tuple(self)[key]

    def __len__(self):
        return len(tuple(iter(self)))

    def __reduce__(self):
        return uname_result, tuple(self)[:len(self._fields) - 1]

class _Processor:
    @classmethod
    def get(cls):
        func = getattr(cls, f'get_{sys.platform}', cls.from_subprocess)
        return func() or ''

    def get_win32():
        return os.environ.get('PROCESSOR_IDENTIFIER', _get_machine_win32())

    def get_OpenVMS():
        try:
            import vms_lib
        except ImportError:
            pass
        else:
            csid, cpu_number = vms_lib.getsyi('SYI$_CPU', 0)
            return 'Alpha' if cpu_number >= 128 else 'VAX'

    def from_subprocess():
        """
        Fall back to `uname -p`
        """
        try:
            import subprocess
        except ImportError:
            return None
        try:
            return subprocess.check_output(
                ['uname', '-p'],
                stderr=subprocess.DEVNULL,
                text=True,
                encoding="utf8",
            ).strip()
        except (OSError, subprocess.CalledProcessError):
            pass

def _get_machine_win32():
    # Try to use the PROCESSOR_* environment variables
    # available on Win XP and later; see
    # http://support.microsoft.com/kb/888731 and
    # http://www.geocities.com/rick_lively/MANUALS/ENV/MSWIN/PROCESSI.HTM

    # WOW64 processes mask the native architecture
    return (
        os.environ.get('PROCESSOR_ARCHITEW6432', '') or
        os.environ.get('PROCESSOR_ARCHITECTURE', '')
    )