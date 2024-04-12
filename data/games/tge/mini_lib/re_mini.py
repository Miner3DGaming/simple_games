
# SRE_FLAG_TEMPLATE = 1 # template mode (unknown purpose, deprecated)
# SRE_FLAG_IGNORECASE = 2 # case insensitive
# SRE_FLAG_LOCALE = 4 # honour system locale
# SRE_FLAG_MULTILINE = 8 # treat target as multiline string
# SRE_FLAG_DOTALL = 16 # treat target as a single string
# SRE_FLAG_UNICODE = 32 # use unicode "locale"
# SRE_FLAG_VERBOSE = 64 # ignore whitespace and comments
# SRE_FLAG_DEBUG = 128 # debugging
# SRE_FLAG_ASCII = 256 # use ascii "locale"

# # flags for INFO primitive
# SRE_INFO_PREFIX = 1 # has prefix
# SRE_INFO_LITERAL = 2 # entire pattern is literal (given by prefix)
# SRE_INFO_CHARSET = 4 # pattern starts with character from given set


# _cache = {}  # ordered!
# _MAXCACHE = 512


# class RegexFlag:
#     NOFLAG = 0
#     ASCII = A = SRE_FLAG_ASCII # assume ascii "locale"
#     IGNORECASE = I = SRE_FLAG_IGNORECASE # ignore case
#     LOCALE = L = SRE_FLAG_LOCALE # assume current 8-bit locale
#     UNICODE = U = SRE_FLAG_UNICODE # assume unicode "locale"
#     MULTILINE = M = SRE_FLAG_MULTILINE # make anchors look for newline
#     DOTALL = S = SRE_FLAG_DOTALL # make dot match newline
#     VERBOSE = X = SRE_FLAG_VERBOSE # ignore whitespace and comments
#     # sre extensions (experimental, don't rely on these)
#     TEMPLATE = T = SRE_FLAG_TEMPLATE # unknown purpose, deprecated
#     DEBUG = SRE_FLAG_DEBUG # dump pattern after compilation
#     __str__ = object.__str__
#     _numeric_repr_ = hex

# def dis(code):
#     import sys

#     labels = set()
#     level = 0
#     offset_width = len(str(len(code) - 1))

#     def dis_(start, end):
#         def print_(*args, to=None):
#             if to is not None:
#                 labels.add(to)
#                 args += ('(to %d)' % (to,),)
#             print('%*d%s ' % (offset_width, start, ':' if start in labels else '.'),
#                   end='  '*(level-1))
#             print(*args)

#         def print_2(*args):
#             print(end=' '*(offset_width + 2*level))
#             print(*args)

