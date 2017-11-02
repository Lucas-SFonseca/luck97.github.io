class Disciplinas(models.Model):
    professor = model.CharField("Professor", max_length=50)
    horasMensais = model.CharfFld("horasMensais", max_length=100)
    horaAula = model.CharField("horaAula", max_length=10)
    ementa = model.CharField("ementa",max_length=1000)       
