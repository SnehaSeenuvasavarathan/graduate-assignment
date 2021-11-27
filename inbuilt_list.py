# Python keywords and builtins
import builtins
import types
import keyword


python_list=['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError',
'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
 'PermissionError', 'ProcessLookupError', 'RecursionError',
'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError',
'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
'ValueError', 'Warning', 'ZeroDivisionError', '__IPYTHON__', '__build_class__', '__debug__', '__doc__', '__import__',
'__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes',
'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'display', 'divmod',
'enumerate', 'eval', 'exec', 'filter', 'float', 'format', 'frozenset', 'get_ipython', 'getattr', 'globals', 'hasattr',
'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals',
'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr',
 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
  'vars', 'zip', '__build_class__', '__import__', 'abs', 'all', 'any', 'ascii', 'bin', 'breakpoint', 'callable', 'chr',
  'compile', 'delattr', 'dir', 'divmod', 'eval', 'exec', 'format', 'getattr', 'globals', 'hasattr', 'hash', 'hex', 'id',
  'isinstance', 'issubclass', 'iter', 'len', 'locals', 'max', 'min', 'next', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'setattr', 'sorted',
'sum', 'vars', 'open', 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', "format","split","join","strip","upper",
 "lower","replace","find","encode","count","startswith","endsWith","index","contains","isalpha","isalnum","isdigit","islower"
 ,"isupper","isspace","ljust","rjust","swapcase","partition","len","ascii","bool","print","slice","ascii","append","clear","copy","extend",
 "insert","remove","reverse","sort"]
# Javascript keywords and builtins
js_key=['abstract', 'arguments','await','boolean',
'break', 'byte', 'case', 'catch',
'char', 'class', 'const', 'continue',
'debugger', 'default', 'delete', 'do',
'double','else', 'enum','eval',
'export', 'extends', 'false', 'final',
'finally', 'float', 'for', 'function',
'goto', 'if', 'implements', 'import',
'in', 'instanceof', 'int', 'interface',
'let', 'long', 'native', 'new',
'null', 'package','private', 'protected',
'public', 'return', 'short', 'static',
'super', 'switch','synchronized','this',
'throw', 'throws','transient','true',
'try','typeof','var','void',
'volatile', 'while', 'with','yield',
'abstract', 'boolean', 'byte', 'char', 'double', 'final', 'float', 'goto',
'int','long', 'native', 'short', 'synchronized', 'throws', 'transient', 'volatile',
'Array','Date', 'eval', 'function',
'hasOwnProperty','Infinity', 'isFinite', 'isNaN',
'isPrototypeOf','length', 'Math', 'NaN',
'name','Number', 'Object', 'prototype','expect',
'String', 'toString','undefined', 'valueOf', 'NaN', 'global','require']
html_elements=['alert', 'all', 'anchor', 'anchors', 'area', 'assign', 'blur','button',
'checkbox','clearInterval','clearTimeout','clientInformation','close',
'closed','confirm', 'constructor', 'crypto', 'decodeURI','decodeURIComponent',
'defaultStatus','document','element','elements','embed','embeds','encodeURI','encodeURIComponent','escape','event',
'fileUpload','focus','form','forms','frame','innerHeight','innerWidth','layer','layers','link',
'location','mimeTypes','navigate','navigator','frames','frameRate','hidden','history',
'image','images','offscreenBuffering','open','opener','option','outerHeight',
'outerWidth','packages','pageXOffset','pageYOffset','parent','parseFloat',
'parseInt','password','pkcs11','plugin','prompt','propertyIsEnum','radio','reset',
'screenX','screenY','scroll','secure','select','self','setInterval','setTimeout',
'status','submit','taint','text','textarea','top','unescape','untaint','window',
'onblur','onclick','onerror','onfocus',
'onkeydown', 'onkeypress','onkeyup','onmouseover',
'onload','onmouseup','onmousedown','onsubmit']
function_properties=['eval','parseInt','parseFloat','isNaN','isFinite','decodeURI',
'decodeURIComponent','encodeURI','encodeURIComponent',
'escape','unescape']
string_functions=[ 'length',   'constructor',   'anchor',   'big',   'blink',   'bold',   'charAt',   'charCodeAt',
                  'codePointAt',   'concat',   'endsWith',   'fontcolor',   'fontsize',   'fixed',   'includes',
                  'indexOf',   'italics',   'lastIndexOf',   'link',   'localeCompare',   'match',   'normalize',
                  'padEnd',   'padStart',   'repeat',   'replace',   'search',   'slice',   'small',   'split',
                  'strike',   'sub',   'substr',   'substring',   'sup',   'startsWith',   'toString',   'trim',
                  'trimLeft',   'trimRight',   'toLowerCase',   'toUpperCase',   'valueOf',   'toLocaleLowerCase',
                  'toLocaleUpperCase',   'trimStart',   'trimEnd', 'map','filter','reduce','some','every','includes','slice',
                  'splice', 'shift','unshift','fill','console','log','alert']
