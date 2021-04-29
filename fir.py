import pandas as pd
import seaborn as sns

# Leemos el dataset con los datos 2016-2019
df = pd.read_csv('FIR.csv',delimiter=';')

# Elegimos las ciudades y especialidades deseadas
ciudades_deseadas = ['MADRID', 'VALENCIA', 'BARCELONA', 'ZARAGOZA']
especialidad = ['FH', 'MICRO','INMUNO', 'AC', 'BQCLIN', 'RAD']
convocatorias = df['Convocatoria'].unique().tolist()
convocatorias.sort()

def preprocesado (df,especialidad):
    # Creamos columnas con valor 0-1 con cada ciudad existente
    ciudades = df['Ciudad'].unique().tolist()
    for x in ciudades:
        df[x] = df['Ciudad'].str.contains(x)
        df[x] = df[x].map({True: 1, False: 0})

    # Creamos columnas con valor 0-1 con cada especialidad deseada
    for y in especialidad:
        df[y] = df['Especialidad'].str.contains(y)
        df[y] = df[y].map({True: 1, False: 0})

    # Identificamos las distintas convocatorias y partimos el dataset en base a ello
    fir = df.groupby('Convocatoria')
    return fir,df

def plazasPorEspecialidad(fir, convocatorias):    
    # Pintamos las plazas totales por convocatoria en función de la especialidad elegida
    contador = 0
    palette = sns.color_palette("bright", n_colors=len(especialidad))
    for x in fir.groups:
        ax = fir.get_group(x).plot(x ='Numero', y=especialidad,kind = 'bar', figsize =(18, 8), title='Plazas por especialidades ' +str(convocatorias[contador]), stacked=True, width=1, color=palette)
        ax.set_xticks(fir.get_group(x)['Numero'][::10])
        ax.set_xticklabels(fir.get_group(x)['Numero'][::10], rotation=45)
        ax.set_xlabel("Numero de plaza obtenida")
        ax.set_yticks([0,1])
        ax.set_yticklabels(["No seleccionada", "Seleccionada"])
        contador = contador + 1
        
def plazasPorCiudadesDeseadas (fir, ciudades_deseadas, convocatorias):
    # Pintamos las plazas seleccionadas en esas ciudades en cada convocatoria
    contador = 0
    palette = sns.color_palette("bright", n_colors=len(ciudades_deseadas))
    for x in fir.groups:
        ax = fir.get_group(x).plot(x ='Numero', y=ciudades_deseadas,kind = 'bar', figsize =(18, 8), title='Plazas '+'en ciudades deseadas'+' '+str(convocatorias[contador]), stacked=True, width=1, color=palette)
        ax.set_xticks(fir.get_group(x)['Numero'][::10])
        ax.set_xticklabels(fir.get_group(x)['Numero'][::10], rotation=45)
        ax.set_xlabel("Numero de plaza obtenida")
        ax.set_yticks([0,1])
        ax.set_yticklabels(["No seleccionada", "Seleccionada"])
        contador = contador + 1
        
def especialidadesPorCiudadesDeseadas (df,ciudades_deseadas, convocatorias, especialidad):
    # Pintamos por cada ciudad elegida y cada convocatoria, la distribución de plazas en función de las especialidad.
    contador_ciudad = 0
    palette = sns.color_palette("bright", n_colors=len(especialidad))
    for x in ciudades_deseadas:
        contador_convocatorias = 0
        
        for y in especialidad:
            df[y] = 0
            
        # Reseteamos a 0 las columnas de especialidad porque ya las usamos antes
        for z in especialidad:
            df.loc[(df['Ciudad']==ciudades_deseadas[contador_ciudad]) & (df['Especialidad'].str.contains(z)),z] = 1
            
        # Partimos de nuevo el dataser por convocatoria
        fir = df.groupby('Convocatoria')    
        for ii in fir.groups:
            ax = fir.get_group(ii).plot(x ='Numero', y=especialidad,kind = 'bar', figsize =(18, 8), stacked=True, width=1,title = 'Plazas en '+ str(ciudades_deseadas[contador_ciudad])+' '+ str(convocatorias[contador_convocatorias]), color=palette )
            ax.set_xticks(fir.get_group(ii)['Numero'][::10])
            ax.set_xticklabels(fir.get_group(ii)['Numero'][::10], rotation=45)
            ax.set_xlabel("Numero de plaza obtenida")
            ax.set_yticks([0,1])
            ax.set_yticklabels(["No seleccionada", "Seleccionada"])  
            contador_convocatorias = contador_convocatorias + 1
        contador_ciudad = contador_ciudad + 1
    
fir,df = preprocesado(df, especialidad)
plazasPorEspecialidad(fir, convocatorias)
plazasPorCiudadesDeseadas (fir, ciudades_deseadas, convocatorias)
especialidadesPorCiudadesDeseadas (df,ciudades_deseadas, convocatorias, especialidad)