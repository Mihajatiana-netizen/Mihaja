from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_de_telephone= models.CharField(max_length=20, default="0387377789")
    niveau= models.CharField(max_length=50, default= 'Première années')
    adresse= models.CharField(max_length=225, default='Vontovorona Bloc 16 porte 565')
    age= models.PositiveIntegerField(default=18)
    birthdate = models.DateField(null=True, blank=True)
    image= models.ImageField(upload_to='profile/', blank=True, null=True)
    #photo_coverture= models.ImageField(upload_to='coverture/')
    type_etablissement= models.BooleanField(default=False,) #Raha false izy dia profil etudiant, raha vrai izy dia profil """
    #etablissement (afaka magnano publication)
    carrier_reve= models.CharField(max_length=255, default="Ingenieur")
    etablissement_freq= models.CharField(max_length=255, blank=True, null=True)
    slogan= models.CharField(max_length=10000, default="")
    ecoles_origine= models.TextField(default="Ingenieur")
    biographie= models.TextField(max_length=100000, default="")
    parcours_disponible =models.TextField(max_length=10000, default="")

    def __str__(self):
        return self.user.username
    

class Publication(models.Model):
    legend= models.CharField(max_length=5000, default=" ")
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='publication')
    image_1= models.ImageField(upload_to='publicatio/', null=True, blank=True)
   

    def __str__(self):
        return self.legend
    


class Commentaires(models.Model):
    #1user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pr')
    pub = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='conex_pub')
    # variables commentaire io lay miassurer liaison n table commentaire aminy table publication
    sender_coms= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_coms')
    coms = models.CharField(max_length=1000, default=" ") #ty lay chaine de caractere lay misaoratra aminy commentaire ign

    def __str__(self):
        return self.coms
    

class Reaction(models.Model):
    pub = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='conex_react')
    # variables commentaire io lay miassurer liaison n table commentaire aminy table publication
    sender_react= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_react')
    nombre_de_reaction= models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre_de_reaction
    
    

class Message(models.Model):
    sender= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient= models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_message')
    texte= models.CharField(max_length=10000, default="")
    
    def __str__(self):
        return self.texte


