# -*- coding: utf-8 -*-


import inspect
from pprint import pprint

from brainpy import errors

__all__ = [
  'get_args',
  'check_kws',
  'compile_code',
]


def check_kws(parameters, keywords):
  for key, meaning in keywords.items():
    if key in parameters:
      raise errors.CodeError(f'"{key}" is a keyword for '
                             f'numerical solvers in BrainPy, denoting '
                             f'"{meaning}". Please change another name.')


def get_args(f):
  """Get the function arguments.

  >>> def f1(a, b, t, *args, c=1): pass
  >>> get_args(f1)
  (['a', 'b'], ['t', '*args', 'c'], ['a', 'b', 't', '*args', 'c=1'])

  >>> def f2(a, b, *args, c=1, **kwargs): pass
  >>> get_args(f2)
  ValueError: Do not support dict of keyword arguments: **kwargs

  >>> def f3(a, b, t, c=1, d=2): pass
  >>> get_args(f4)
  (['a', 'b'], ['t', 'c', 'd'], ['a', 'b', 't', 'c=1', 'd=2'])

  >>> def f4(a, b, t, *args): pass
  >>> get_args(f4)
  (['a', 'b'], ['t', '*args'], ['a', 'b', 't', '*args'])

  >>> scope = {}
  >>> exec(compile('def f5(a, b, t, *args): pass', '', 'exec'), scope)
  >>> get_args(scope['f5'])
  (['a', 'b'], ['t', '*args'], ['a', 'b', 't', '*args'])

  Parameters
  ----------
  f : callable
      The function.

  Returns
  -------
  args : tuple
      The variable names, the other arguments, and the original args.
  """

  # get the function arguments
  reduced_args = []
  args = []

  for name, par in inspect.signature(f).parameters.items():
    if par.kind is inspect.Parameter.POSITIONAL_OR_KEYWORD:
      reduced_args.append(par.name)

    elif par.kind is inspect.Parameter.VAR_POSITIONAL:
      reduced_args.append(f'*{par.name}')

    elif par.kind is inspect.Parameter.KEYWORD_ONLY:
      raise errors.DiffEqError(f'In BrainPy, numerical integrators do not support KEYWORD_ONLY '
                               f'parameters, e.g., * (error in {f}).')
    elif par.kind is inspect.Parameter.POSITIONAL_ONLY:
      raise errors.DiffEqError(f'In BrainPy, numerical integrators do not support POSITIONAL_ONLY '
                               f'parameters, e.g., / (error in {f}).')
    elif par.kind is inspect.Parameter.VAR_KEYWORD:  # TODO
      raise errors.DiffEqError(f'In BrainPy, numerical integrators do not support VAR_KEYWORD '
                               f'arguments: {str(par)} (error in {f}).')
    else:
      raise errors.DiffEqError(f'Unknown argument type: {par.kind} (error in {f}).')

    args.append(str(par))

  #  variable names
  vars = []
  for a in reduced_args:
    if a == 't':
      break
    vars.append(a)
  else:
    raise ValueError('Do not find time variable "t".')
  pars = reduced_args[len(vars):]
  return vars, pars, args


def compile_code(code_lines, code_scope, func_name, show_code=False):
  code = '\n'.join(code_lines)
  if show_code:
    print(code)
    print()
    pprint(code_scope)
    print()
  exec(compile(code, '', 'exec'), code_scope)
  new_f = code_scope[func_name]
  return new_f
