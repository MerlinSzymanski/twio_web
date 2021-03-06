from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse #to get absolut_urls
from datetime import datetime, timedelta
from multiselectfield import MultiSelectField
from PIL import Image

class News(models.Model):
    title = models.CharField("Titel", max_length=200)
    capture = models.TextField("Kurzbeschreibung", blank=True, null=True)
    content = models.TextField("Beitrag", blank=True, null=True)
    content_rendered = models.TextField(blank=True, null=True)
    picture = models.ImageField("Stockphoto", blank=True, null=True, upload_to="beiträge/")
    
    def __str__(self):
        return f"Beitrag: {self.title}"
        
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={"pk": self.pk})

# Create your models here.
class Spot(models.Model):
    title = models.CharField("Spotname", max_length=30)
    lat = models.CharField("Latitude", max_length=30, default="51.347127")
    long = models.CharField("Longitude", max_length=30,default="12.350504")
    description = models.TextField("Beschreibung, Zusatzinformation", default="Lorem Ipsum")
    description_rendered = models.TextField(blank=True, null=True)
    picture = models.ImageField("Foto vom Spot", blank=True, null=True, upload_to="spot_pics/")

    def __str__(self):
        return f"Spot: {self.title}"
        
    def get_absolute_url(self):
        return reverse('spot_detail', kwargs={"pk": self.pk})

class Group(models.Model):
    group_id = models.CharField("Gruppe (z.B 'A')", max_length=10)

    def __str__(self):
        return f"Gruppe: {self.group_id}"

    def get_absolute_url(self):
        return reverse('group_list')


class Event(models.Model):
    allowed_groups = models.ManyToManyField(Group, verbose_name="Für die Gruppen")
    
    title = models.CharField("Event-name", max_length=100)
    place = models.CharField("Veranstaltungsort", max_length=200, blank=True, default="Leipzig")
    description = models.TextField("Beschreibung", blank=True)
    description_rendered = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField("Anmeldung/Abmeldung bis", default= datetime(2020, 11, 14, 1, 54, 52, 799289))
    start_date = models.DateTimeField("Datum Beginn", default= datetime(2020, 11, 14, 1, 54, 52, 799289))
    end_date = models.DateTimeField("Datum Ende", default= datetime(2020, 11, 14, 1, 54, 52, 799289))
    hinweis = models.CharField("Hinweis", blank=True, max_length=50)
    costs = models.IntegerField("Kosten", blank=True, null=True)
    info_only = models.BooleanField("Nur Ankündigung?",default=False)
    
    teilnahmebedingungen = models.FileField("Teilnahmebedingungen", upload_to=f"Events/Docs/",null=True,blank=True)
    datenschutz = models.FileField("Datenschutzerklärung",upload_to=f"Events/Docs/",null=True,blank=True)
    einverstaendnis = models.FileField("Einverständnis",upload_to=f"Events/Docs/",null=True,blank=True)
    
    participants = models.ManyToManyField(User)

    #if we query over events, we want the most recent one firsthand 
    class Meta:
        ordering = ["start_date"]
    
    #This we need to return the url on creating a new event 
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={"pk": self.pk})
    
    @property
    def is_past_due(self):
        return datetime.now().replace(tzinfo=None) > self.end_date.replace(tzinfo=None) + timedelta(days=3)
    @property
    def deadline_reached(self):
        return datetime.now().replace(tzinfo=None) > self.deadline.replace(tzinfo=None)
    
    def __str__(self):
        return f"Event: {self.title}"
        
        
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainer_telnr = models.CharField("Öffentliche Telefonnummer", max_length=100, default = "Hier die Nummer für die Website")
    trainer_email = models.CharField("Öffentliche Email", max_length=150, default = "Hier die Email für die Website")
    image = models.ImageField("Profilbild", upload_to="profile_pics/")
    salary = models.CharField("Bezahlung", blank=True, null=True, max_length=5)
    license_level = models.CharField("Lizenzstufe", max_length=100, blank=True, null=True)
    license_number = models.CharField("Lizenznummer", max_length=100, blank=True, null=True)
    license_valid = models.DateTimeField('Gültigkeit', blank=True, null=True)
    license = models.FileField("Lizenz", upload_to="trainer_stuff", blank=True, null=True)
    contract = models.FileField("Vertrag", upload_to="trainer_stuff", blank=True, null=True)
    codex = models.FileField("Ehrencodex", upload_to="trainer_stuff", blank=True, null=True)
    
    def __str__(self):
        return f"Trainer: {self.user.first_name} {self.user.last_name}"
    
    def get_absolute_url(self):
        return reverse('trainer_list')
        
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if(img.height > img.width):
            cut = int((img.height-img.width)/2)
            img = img.crop((0, 0+cut, img.width, img.height-cut))
            img2 = img.resize((720,720))
            img2.save(self.image.path)
        elif(img.width > img.height):
            cut = int((img.width-img.height)/2)
            img = img.crop((0+cut, 0, img.width-cut, img.height))
            img2 = img.resize((720,720))
            img2.save(self.image.path)
    
    def trainer_info(self):
        info = [f"Trainer:\t{self.user.first_name} {self.user.last_name}"]
        if self.license_number:
            info.append(f"Lizenznummer:\t{self.license_number}")
        if self.license_valid:
            info.append(f"Gültigkeit:\t{self.license_valid.strftime('%d.%m.%Y')}")
    
        return "\n".join(info)
    
