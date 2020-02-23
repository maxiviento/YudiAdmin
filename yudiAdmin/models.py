from django.db import models
#from django_mysql.models import JSONField


class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    dni = models.CharField(max_length=20)

class Operador(models.Model):
    id_operador = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Resolutor(models.Model):
    id_resolutor = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Medio(models.Model):
    nombre = models.CharField(max_length=20)

class Persona_medio(models.Model):
    contacto = models.CharField(max_length=20)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_medio = models.ForeignKey(Medio, on_delete=models.CASCADE)

class Origen(models.Model):
    medio = models.CharField(max_length=20)

class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    referente = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Respuesta_frecuente(models.Model):
    respuesta = models.CharField(max_length=50)
    id_programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

class Estado_consulta(models.Model):
    estado = models.CharField(max_length=50)

class Consulta(models.Model):
    fecha_origen = models.DateField()
    fecha_respuesta = models.DateField()
    pregunta = models.CharField(max_length=100)
    respuesta_especifica = models.CharField(max_length=100)
    id_resp_frec = models.ForeignKey(Respuesta_frecuente, on_delete=models.CASCADE)
    id_programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    id_origen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    operador =  models.ForeignKey(Operador, default = "", on_delete=models.CASCADE)
    resolutor =  models.ForeignKey(Resolutor, default = "", on_delete=models.CASCADE)
    id_ciudadano =  models.ForeignKey(Persona, default = "", on_delete=models.CASCADE)
    id_estado =  models.ForeignKey(Estado_consulta, on_delete=models.CASCADE)

class Parseo(models.Model):
    fecha_parseo = models.DateField()
    nombre = models.CharField(max_length=20, default = "")
    def __str__(self):
        return self.nombre

class Contacto_parseo(models.Model):
    contacto = models.CharField(max_length=20, default = "")
    id_parseo =  models.ForeignKey(Parseo, default = "", on_delete=models.CASCADE)
    #chat = models.JSONField()
    def __str__(self):
        return self.contacto




