#!/bin/sh
#echo "Saludos"
for archivo in $( ls *_minus.log ); do                                                                                                                                            #organizar ligandos por carpetas que inicien con Lig y que los grids esten en una carpeta con el nombre del PDB
	#echo $archivo
	python fukuiPorLote.py $archivo
done