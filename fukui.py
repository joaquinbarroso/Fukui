#Version 171026-0922

#Programa para calcular las funciones de Fukui
# entrada: python fukui.py archivoOriginal archivoMinus ArchivoPlus
# salida: archivoSalida-fecha-hora.csv

import sys #Para recibir archivos de entrada
import time #para importar la fecha


fukuiLog = open( "fukui.log" , "a"); #para llevar un seguimiento de la entrada se agrega la linea...
fukuiLog.write("\n" + time.strftime("%Y/%m/%d-%H:%M:%S") + " :  " + sys.argv[0] + "  " + sys.argv[1] + "  " + sys.argv[2] + "  " + sys.argv[3] + " =  " );

inicio = " Summary of Natural Population Analysis:                  "
fin = "                                 Natural Population      "

recolector = []; # Recolecta las lineas necesarias de los 3 archivos

bandera = 0;
renglones = 0;
#print ("Valores del archivo " + sys.argv[1]);
archOriginal = open(sys.argv[1], "r"); # archivoOriginal
linea = archOriginal.readline();
while linea:
    if( inicio in linea ): # si encuentra la linea este titulo
        bandera += 1; # la BANDERA aumenta en 1
    if( bandera == 2 ): # si encuentra el segundo titulo 
        renglones += 1;
        recolector.append(linea);
        #print (str(renglones) + ". " + linea); 
        if( fin in linea ): # cuando encuentre el fin del archivo
        	break;
    linea = archOriginal.readline();
archOriginal.close()

bandera = 0;
renglones = 0;
#print ("Valores del archivo " + sys.argv[2]);
archMinus = open(sys.argv[2], "r"); # archivoMinus
linea = archMinus.readline();
while linea:
    if( inicio in linea ): # Si encuentra la linea este titulo
        bandera = bandera + 1; # la BANDERA aumenta en 1

    if( bandera == 1 ): # Si encuentra el primer titulo 
        #print (linea); 
        recolector[renglones] = recolector[renglones] + linea;
        renglones = renglones + 1;
        if( fin in linea ): # cuando encuentre el fin del archivo
        	break;
    linea = archMinus.readline();
archMinus.close()


bandera = 0;
renglones = 0;
#print ("Valores del archivo " + sys.argv[3]);
archPlus = open(sys.argv[3], "r"); # ArchivoPlus
linea = archPlus.readline();
while linea:
    if( inicio in linea ): # Si encuentra la linea este titulo
        bandera = bandera + 1; # ... la BANDERA aumenta en 1

    if( bandera == 1 ): # Si encuentra el primer titulo
        #print (linea); 
        recolector[renglones] = recolector[renglones] + linea ;
        renglones = renglones + 1;
        	
        if( fin in linea ): # cuando encuentre el fin del archivo
        	break;
    linea = archPlus.readline();
archPlus.close()
#print ( str(renglones) + " renglones");

# Normalizar los datos
contador = 0;
renglonesSalida = 0;
salida = []; # Cadena para concatenar los renglones finales
for contador in range(renglones):
	if( contador > 4 and contador < (renglones - 2) and contador != 5 and contador != (renglones - 4) ):
		recolector[contador] = recolector[contador].replace("\n"," ");
		recolector[contador] = recolector[contador].replace("     "," ");
		recolector[contador] = recolector[contador].replace("    "," ");
		recolector[contador] = recolector[contador].replace("   "," ");
		recolector[contador] = recolector[contador].replace("  "," ");
		recolector[contador] = recolector[contador].replace("* Total *","Total ");
		recolector[contador] = recolector[contador].replace(" ",",");
		recolector[contador] = recolector[contador][1:]; # Omitir la primer coma
		salida.append(recolector[contador]);


# El mayor(1) de los f+
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice1 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[20]) - float(valor[6]);  # (f+) = fP - fo
    salida[contador] =  salida[contador]  + "," + valor[0] + "," + valor[1] + "," + str( comparador2 );
    if(comparador1 < comparador2):
        comparador1 = comparador2;
        indice1 = contador;
salida[indice1] = salida[indice1] + "(1)"; # (f+) = fP - fo

# El mayor(2) de los f+
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice2 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[20]) - float(valor[6]);  # (f+) = fP - fo
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1):
        comparador1 = comparador2;
        indice2 = contador;
salida[indice2] = salida[indice2] + "(2)"; # (f+) = fP - fo

