from app.models import  Inmueble


def get_all_inmuebles():
 Inm = Inmueble.objects.all()
 return Inm



def insertar_inmueble(data):
    id_user = data[0]
    id_tipo_inmueble = data[1]
    id_comuna = data[2]
    id_region = data[3]
    nombre_inmueble = data[4]
    descripcion = data[5]
    m2_construido = data[6]
    numero_banos = data[7]
    numero_hab = data[8]
    direccion = data[9]
    inm = Inmueble(
    id_user = id_user,
    id_tipo_inmueble = id_tipo_inmueble,
    id_comuna = id_comuna,
    id_region = id_region,
    nombre_inmueble = nombre_inmueble,
    descripcion = descripcion,
    m2_construido = m2_construido,
    numero_banos = numero_banos,
    numero_hab = numero_hab,
    direccion = direccion)
    inm.save()
    
 
 
def actualizar_descrp_inmueble(id_inmueble,new_descrip):
    Inmueble.objects.filter(pk=inmueble_id).update(descripcion=new_descrip)
 
 
def eliminar_inmueble(id_inmueble):
    Inmueble.objects.get(id=id_inmueble).delete()