_.PHONY: clean map

# Default values
INPUT_FILE ?= prefix_adder.v
LOGIC_STYLE ?= nor_or
PYTHON ?= python3

# Generic map target - modifies simpler_conf.cfg and runs simpler_main.py
map:
	sed -i '' 's/^input_path=.*/input_path=$(INPUT_FILE)/' simpler_conf.cfg
	sed -i '' 's/^logic_style=.*/logic_style=$(LOGIC_STYLE)/' simpler_conf.cfg
	$(PYTHON) simpler_main.py

# Convenience targets for common designs
map_prefix_adder_nor: INPUT_FILE := prefix_adder.v
map_prefix_adder_nor: LOGIC_STYLE := nor
map_prefix_adder_nor: map

map_prefix_adder_or: INPUT_FILE := prefix_adder.v
map_prefix_adder_or: LOGIC_STYLE := or
map_prefix_adder_or: map

map_prefix_adder_nor_or: INPUT_FILE := prefix_adder.v
map_prefix_adder_nor_or: LOGIC_STYLE := nor_or
map_prefix_adder_nor_or: map

map_four_bit_or_nor: INPUT_FILE := four_bit_or.v
map_four_bit_or_nor: LOGIC_STYLE := nor
map_four_bit_or_nor: map

map_four_bit_or_or: INPUT_FILE := four_bit_or.v
map_four_bit_or_or: LOGIC_STYLE := or
map_four_bit_or_or: map

map_four_bit_or_nor_or: INPUT_FILE := four_bit_or.v
map_four_bit_or_nor_or: LOGIC_STYLE := nor_or
map_four_bit_or_nor_or: map

map_full_adder_nor: INPUT_FILE := full_adder_1bit.v
map_full_adder_nor: LOGIC_STYLE := nor
map_full_adder_nor: map

map_full_adder_or: INPUT_FILE := full_adder_1bit.v
map_full_adder_or: LOGIC_STYLE := or
map_full_adder_or: map

map_full_adder_nor_or: INPUT_FILE := full_adder_1bit.v
map_full_adder_nor_or: LOGIC_STYLE := nor_or
map_full_adder_nor_or: map

clean:
	rm -rf *.pyc __pycache__ *_output* *.dot *.json