math_functions=[ 'abs',   'acos',   'acosh',   'asin',   'asinh',   'atan',   'atanh',   'atan2',
                'ceil',   'cbrt',   'expm1',   'clz32',   'cos',   'cosh',   'exp',   'floor',   'fround',
                'hypot',   'imul',   'log',   'log1p',   'log2',   'log10',   'max',   'min',   'pow',   'random',
                'round',   'sign',   'sin',   'sinh',   'sqrt',   'tan',   'tanh',   'trunc',   'E',   'LN10',
                'LN2',   'LOG10E',   'LOG2E',   'PI',   'SQRT1_2',   'SQRT2' ]
number_functions=[ 'constructor',
  'toExponential',
  'toFixed',
  'toPrecision',
  'toString',
  'valueOf',
  'toLocaleString' ]
date_functions=[ 'constructor',   'toString',   'toDateString',   'toTimeString',   'toISOString',   'toUTCString',
                'toGMTString',   'getDate',   'setDate',   'getDay',   'getFullYear',   'setFullYear',   'getHours',
                'setHours',   'getMilliseconds',   'setMilliseconds',   'getMinutes',   'setMinutes',   'getMonth',
                'setMonth',   'getSeconds',   'setSeconds',   'getTime',   'setTime',   'getTimezoneOffset',
                'getUTCDate',   'setUTCDate',   'getUTCDay',   'getUTCFullYear',   'setUTCFullYear',   'getUTCHours',
                'setUTCHours',   'getUTCMilliseconds',   'setUTCMilliseconds',   'getUTCMinutes',   'setUTCMinutes',
                'getUTCMonth',   'setUTCMonth',   'getUTCSeconds',   'setUTCSeconds',   'valueOf',   'getYear',
                'setYear',   'toJSON',   'toLocaleString',   'toLocaleDateString',   'toLocaleTimeString' ]
error_functions=[ 'constructor', 'name', 'message', 'toString' ]
array_functions=[ 'length',   'constructor',   'concat',   'find',
'findIndex',   'pop',   'push',   'shift',   'unshift',   'slice',   'splice',   'includes',   'indexOf',
'keys',   'entries',   'forEach',   'filter',   'map',   'every',
  'some',   'reduce',   'reduceRight',   'toString',   'toLocaleString',   'join',
  'reverse',   'sort',   'lastIndexOf',   'copyWithin',   'fill',   'values' ]
js_list=js_key+html_elements+function_properties+string_functions+math_functions+number_functions+date_functions+error_functions+array_functions
javascript_list=list(set(js_list))

# Ruby keywords and builtins
ruby_keywords=['__ENCODING__','__LINE__' ,'__FILE__','BEGIN','END'
,'alias','and' ,'begin','break','case','class','def','defined?','do','else','elsif','end','ensure','false','for','if','in','module',
               'next','nil' ,'not', 'or', 'redo'
,'rescue','retry','return','self' ,'super' ,'then','true','undef','unless','until','when','while' ,'yield']
ruby_inbuilt_functions=['Array','Float','Integer','String','at_exit','autoload','binding','caller','catch','chop','chop!','chomp',
                        'chomp!','eval','exec','exit','exit!','fail','fork','format','gets','global_variables','gsub','gsub!',
                        'iterator?','lambda','load','local_variables','loop','open','p','print','printf','proc','putc','puts','raise',
                        'rand','readline','readlines','require','select','sleep','split','sprintf','srand','sub','sub!','syscall','system',
                        'test','trace_var','trap','untrace_var']
ruby_list=ruby_keywords+ruby_inbuilt_functions

# Go keywords and builtins
go_keywords=[
    'break', 'default', 'func', 'interface', 'select', 'case', 'defer', 'go', 'map', 'struct', 'chan',
    'else', 'goto', 'package', 'switch', 'const', 'fallthrough', 'if', 'range', 'type', 'continue', 'for',
    'import', 'return', 'var', 'int','float',"string","error","byte","bool"]

go_built_in=["append", "cap", "close", "complex","copy", "delete", "imag", "len", "make", "new","panic",
             "print","println","real", "recover"]
go_list=go_keywords+go_built_in
