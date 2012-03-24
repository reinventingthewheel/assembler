# Assembler

This is the second step in abtraction from the brainfuck machine.

It's a assembly to micro-assembly compiler. Please see the
[micro-assembler](http://github.com/reinventingthewheel/micro-assembler)
projects for details in this lower level language.

## Specification

There are six registers for general use, and they can hold integers (or
chars), named:

    A, B, C, D, E, F

There is also a special register `IP` (instrucion pointer) which holds the
current instruction address in the program.

There is a special stack data structure for general use. It can be accessed by
the instructions `PUSH`, `POP` and `TOP`.

The instruction set is:

* `ADD <REG> [$]<V>` Adds to `<REG>` the value of `<V>`.
* `SUB <REG> [$]<V>` Substracts from `<REG>` the value of `<V>`.
* `MUL <REG> [$]<V>` Multiplies `<REG>` by the value of `<V>`.
* `DIV <REG> [$]<V>` Performs a integer division of `<REG>` by the value of `<V>`.
* `MOD <REG> [$]<V>` Performs a integer modulus of `<REG>` by the value of `<V>`.
* `ABS <REG>` Calculates the absolute value of `<REG>`.
* `SQR <REG>` Calculates the square root of `<REG>`.
* `MOV [$]<X> [$]<V>` Copies from `<V>` into `<X>`.
* `PUSH [$]<V>` Pushes to stack the value '<V>`.
* `POP <REG>` Pops from stack into `<REG>`.
* `TOP <REG>` Checks the last pushed value from stack into `<REG>`.
* `JMP [$]<V>` Jumps to instruction at the address in `<V>`.
* `GOTO <LABEL>` Goto label (Jump to label, where `<LABEL>` is a identifier
  followed by commas).
* `WRITE [$]<V>` Writes to output the value of `<V>`.
* `READ <REG>` Reads from input into `<REG>`.
* `EQ [$]<V> [$]<V>` Skips next instruction if arguments are equal.
* `NEQ [$]<V> [$]<V>` Skips next instruction if arguments are not equal.
* `GT [$]<V> [$]<V>` Skips next instruction if first argument is bigger than the second.
* `LT [$]<V> [$]<V>` Skips next instruction if first argument is less than the second.
* `GTE [$]<V> [$]<V>` Skips next instruction if first argument is greater or equal to the second.
* `LTE [$]<V> [$]<V>` Skips next instruction if first argument is less or equal to the second.
* `NOP` Does nothing (no operation).

Where `<REG>` is a register name (A, B, C, D, E or F). `<V>` is whether a
register or a integer (denoting a memory address). `<X>` is a register or a
integer, but, in the latter case, it's always interpreted as a memory address.

The optional `$` in some operands specifies the indirect addressing mode. It
denotes the value in the address pointed by the subsequent value - which can be
an integer or an register name (i.e. C/C++ style pointer `&`).

