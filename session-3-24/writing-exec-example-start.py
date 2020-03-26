import sys

example_date = print("the second argument in command line is "+sys.argv[1])

vec_file = open('vectorq.exec','w')
vec_file.write("#!/bin/csh\n\n")
vec_file.write("set dir = ./test/\n")
vec_file.write("set fileinfo = {$dir}info_pr.dat\n")
vec_file.write("set filedh =  {$dir}dh_" + example_date + ".gr\n")
vec_file.write("set filest =  {$dir}density" + example_date + ".gr\n")
vec_file.write("set filestm = {$dir}ss1_st0.dat\n")
vec_file.write("set filequ =  {$dir}ss1a2qu.gr\n")
vec_file.write("set fileqv =  {$dir}ss1a2qv.gr\n")
vec_file.write("set fileqdi = {$dir}ss1a2qdi.gr\n")
vec_file.write("./vectorq.exe << !\n")
vec_file.write("'$fileinfo'	#>>>>>Escribe info file info.dat:\n")
vec_file.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:\n")
vec_file.write("'$filest'	#>>>>>Escribe fichero de densidad:\n")
vec_file.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:\n")
vec_file.write("'$filequ'	#>>>>>Escribe fichero Qu:\n")
vec_file.write("'$fileqv'	#>>>>>Escribe fichero Qv:\n")
vec_file.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:\n")

vec_file.close()

omega_file = open('omegainv.exec','w')

omega_file.write("#!/bin/csh\n")
omega_file.write("set dir = ./test/\n")
omega_file.write("set fileinfo = {$dir}info_pr.dat\n")
omega_file.write("set filestm = {$dir}ss1_st0.dat\n")
omega_file.write("set fileqdi = {$dir}ss1a2qdi.gr\n")
omega_file.write("set filew =   {$dir}ss1a2ww.gr\n")

omega_file.write("./omegainv.exe << !\n")
omega_file.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:\n")
omega_file.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:\n")
omega_file.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:\n")
omega_file.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):\n")
omega_file.write("'$filew'	#>>>>>Escribe fichero Salida W:\n")
omega_file.write("!\n")

omega_file.close()