# El mayor(3) de los f+
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice3 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[20]) - float(valor[6]);  # (f+) = fP - fo
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1 and contador != indice2):
        comparador1 = comparador2;
        indice3 = contador;
salida[indice3] = salida[indice3] + "(3)"; # (f+) = fP - fo

# El mayor(4) de los f+
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice4 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[20]) - float(valor[6]);  # (f+) = fP - fo
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1 and contador != indice2 and contador != indice3):
        comparador1 = comparador2;
        indice4 = contador;
salida[indice4] = salida[indice4] + "(4)"; # (f+) = fP - fo

# El mayor(1) de los f-
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice1 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[6]) - float(valor[13]); # (f-) = fo - fM
    salida[contador] =  salida[contador] + "," + str( comparador2 );
    if(comparador1 < comparador2):
        comparador1 = comparador2;
        indice1 = contador;
salida[indice1] = salida[indice1] + "(1)"; 

# El mayor(2) de los f-
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice2 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[6]) - float(valor[13]); # (f-) = fo - fM
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1):
        comparador1 = comparador2;
        indice2 = contador;
salida[indice2] = salida[indice2] + "(2)";

# El mayor(3) de los f-
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice3 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[6]) - float(valor[13]); # (f-) = fo - fM
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1 and contador != indice2):
        comparador1 = comparador2;
        indice3 = contador;
salida[indice3] = salida[indice3] + "(3)"; 

# El mayor(4) de los f-
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice4 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = float(valor[6]) - float(valor[13]); # (f-) = fo - fM
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1 and contador != indice2 and contador != indice3):
        comparador1 = comparador2;
        indice4 = contador;
salida[indice4] = salida[indice4] + "(4)";



# El mayor(1) de los f0
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice1 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = ( float(valor[20]) - float(valor[13]) ) / 2; # f0 = (fP - fM) / 2
    salida[contador] =  salida[contador] + "," + str( comparador2 );
    if(comparador1 < comparador2):
        comparador1 = comparador2;
        indice1 = contador;
salida[indice1] = salida[indice1] + "(1)"; 

# El mayor(2) de los f0
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice2 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = ( float(valor[20]) - float(valor[13]) ) / 2; # f0 = (fP - fM) / 2
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1):
        comparador1 = comparador2;
        indice2 = contador;
salida[indice2] = salida[indice2] + "(2)";

# El mayor(3) de los f0
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice3 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = ( float(valor[20]) - float(valor[13]) ) / 2; # f0 = (fP - fM) / 2
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1 and contador != indice2):
        comparador1 = comparador2;
        indice3 = contador;
salida[indice3] += "(3)"; 

# El mayor(4) de los f0
comparador1 = 0; # variable1 para comparar
comparador2= 0; # variable2 para comparar
indice4 = 0; # guarda la ubicacion del mayor numero
contador = 0; # de renglones
for contador in range(renglones - 10):
    valor = salida[contador].split(",");
    comparador2 = ( float(valor[20]) - float(valor[13]) ) / 2; # f0 = (fP - fM) / 2
    #salida[contador] = salida[contador] + str( comparador2 );
    if(comparador1 < comparador2 and contador != indice1 and contador != indice2 and contador != indice3):
        comparador1 = comparador2;
        indice4 = contador;
salida[indice4] = salida[indice4] + "(4)";


# Escribe en el .CSV


nombre = (sys.argv[1]).split(".");
nombreArchivoSalida = nombre[0] + time.strftime("-%y%m%d-%H%M%S") + ".csv";
archivoSalida = open( nombreArchivoSalida , "w"); 
archivoSalida.write("Salida del programa 'fukui.py' creado por Ricardo Loaiza y Joaquin Barroso\n");

archivoSalida.write("Original," + sys.argv[1] +",,,,,,Minus," + sys.argv[2] + ",,,,,,Plus," + sys.argv[3] + ",,,,,,,,,Funciones\n");
archivoSalida.write("Atom,No,Charge,Core,Valence,Rydberg,Total,Atom,No,Charge,Core,Valence,Rydberg,Total,Atom,No,Charge,Core,Valence,Rydberg,Total,,Atom,No,f+,f-,f_0\n");
for contador in range(renglones - 9):
    archivoSalida.write(salida[contador] + "\n");
archivoSalida.close() 

fukuiLog.write( nombreArchivoSalida );
fukuiLog.close() 

print ( "\n Resultados en: " + nombreArchivoSalida );