---
title: Notes on Programming Things
author: Nafid Enan
---

C
-

- Zero/empty initializer: "Type name = { 0 };"
- Designated initializer: "type_s name = { .field_name = value };"

CXX
---

- Dynamic cast works only with polymorphic base.
- 'free'ing 'new Object', instead of 'delete'ing will result in the destructor
  not being called.
- Defining a member function inside class definition makes it inline.
- Deleted function: `int func( int ) = delete;`
- 'new' calls constructor, 'malloc' doesnt
- 'delete' calls destructor, 'free' doesnt
- '#ifndef #define #endif': include guard
- _REENTRANT flag causes compiler to use thread-safe (i.e., re-entrant)
  versions of severals functions in the C library
- "-lpthread -D _REENTRANT" is the same as "-pthread"
- "std::optional<T>" exists
- "-Wl," sends options to linker from gcc/g++
- List of functions in .a: "nm -g -C x.a"
- "#define"s in .cpp can clash, so do #undef at the end of .cpp
- Should "#define" 1st-party headers before std headers

Python
------

- pandas has a 'to_latex' for tables/dataframes
- "=" copies references, not only the value (BEWARE)
- mylist.copy() copies only the first level of list, so doesn't work for 2d lists
- "export CUDA_VISIBLE_DEVICES=3"
- Install pip: `python -m ensurepip`
- If "pip install gym[box2d]" errors for swig: try "pip install swig"
- List comprehensions ([x for x in range(10)]) are more efficient
- PEP: python enhancement proposals
- "dunder" is "double under": __init__
- list1.extend(list2)
- dict1.update(dict2)
- {sys.executable} is the path to python executable
- $NO_COLOR disable colored outputs
- 'inspect' module: class 'getmember()', method 'signature()'
- pip.conf in venv/pip.conf (linux) or venv/pip.ini (windows)
- 'df.resample("1min")'

Rust
----

- CXX's 'erase()' with iterator is Rust's 'retain()'.
- r#"he said,"Escape quotes in raw strings""#


FFI
---

- ABI: Application Binary Interface
  - Defines the func signature and types
  - Much like an API but for linkers


Comp Arch
---------

- ISA architectures
  - Stack
  - Accumulator
  - Register-Memory (ours, probly)
    - arithmetic instructions can use regs/mems
  - Load-Store
    - arithmetic instructions can only use regs
    - cant do 'add x1, x2, x3'
    - cant do 'add x1, x2, 40(x3)'
    - -ve more instructions
    - +ve fast implementation
    - risc-v is load-store
- 5 stage pipeline
  - IF
    - Fetch instruction from memory
    - PC += 4
  - ID
    - decode instr
    - read source regs (rs1, rs2)
  - Ex
    - ALU computation
    - addr computation for load/store
    - compare regs & compute branching targets
  - Mem
    - mem access to/from data cache
    - load reads; store writes
  - WB
    - branching, store --> NOP
- FORWARDING path to avoid data hazard (RAW)
- data depency != data hazard


RISC-V
------

- ISA: Instruction Set Architecture
- Total registers: 32
- Instructions length: 32 bits
- Base ISA fixed
- Extensions possible
- Available extensions
  - I: integer
  - M: multiply, division
  - F: floating-point
  - C: compressed (<32bit instructions)
  - V: vector
- Instructions formats: R, I, S, B, U, J


gdb
---

- C-x s: single key mode
- follow-fork-mode
- detach-on-fork

MISC
----

- prefix sum: output[i] = input[0] + input[1] + ... + input[i]
- GNU make escape '$' with a '$', not a backslash
- GNU make runs each command in a subshell
- GNU make can do "export VAR=value"
- GNU make "command too long": redirect params into a file and then read params
  from file when running the command

