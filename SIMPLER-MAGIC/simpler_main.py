import configparser
import os
import tempfile
import SIMPLER_Mapping
import ast
import json

def main():

    # Read configuration parameters
    config = configparser.ConfigParser()
    # config.readfp(open('simpler_conf.cfg'))
    with open('simpler_conf.cfg', 'r') as f:
        config.read_file(f)
    input_path = config.get('input_output', 'input_path')
    input_format = config.get('input_output', 'input_format')
    abc_dir_path = config.get('abc', 'abc_dir_path')
    #BenchmarkStrings = ast.literal_eval(config.get("SIMPLER_Mapping", "BenchmarkStrings"))
    Max_num_gates = config.getint('SIMPLER_Mapping', 'Max_num_gates')
    ROW_SIZE = [int(i) for i in ast.literal_eval(config.get("SIMPLER_Mapping", "ROW_SIZE"))]
    generate_json = config.getboolean('SIMPLER_Mapping', 'generate_json')
    print_mapping = config.getboolean('SIMPLER_Mapping', 'print_mapping')
    print_warnings = config.getboolean('SIMPLER_Mapping', 'print_warnings')
    end_of_line_output = config.getboolean('SIMPLER_Mapping', 'end_of_line_output')
    logic_style = config.get('technology_mapping', 'logic_style', fallback='magic_nor')
    # Auto-generate output_path from input_path (remove extension) and include logic_style
    output_path = os.path.splitext(input_path)[0] + "_" + logic_style + "_output"
    
    #genlib by style
    GENLIB = {
        'nor': 'mcnc1_nor2.genlib',
        'or': 'mcnc1_or2.genlib',
        'nor_or': 'mcnc1_hybrid_nor2_or2.genlib'
    }

    if logic_style not in GENLIB:
        print(f"Error: Invalid logic style '{logic_style}' specified in configuration. Allowed values are: {', '.join(GENLIB.keys())}.")
        return
    
    genlib_path = GENLIB[logic_style]

    abc_exe_path = os.path.join(abc_dir_path, "abc")
    abc_rc_path = os.path.join(abc_dir_path, "abc.rc")

    # Create abc script
    abc_script = open('abc_script_template.abc', 'r').read()
    abc_script = abc_script.replace('abc_rc_path', abc_rc_path)
    abc_script = abc_script.replace('input.blif', input_path)
    if input_format == 'verilog':
        abc_script = abc_script.replace('read_blif', 'read_verilog')
    abc_script = abc_script.replace('lib.genlib', genlib_path)
    # abc_output_path = tempfile.mktemp()
    abc_output_path = output_path + "_abc_mapped.v"
    print("DEBUG: abc_output_path =", abc_output_path)
    abc_script = abc_script.replace('output.v', abc_output_path)

    # Run abc script
    fd, abc_script_path = tempfile.mkstemp()
    os.close(fd)
    open(abc_script_path, "w").write(abc_script)
    os.system('%s -f "%s"' % (abc_exe_path, abc_script_path))
    # Mapping into the memory array
    SIMPLER_Mapping.SIMPLER_Main([abc_output_path], Max_num_gates, ROW_SIZE, input_path.split(".")[0], generate_json, print_mapping, print_warnings, end_of_line_output)

    

    # Clean files
    os.remove(abc_script_path)
    # os.remove(abc_output_path)

if __name__ == "__main__":
    main()
