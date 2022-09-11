from os import system
from traceback import print_tb
vhdl_file = 'mult_by_constant'
vhdl_file_tb = 'file_tb'
line_vhdl = vhdl_file+'.vhd ' + vhdl_file_tb+'.vhd'

system("ghdl -a --std=08 "+line_vhdl)
system("ghdl -s --std=08 "+line_vhdl)
system("ghdl -e --std=08 "+vhdl_file_tb)
system("ghdl -r "+vhdl_file_tb+" --vcd="+ vhdl_file_tb+".vcd --stop-time=4000ns")
#system("open /Applications/gtkwave.app "+ vhdl_file_tb+".vcd")

#open /Applications/gtkwave.app file_tb.vcd

