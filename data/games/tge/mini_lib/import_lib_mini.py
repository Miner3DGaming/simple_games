from .. import sys
import _imp

_bootstrap_external = None
_warnings = None
_module_locks = {}
_weakref = None
_thread = None
_blocking_on = {}

class _DeadlockError(RuntimeError):
    pass

def _find_spec(name, path, target=None):
    """Find a module's spec."""
    meta_path = sys.meta_path
    if meta_path is None:
        # PyImport_Cleanup() is running or has been called.
        raise ImportError("sys.meta_path is None, Python is likely "
                          "shutting down")

    if not meta_path:
        _warnings.warn('sys.meta_path is empty', ImportWarning)

    # We check sys.modules here for the reload case.  While a passed-in
    # target will usually indicate a reload there is no guarantee, whereas
    # sys.modules provides one.
    is_reload = name in sys.modules
    for finder in meta_path:
        with _ImportLockContext():
            try:
                find_spec = finder.find_spec
            except AttributeError:
                spec = _find_spec_legacy(finder, name, path)
                if spec is None:
                    continue
            else:
                spec = find_spec(name, path, target)
        if spec is not None:
            # The parent import may have already imported this module.
            if not is_reload and name in sys.modules:
                module = sys.modules[name]
                try:
                    __spec__ = module.__spec__
                except AttributeError:
                    # We use the found spec since that is the one that
                    # we would have used if the parent module hadn't
                    # beaten us to the punch.
                    return spec
                else:
                    if __spec__ is None:
                        return spec
                    else:
                        return __spec__
            else:
                return spec
    else:
        return None
    

def find_spec(name, package=None):
    """Return the spec for the specified module.

    First, sys.modules is checked to see if the module was already imported. If
    so, then sys.modules[name].__spec__ is returned. If that happens to be
    set to None, then ValueError is raised. If the module is not in
    sys.modules, then sys.meta_path is searched for a suitable spec with the
    value of 'path' given to the finders. None is returned if no spec could
    be found.

    If the name is for submodule (contains a dot), the parent module is
    automatically imported.

    The name and package arguments work the same as importlib.import_module().
    In other words, relative module names (with leading dots) work.

    """
    fullname = resolve_name(name, package) if name.startswith('.') else name
    if fullname not in sys.modules:
        parent_name = fullname.rpartition('.')[0]
        if parent_name:
            parent = __import__(parent_name, fromlist=['__path__'])
            try:
                parent_path = parent.__path__
            except AttributeError as e:
                raise ModuleNotFoundError(
                    f"__path__ attribute not found on {parent_name!r} "
                    f"while trying to find {fullname!r}", name=fullname) from e
        else:
            parent_path = None
        return _find_spec(fullname, parent_path)
    else:
        module = sys.modules[fullname]
        if module is None:
            return None
        try:
            spec = module.__spec__
        except AttributeError:
            raise ValueError('{}.__spec__ is not set'.format(name)) from None
        else:
            if spec is None:
                raise ValueError('{}.__spec__ is None'.format(name))
            return spec
        
def _find_spec_legacy(finder, name, path):
    msg = (f"{_object_name(finder)}.find_spec() not found; "
                           "falling back to find_module()")
    _warnings.warn(msg, ImportWarning)
    loader = finder.find_module(name, path)
    if loader is None:
        return None
    return spec_from_loader(name, loader)

def _object_name(obj):
    try:
        return obj.__qualname__
    except AttributeError:
        return type(obj).__qualname__

def resolve_name(name, package):
    """Resolve a relative module name to an absolute one."""
    if not name.startswith('.'):
        return name
    elif not package:
        raise ImportError(f'no package specified for {repr(name)} '
                          '(required for relative module names)')
    level = 0
    for character in name:
        if character != '.':
            break
        level += 1
    return _resolve_name(name[level:], package, level)

def _resolve_name(name, package, level):
    """Resolve a relative module name to an absolute one."""
    bits = package.rsplit('.', level - 1)
    if len(bits) < level:
        raise ImportError('attempted relative import beyond top-level package')
    base = bits[0]
    return '{}.{}'.format(base, name) if name else base

