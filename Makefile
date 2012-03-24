#! /bin/make
default: asm.bf

asm.masm: src/program-reader.masm tools/jump_fixer.py
	python tools/jump_fixer.py < src/program-reader.masm > asm.masm

asm.bf: asm.masm
	make -C ../micro-assembler/ ../assembler/asm.bf