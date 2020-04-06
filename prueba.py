ancho_matriz_grande=16
alto_matriz_grande=16

ancho_submatriz=4
alto_submatriz=4


if( (ancho_matriz_grande%ancho_submatriz==0) && (alto_matriz_grande%alto_submatriz==0))
{
for(int y=0;y<alto_matriz_grande;y=y+altosubmatriz)
{
	for(int x=0;x<ancho_matriz_grande;x=x+anchosubmatriz)
	{
		for(int j=0;j<alto_submatriz;j++)
		{
	
			for(int i=0;i<ancho_submatriz;i++)
			{

				print(matriz[x*anchosubmatriz + i][y*altosubmatriz+j]);
				print(";");
			}
			
			println();
			

		}




	}



}


}