def spec_from_loader(name, loader, *, origin=None, is_package=None):
    """Return a module spec based on various loader methods."""
    if origin is None:
        origin = getattr(loader, '_ORIGIN', None)

    if not origin and hasattr(loader, 'get_filename'):
        if _bootstrap_external is None:
            raise NotImplementedError
        spec_from_file_location = _bootstrap_external.spec_from_file_location

        if is_package is None:
            return spec_from_file_location(name, loader=loader)
        search = [] if is_package else None
        return spec_from_file_location(name, loader=loader,
                                       submodule_search_locations=search)

class _ImportLockContext:

    """Context manager for the import lock."""

    def __enter__(self):
        """Acquire the import lock."""
        _imp.acquire_lock()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Release the import lock regardless of any raised exceptions."""
        _imp.release_lock()

def _load_module_shim(self, fullname):
    """Load the specified module into sys.modules and return it.

    This method is deprecated.  Use loader.exec_module() instead.

    """
    msg = ("the load_module() method is deprecated and slated for removal in "
          "Python 3.12; use exec_module() instead")
    _warnings.warn(msg, DeprecationWarning)
    spec = spec_from_loader(fullname, self)
    if fullname in sys.modules:
        module = sys.modules[fullname]
        _exec(spec, module)
        return sys.modules[fullname]
    else:
        return _load(spec)

def _call_with_frames_removed(f, *args, **kwds):
    """remove_importlib_frames in import.c will always remove sequences
    of importlib frames that end with a call to this function

    Use it instead of a normal call in places where including the importlib
    frames introduces unwanted noise into the traceback (e.g. when executing
    module code)
    """
    return f(*args, **kwds)

def _requires_builtin(fxn):
    """Decorator to verify the named module is built-in."""
    def _requires_builtin_wrapper(self, fullname):
        if fullname not in sys.builtin_module_names:
            raise ImportError('{!r} is not a built-in module'.format(fullname),
                              name=fullname)
        return fxn(self, fullname)
    _wrap(_requires_builtin_wrapper, fxn)
    return _requires_builtin_wrapper

def _wrap(new, old):
    """Simple substitute for functools.update_wrapper."""
    for replace in ['__module__', '__name__', '__qualname__', '__doc__']:
        if hasattr(old, replace):
            setattr(new, replace, getattr(old, replace))
    new.__dict__.update(old.__dict__)

class BuiltinImporter:

    """Meta path import for built-in modules.

    All methods are either class or static methods to avoid the need to
    instantiate the class.

    """

    _ORIGIN = "built-in"

    @staticmethod
    def module_repr(module):
        """Return repr for the module.

        The method is deprecated.  The import machinery does the job itself.

        """
        _warnings.warn("BuiltinImporter.module_repr() is deprecated and "
                       "slated for removal in Python 3.12", DeprecationWarning)
        return f'<module {module.__name__!r} ({BuiltinImporter._ORIGIN})>'

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        if _imp.is_builtin(fullname):
            return spec_from_loader(fullname, cls, origin=cls._ORIGIN)
        else:
            return None

    @classmethod
    def find_module(cls, fullname, path=None):
        """Find the built-in module.

        If 'path' is ever specified then the search is considered a failure.

        This method is deprecated.  Use find_spec() instead.

        """
        _warnings.warn("BuiltinImporter.find_module() is deprecated and "
                       "slated for removal in Python 3.12; use find_spec() instead",
                       DeprecationWarning)
        spec = cls.find_spec(fullname, path)
        return spec.loader if spec is not None else None

    @staticmethod
    def create_module(spec):
        """Create a built-in module"""
        if spec.name not in sys.builtin_module_names:
            raise ImportError('{!r} is not a built-in module'.format(spec.name),
                              name=spec.name)
        return _call_with_frames_removed(_imp.create_builtin, spec)

    @staticmethod
    def exec_module(module):
        """Exec a built-in module"""
        _call_with_frames_removed(_imp.exec_builtin, module)

    @classmethod
    @_requires_builtin
    def get_code(cls, fullname):
        """Return None as built-in modules do not have code objects."""
        return None

    @classmethod
    @_requires_builtin
    def get_source(cls, fullname):
        """Return None as built-in modules do not have source code."""
        return None

    @classmethod
    @_requires_builtin
    def is_package(cls, fullname):
        """Return False as built-in modules are never packages."""
        return False

    load_module = classmethod(_load_module_shim)



def _exec(spec, module):
    """Execute the spec's specified module in an existing module's namespace."""
    name = spec.name
    with _ModuleLockManager(name):
        if sys.modules.get(name) is not module:
            msg = 'module {!r} not in sys.modules'.format(name)
            raise ImportError(msg, name=name)
        try:
            if spec.loader is None:
                if spec.submodule_search_locations is None:
                    raise ImportError('missing loader', name=spec.name)
                # Namespace package.
                _init_module_attrs(spec, module, override=True)
            else:
                _init_module_attrs(spec, module, override=True)
                if not hasattr(spec.loader, 'exec_module'):
                    msg = (f"{_object_name(spec.loader)}.exec_module() not found; "
                           "falling back to load_module()")
                    _warnings.warn(msg, ImportWarning)
                    spec.loader.load_module(name)
                else:
                    spec.loader.exec_module(module)
        finally:
            # Update the order of insertion into sys.modules for module
            # clean-up at shutdown.
            module = sys.modules.pop(spec.name)
            sys.modules[spec.name] = module
    return module

def _init_module_attrs(spec, module, *, override=False):
    # The passed-in module may be not support attribute assignment,
    # in which case we simply don't set the attributes.
    # __name__
    if (override or getattr(module, '__name__', None) is None):
        try:
            module.__name__ = spec.name
        except AttributeError:
            pass
    # __loader__
    if override or getattr(module, '__loader__', None) is None:
        loader = spec.loader
        if loader is None:
            # A backward compatibility hack.
            if spec.submodule_search_locations is not None:
                if _bootstrap_external is None:
                    raise NotImplementedError
                NamespaceLoader = _bootstrap_external.NamespaceLoader

                loader = NamespaceLoader.__new__(NamespaceLoader)
                loader._path = spec.submodule_search_locations
                spec.loader = loader
                # While the docs say that module.__file__ is not set for
                # built-in modules, and the code below will avoid setting it if
                # spec.has_location is false, this is incorrect for namespace
                # packages.  Namespace packages have no location, but their
                # __spec__.origin is None, and thus their module.__file__
                # should also be None for consistency.  While a bit of a hack,
                # this is the best place to ensure this consistency.
                #
                # See # https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module
                # and bpo-32305
                module.__file__ = None
        try:
            module.__loader__ = loader
        except AttributeError:
            pass
    # __package__
    if override or getattr(module, '__package__', None) is None:
        try:
            module.__package__ = spec.parent
        except AttributeError:
            pass
    # __spec__
    try:
        module.__spec__ = spec
    except AttributeError:
        pass
    # __path__
    if override or getattr(module, '__path__', None) is None:
        if spec.submodule_search_locations is not None:
            # XXX We should extend __path__ if it's already a list.
            try:
                module.__path__ = spec.submodule_search_locations
            except AttributeError:
                pass
    # __file__/__cached__
    if spec.has_location:
        if override or getattr(module, '__file__', None) is None:
            try:
                module.__file__ = spec.origin
            except AttributeError:
                pass

        if override or getattr(module, '__cached__', None) is None:
            if spec.cached is not None:
                try:
                    module.__cached__ = spec.cached
                except AttributeError:
                    pass
    return module



class _ModuleLockManager:

    def __init__(self, name):
        self._name = name
        self._lock = None

    def __enter__(self):
        self._lock = _get_module_lock(self._name)
        self._lock.acquire()

    def __exit__(self, *args, **kwargs):
        self._lock.release()

def _get_module_lock(name):
    """Get or create the module lock for a given module name.

    Acquire/release internally the global import lock to protect
    _module_locks."""

    _imp.acquire_lock()
    try:
        try:
            lock = _module_locks[name]()
        except KeyError:
            lock = None

        if lock is None:
            if _thread is None:
                lock = _DummyModuleLock(name)
            else:
                lock = _ModuleLock(name)

            def cb(ref, name=name):
                _imp.acquire_lock()
                try:
                    # bpo-31070: Check if another thread created a new lock
                    # after the previous lock was destroyed
                    # but before the weakref callback was called.
                    if _module_locks.get(name) is ref:
                        del _module_locks[name]
                finally:
                    _imp.release_lock()

            _module_locks[name] = _weakref.ref(lock, cb)
    finally:
        _imp.release_lock()

    return lock

def _requires_frozen(fxn):
    """Decorator to verify the named module is frozen."""
    def _requires_frozen_wrapper(self, fullname):
        if not _imp.is_frozen(fullname):
            raise ImportError('{!r} is not a frozen module'.format(fullname),
                              name=fullname)
        return fxn(self, fullname)
    _wrap(_requires_frozen_wrapper, fxn)
    return _requires_frozen_wrapper

class _ModuleLock:
    """A recursive lock implementation which is able to detect deadlocks
    (e.g. thread 1 trying to take locks A then B, and thread 2 trying to
    take locks B then A).
    """

    def __init__(self, name):
        self.lock = _thread.allocate_lock()
        self.wakeup = _thread.allocate_lock()
        self.name = name
        self.owner = None
        self.count = 0
        self.waiters = 0

    def has_deadlock(self):
        # Deadlock avoidance for concurrent circular imports.
        me = _thread.get_ident()
        tid = self.owner
        seen = set()
        while True:
            lock = _blocking_on.get(tid)
            if lock is None:
                return False
            tid = lock.owner
            if tid == me:
                return True
            if tid in seen:
                # bpo 38091: the chain of tid's we encounter here
                # eventually leads to a fixpoint or a cycle, but
                # does not reach 'me'.  This means we would not
                # actually deadlock.  This can happen if other
                # threads are at the beginning of acquire() below.
                return False
            seen.add(tid)

    def acquire(self):
        """
        Acquire the module lock.  If a potential deadlock is detected,
        a _DeadlockError is raised.
        Otherwise, the lock is always acquired and True is returned.
        """
        tid = _thread.get_ident()
        _blocking_on[tid] = self
        try:
            while True:
                with self.lock:
                    if self.count == 0 or self.owner == tid:
                        self.owner = tid
                        self.count += 1
                        return True
                    if self.has_deadlock():
                        raise _DeadlockError('deadlock detected by %r' % self)
                    if self.wakeup.acquire(False):
                        self.waiters += 1
                # Wait for a release() call
                self.wakeup.acquire()
                self.wakeup.release()
        finally:
            del _blocking_on[tid]

    def release(self):
        tid = _thread.get_ident()
        with self.lock:
            if self.owner != tid:
                raise RuntimeError('cannot release un-acquired lock')
            assert self.count > 0
            self.count -= 1
            if self.count == 0:
                self.owner = None
                if self.waiters:
                    self.waiters -= 1
                    self.wakeup.release()

    def __repr__(self):
        return '_ModuleLock({!r}) at {}'.format(self.name, id(self))

class _DummyModuleLock:
    """A simple _ModuleLock equivalent for Python builds without
    multi-threading support."""

    def __init__(self, name):
        self.name = name
        self.count = 0

    def acquire(self):
        self.count += 1
        return True

    def release(self):
        if self.count == 0:
            raise RuntimeError('cannot release un-acquired lock')
        self.count -= 1

    def __repr__(self):
        return '_DummyModuleLock({!r}) at {}'.format(self.name, id(self))

def _load(spec):
    """Return a new module object, loaded by the spec's loader.

    The module is not added to its parent.

    If a module is already in sys.modules, that existing module gets
    clobbered.

    """
    with _ModuleLockManager(spec.name):
        return _load_unlocked(spec)

def _load_unlocked(spec):
    # A helper for direct use by the import system.
    if spec.loader is not None:
        # Not a namespace package.
        if not hasattr(spec.loader, 'exec_module'):
            msg = (f"{_object_name(spec.loader)}.exec_module() not found; "
                    "falling back to load_module()")
            _warnings.warn(msg, ImportWarning)
            return _load_backward_compatible(spec)

def _load_backward_compatible(spec):
    # It is assumed that all callers have been warned about using load_module()
    # appropriately before calling this function.
    try:
        spec.loader.load_module(spec.name)
    except:
        if spec.name in sys.modules:
            module = sys.modules.pop(spec.name)
            sys.modules[spec.name] = module
        raise
    # The module must be in sys.modules at this point!
    # Move it to the end of sys.modules.
    module = sys.modules.pop(spec.name)
    sys.modules[spec.name] = module
    if getattr(module, '__loader__', None) is None:
        try:
            module.__loader__ = spec.loader
        except AttributeError:
            pass
    if getattr(module, '__package__', None) is None:
        try:
            # Since module.__path__ may not line up with
            # spec.submodule_search_paths, we can't necessarily rely
            # on spec.parent here.
            module.__package__ = module.__name__
            if not hasattr(module, '__path__'):
                module.__package__ = spec.name.rpartition('.')[0]
        except AttributeError:
            pass
    if getattr(module, '__spec__', None) is None:
        try:
            module.__spec__ = spec
        except AttributeError:
            pass
    return module

def _load_module_shim(self, fullname):
    """Load the specified module into sys.modules and return it.

    This method is deprecated.  Use loader.exec_module() instead.

    """
    msg = ("the load_module() method is deprecated and slated for removal in "
          "Python 3.12; use exec_module() instead")
    _warnings.warn(msg, DeprecationWarning)
    spec = spec_from_loader(fullname, self)
    if fullname in sys.modules:
        module = sys.modules[fullname]
        _exec(spec, module)
        return sys.modules[fullname]
    else:
        return _load(spec)

def _builtin_from_name(name):
    spec = BuiltinImporter.find_spec(name)
    if spec is None:
        raise ImportError('no built-in module named ' + name)
    return _load_unlocked(spec)

def _spec_from_module(module, loader=None, origin=None):
    # This function is meant for use in _setup().
    try:
        spec = module.__spec__
    except AttributeError:
        pass
    else:
        if spec is not None:
            return spec

class FrozenImporter:

    """Meta path import for frozen modules.

    All methods are either class or static methods to avoid the need to
    instantiate the class.

    """

    _ORIGIN = "frozen"

    @staticmethod
    def module_repr(m):
        """Return repr for the module.

        The method is deprecated.  The import machinery does the job itself.

        """
        _warnings.warn("FrozenImporter.module_repr() is deprecated and "
                       "slated for removal in Python 3.12", DeprecationWarning)
        return '<module {!r} ({})>'.format(m.__name__, FrozenImporter._ORIGIN)

    @classmethod
    def _fix_up_module(cls, module):
        spec = module.__spec__
        state = spec.loader_state
        if state is None:
            # The module is missing FrozenImporter-specific values.

            # Fix up the spec attrs.
            origname = vars(module).pop('__origname__', None)
            assert origname, 'see PyImport_ImportFrozenModuleObject()'
            ispkg = hasattr(module, '__path__')
            assert _imp.is_frozen_package(module.__name__) == ispkg, ispkg
            filename, pkgdir = cls._resolve_filename(origname, spec.name, ispkg)
            spec.loader_state = type(sys.implementation)(
                filename=filename,
                origname=origname,
            )
            __path__ = spec.submodule_search_locations
            if ispkg:
                assert __path__ == [], __path__
                if pkgdir:
                    spec.submodule_search_locations.insert(0, pkgdir)
            else:
                assert __path__ is None, __path__

            # Fix up the module attrs (the bare minimum).
            assert not hasattr(module, '__file__'), module.__file__
            if filename:
                try:
                    module.__file__ = filename
                except AttributeError:
                    pass
            if ispkg:
                if module.__path__ != __path__:
                    assert module.__path__ == [], module.__path__
                    module.__path__.extend(__path__)
        else:
            # These checks ensure that _fix_up_module() is only called
            # in the right places.
            __path__ = spec.submodule_search_locations
            ispkg = __path__ is not None
            # Check the loader state.
            assert sorted(vars(state)) == ['filename', 'origname'], state
            if state.origname:
                # The only frozen modules with "origname" set are stdlib modules.
                (__file__, pkgdir,
                 ) = cls._resolve_filename(state.origname, spec.name, ispkg)
                assert state.filename == __file__, (state.filename, __file__)
                if pkgdir:
                    assert __path__ == [pkgdir], (__path__, pkgdir)
                else:
                    assert __path__ == ([] if ispkg else None), __path__
            else:
                __file__ = None
                assert state.filename is None, state.filename
                assert __path__ == ([] if ispkg else None), __path__
            # Check the file attrs.
            if __file__:
                assert hasattr(module, '__file__')
                assert module.__file__ == __file__, (module.__file__, __file__)
            else:
                assert not hasattr(module, '__file__'), module.__file__
            if ispkg:
                assert hasattr(module, '__path__')
                assert module.__path__ == __path__, (module.__path__, __path__)
            else:
                assert not hasattr(module, '__path__'), module.__path__
        assert not spec.has_location

    @classmethod
    def _resolve_filename(cls, fullname, alias=None, ispkg=False):
        if not fullname or not getattr(sys, '_stdlib_dir', None):
            return None, None
        try:
            sep = cls._SEP
        except AttributeError:
            sep = cls._SEP = '\\' if sys.platform == 'win32' else '/'

        if fullname != alias:
            if fullname.startswith('<'):
                fullname = fullname[1:]
                if not ispkg:
                    fullname = f'{fullname}.__init__'
            else:
                ispkg = False
        relfile = fullname.replace('.', sep)
        if ispkg:
            pkgdir = f'{sys._stdlib_dir}{sep}{relfile}'
            filename = f'{pkgdir}{sep}__init__.py'
        else:
            pkgdir = None
            filename = f'{sys._stdlib_dir}{sep}{relfile}.py'
        return filename, pkgdir

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        info = _call_with_frames_removed(_imp.find_frozen, fullname)
        if info is None:
            return None
        # We get the marshaled data in exec_module() (the loader
        # part of the importer), instead of here (the finder part).
        # The loader is the usual place to get the data that will
        # be loaded into the module.  (For example, see _LoaderBasics
        # in _bootstra_external.py.)  Most importantly, this importer
        # is simpler if we wait to get the data.
        # However, getting as much data in the finder as possible
        # to later load the module is okay, and sometimes important.
        # (That's why ModuleSpec.loader_state exists.)  This is
        # especially true if it avoids throwing away expensive data
        # the loader would otherwise duplicate later and can be done
        # efficiently.  In this case it isn't worth it.
        _, ispkg, origname = info
        spec = spec_from_loader(fullname, cls,
                                origin=cls._ORIGIN,
                                is_package=ispkg)
        filename, pkgdir = cls._resolve_filename(origname, fullname, ispkg)
        spec.loader_state = type(sys.implementation)(
            filename=filename,
            origname=origname,
        )
        if pkgdir:
            spec.submodule_search_locations.insert(0, pkgdir)
        return spec

    @classmethod
    def find_module(cls, fullname, path=None):
        """Find a frozen module.

        This method is deprecated.  Use find_spec() instead.

        """
        _warnings.warn("FrozenImporter.find_module() is deprecated and "
                       "slated for removal in Python 3.12; use find_spec() instead",
                       DeprecationWarning)
        return cls if _imp.is_frozen(fullname) else None

    @staticmethod
    def create_module(spec):
        """Set __file__, if able."""
        module = type(sys)(spec.name)
        try:
            filename = spec.loader_state.filename
        except AttributeError:
            pass
        else:
            if filename:
                module.__file__ = filename
        return module

    @staticmethod
    def exec_module(module):
        spec = module.__spec__
        name = spec.name
        code = _call_with_frames_removed(_imp.get_frozen_object, name)
        exec(code, module.__dict__)

    @classmethod
    def load_module(cls, fullname):
        """Load a frozen module.

        This method is deprecated.  Use exec_module() instead.

        """
        # Warning about deprecation implemented in _load_module_shim().
        module = _load_module_shim(cls, fullname)
        info = _imp.find_frozen(fullname)
        assert info is not None
        _, ispkg, origname = info
        module.__origname__ = origname
        vars(module).pop('__file__', None)
        if ispkg:
            module.__path__ = []
        cls._fix_up_module(module)
        return module

    @classmethod
    @_requires_frozen
    def get_code(cls, fullname):
        """Return the code object for the frozen module."""
        return _imp.get_frozen_object(fullname)

    @classmethod
    @_requires_frozen
    def get_source(cls, fullname):
        """Return None as frozen modules do not have source code."""
        return None

    @classmethod
    @_requires_frozen
    def is_package(cls, fullname):
        """Return True if the frozen module is a package."""
        return _imp.is_frozen_package(fullname)