class Session(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name = u"Gruppe",blank=True, null=True,)
    trainer = models.ManyToManyField(Trainer, blank=True, verbose_name =u"Trainer")
    spot = models.ForeignKey(Spot, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u"Spot")
    
    title = models.CharField("Titel", max_length=50, default="Hallentraining")
    day = models.CharField("Tag",max_length=2, default="Mo")
    day_key = models.IntegerField("Key", default=1)
    
    start_time = models.TimeField("Beginn",default="17:00")
    end_time = models.TimeField("Ende",default="19:00")
    hinweis = models.CharField("Hinweis", blank=True, max_length=50)
    
    class Meta:
        permissions = [('see_group', 'Can see members of the group')]
    
    @property
    def format_start_time(self):
        return self.start_time.strftime("%H:%M")
    
    @property
    def format_end_time(self):
        return self.end_time.strftime("%H:%M")
    
    @property
    def weekday(self):
        tag={
        "Mo":"Montags",
        "Di":"Dienstags",
        "Mi":"Mittwochs",
        "Do":"Donnerstags",
        "Fr":"Freitags",
        "Sa":"Samstags",
        "So":"Sonntags",
        }
        if(self.day in tag):
            return tag[self.day]
        else: 
            return "Irgendwann"
            
    def get_absolute_url(self):
        return reverse('session_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return f"Session: {self.title}_{self.group.group_id_self.day}"
        
    class Meta:
        ordering = ["day_key"]

class Message(models.Model):
    choices =(
        ("sessions","Sessions"),
        ("events","Events")
    )
    title = models.CharField("Titel",max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField("Hinweis",default = "Deine Nachricht hier")
    date = models.DateTimeField(default=datetime(2020, 11, 14, 1, 54, 52, 799289))
    display = models.CharField(max_length=20, choices=choices, blank=True)
    groups = models.ManyToManyField(Group,verbose_name="Für die Gruppen")
    
    def __str__(self):
        return f"Message: {self.title}"
    
    def get_absolute_url(self):
        return reverse('index')

class Chairman(models.Model):
    choices = (('member_site', 'Anzeige Mitglieder'),
              ('interested_site', 'Anzeige Interessierte'),
              ('event_site', 'Anzeige Veranstalter'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_telnr = models.CharField("Öffentliche Telefonnummer", max_length=100, default = "Hier die Nummer für die Website")
    public_email = models.CharField("Öffentliche Email", max_length=150, default = "Hier die Email für die Website")
    competences = models.TextField("Zuständigkeiten (mit Komma getrennt)")
    image = models.ImageField("Profilbild", upload_to="profile_pics/")
    show = MultiSelectField(choices=choices, blank=True)
    
    def __str__(self):
        return f"Vorstand: {self.user.first_name} {self.user.last_name}"
    @property
    def complist(self):
        return self.competences.split(",")
    
    def get_absolute_url(self):
        return reverse('index')
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if(img.height > img.width):
            cut = int((img.height-img.width)/2)
            img = img.crop((0, 0+cut, img.width, img.height-cut))
            img2 = img.resize((720,720))
            img2.save(self.image.path)
        elif(img.width > img.height):
            cut = int((img.width-img.height)/2)
            img = img.crop((0+cut, 0, img.width-cut, img.height))
            img2 = img.resize((720,720))
            img2.save(self.image.path)

class Profile(models.Model):
    choices = (('Ordentliches Mitglied', 'Ordentliches Mitglied'),
              ('Förderndes Mitglied', 'Förderndes Mitglied'),
              ('Pausiertes Mitglied', 'Pausiertes Mitglied'),
              ('Kündigung', 'Kündigung')
              )
    choices2 = (('SEPA', 'SEPA'),
              ('Dauerauftrag', 'Dauerauftrag'),
              ('Überweisung', 'Überweisung'))
    
    #peronal data
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField("Geburtstag",null=True, blank=True)
    address = models.CharField("Adresse", max_length=300, null=True, blank=True)
    telephone = models.CharField("Telephone", max_length=20, null=True, blank=True)
    sex = models.CharField("Geschlecht", default="w", max_length=1)
    
    #for u18
    parent = models.CharField("Ansprechpartner*in", max_length=100, null=True, blank=True)
    parent_telnr = models.CharField("Notfallnummer", max_length=100, null=True, blank=True)
    
    # club data
    status = models.CharField(max_length=40, choices=choices, default="Ordentliches Mitglied")
    member_num = models.CharField("Mitgliedsnummer", blank=True, max_length=30)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL)
    membership_start = models.DateTimeField("Beginn der Mitgliedschaft",null=True, blank=True)
    membership_end = models.DateTimeField("Kündigung zum", null=True, blank=True) 
    ermaessigt = models.BooleanField("Ermäßigt?", default=False)
    mandatsref = models.CharField("Mandatsreferenz", max_length=40, null=True, blank=True)
    zahlungsart = models.CharField("Zahlungsart",choices=choices2, max_length=30, default="SEPA")
    beitrag = models.IntegerField("Beitragshöhe", default = 20)
    notes_trainer = models.TextField("Notizen für den/die Trainer*in",null=True, blank=True)
    notes_chairman = models.TextField("Notizen für den Vorstand",null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}\'s Profile"
        
    def get_absolute_url(self):
        return reverse('member_list')
        