#         nonlocal level
#         level += 1
#         i = start
#         while i < end:
#             start = i
#             op = code[i]
#             i += 1
#             op = OPCODES[op]
#             if op in (SUCCESS, FAILURE, ANY, ANY_ALL,
#                       MAX_UNTIL, MIN_UNTIL, NEGATE):
#                 print_(op)
#             elif op in (LITERAL, NOT_LITERAL,
#                         LITERAL_IGNORE, NOT_LITERAL_IGNORE,
#                         LITERAL_UNI_IGNORE, NOT_LITERAL_UNI_IGNORE,
#                         LITERAL_LOC_IGNORE, NOT_LITERAL_LOC_IGNORE):
#                 arg = code[i]
#                 i += 1
#                 print_(op, '%#02x (%r)' % (arg, chr(arg)))
#             elif op is AT:
#                 arg = code[i]
#                 i += 1
#                 arg = str(ATCODES[arg])
#                 assert arg[:3] == 'AT_'
#                 print_(op, arg[3:])
#             elif op is CATEGORY:
#                 arg = code[i]
#                 i += 1
#                 arg = str(CHCODES[arg])
#                 assert arg[:9] == 'CATEGORY_'
#                 print_(op, arg[9:])
#             elif op in (IN, IN_IGNORE, IN_UNI_IGNORE, IN_LOC_IGNORE):
#                 skip = code[i]
#                 print_(op, skip, to=i+skip)
#                 dis_(i+1, i+skip)
#                 i += skip
#             elif op in (RANGE, RANGE_UNI_IGNORE):
#                 lo, hi = code[i: i+2]
#                 i += 2
#                 print_(op, '%#02x %#02x (%r-%r)' % (lo, hi, chr(lo), chr(hi)))
#             elif op is CHARSET:
#                 print_(op, _hex_code(code[i: i + 256//_CODEBITS]))
#                 i += 256//_CODEBITS
#             elif op is BIGCHARSET:
#                 arg = code[i]
#                 i += 1
#                 mapping = list(b''.join(x.to_bytes(_sre.CODESIZE, sys.byteorder)
#                                         for x in code[i: i + 256//_sre.CODESIZE]))
#                 print_(op, arg, mapping)
#                 i += 256//_sre.CODESIZE
#                 level += 1
#                 for j in range(arg):
#                     print_2(_hex_code(code[i: i + 256//_CODEBITS]))
#                     i += 256//_CODEBITS
#                 level -= 1
#             elif op in (MARK, GROUPREF, GROUPREF_IGNORE, GROUPREF_UNI_IGNORE,
#                         GROUPREF_LOC_IGNORE):
#                 arg = code[i]
#                 i += 1
#                 print_(op, arg)
#             elif op is JUMP:
#                 skip = code[i]
#                 print_(op, skip, to=i+skip)
#                 i += 1
#             elif op is BRANCH:
#                 skip = code[i]
#                 print_(op, skip, to=i+skip)
#                 while skip:
#                     dis_(i+1, i+skip)
#                     i += skip
#                     start = i
#                     skip = code[i]
#                     if skip:
#                         print_('branch', skip, to=i+skip)
#                     else:
#                         print_(FAILURE)
#                 i += 1
#             elif op in (REPEAT, REPEAT_ONE, MIN_REPEAT_ONE,
#                         POSSESSIVE_REPEAT, POSSESSIVE_REPEAT_ONE):
#                 skip, min, max = code[i: i+3]
#                 if max == MAXREPEAT:
#                     max = 'MAXREPEAT'
#                 print_(op, skip, min, max, to=i+skip)
#                 dis_(i+3, i+skip)
#                 i += skip
#             elif op is GROUPREF_EXISTS:
#                 arg, skip = code[i: i+2]
#                 print_(op, arg, skip, to=i+skip)
#                 i += 2
#             elif op in (ASSERT, ASSERT_NOT):
#                 skip, arg = code[i: i+2]
#                 print_(op, skip, arg, to=i+skip)
#                 dis_(i+2, i+skip)
#                 i += skip
#             elif op is ATOMIC_GROUP:
#                 skip = code[i]
#                 print_(op, skip, to=i+skip)
#                 dis_(i+1, i+skip)
#                 i += skip
#             elif op is INFO:
#                 skip, flags, min, max = code[i: i+4]
#                 if max == MAXREPEAT:
#                     max = 'MAXREPEAT'
#                 print_(op, skip, bin(flags), min, max, to=i+skip)
#                 start = i+4
#                 if flags & SRE_INFO_PREFIX:
#                     prefix_len, prefix_skip = code[i+4: i+6]
#                     print_2('  prefix_skip', prefix_skip)
#                     start = i + 6
#                     prefix = code[start: start+prefix_len]
#                     print_2('  prefix',
#                             '[%s]' % ', '.join('%#02x' % x for x in prefix),
#                             '(%r)' % ''.join(map(chr, prefix)))
#                     start += prefix_len
#                     print_2('  overlap', code[start: start+prefix_len])
#                     start += prefix_len
#                 if flags & SRE_INFO_CHARSET:
#                     level += 1
#                     print_2('in')
#                     dis_(start, i+skip)
#                     level -= 1
#                 i += skip
#             else:
#                 raise ValueError(op)

#         level -= 1

#     dis_(0, len(code))


# def c_compile(p, flags=0):
#     # internal: convert pattern list to internal format

#     if isstring(p):
#         pattern = p
#         p = _parser.parse(p, flags)
#     else:
#         pattern = None

#     code = _code(p, flags)

#     if flags & SRE_FLAG_DEBUG:
#         print()
#         dis(code)

#     # map in either direction
#     groupindex = p.state.groupdict
#     indexgroup = [None] * p.state.groups
#     for k, i in groupindex.items():
#         indexgroup[i] = k

#     return _sre.compile(
#         pattern, flags | p.state.flags, code,
#         p.state.groups-1,
#         groupindex, tuple(indexgroup)
#         )


# def isstring(obj):
#     return isinstance(obj, (str, bytes))

# Pattern = type(c_compile('', 0))

# def _compile(pattern, flags):
#     # internal: compile pattern
#     if isinstance(flags, RegexFlag):
#         flags = flags.value
#     try:
#         return _cache[type(pattern), pattern, flags]
#     except KeyError:
#         pass
#     if isinstance(pattern, Pattern):
#         if flags:
#             raise ValueError(
#                 "cannot process flags argument with a compiled pattern")
#         return pattern
#     if not isstring(pattern):
#         raise TypeError("first argument must be string or compiled pattern")
#     if flags & T:
#         import warnings
#         warnings.warn("The re.TEMPLATE/re.T flag is deprecated "
#                   "as it is an undocumented flag "
#                   "without an obvious purpose. "
#                   "Don't use it.",
#                   DeprecationWarning)
#     p = compile(pattern, flags)
#     if not (flags & DEBUG):
#         if len(_cache) >= _MAXCACHE:
#             # Drop the oldest item
#             try:
#                 del _cache[next(iter(_cache))]
#             except (StopIteration, RuntimeError, KeyError):
#                 pass
#         _cache[type(pattern), pattern, flags] = p
#     return p

# def compile(pattern, flags=0):
#     "Compile a regular expression pattern, returning a Pattern object."
#     return _compile(pattern, flags)

















