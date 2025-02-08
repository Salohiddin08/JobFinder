from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Davlatlar ro'yxati
class Country(models.Model):
    countries = [
        ("AF", "Afghanistan"), ("AL", "Albania"), ("DZ", "Algeria"), ("AD", "Andorra"),
        ("AO", "Angola"), ("AG", "Antigua and Barbuda"), ("AR", "Argentina"), ("AM", "Armenia"),
        ("AU", "Australia"), ("AT", "Austria"), ("AZ", "Azerbaijan"), ("BS", "Bahamas"),
        ("BH", "Bahrain"), ("BD", "Bangladesh"), ("BB", "Barbados"), ("BY", "Belarus"),
        ("BE", "Belgium"), ("BZ", "Belize"), ("BJ", "Benin"), ("BT", "Bhutan"), ("BO", "Bolivia"),
        ("BA", "Bosnia and Herzegovina"), ("BW", "Botswana"), ("BR", "Brazil"), ("BN", "Brunei"),
        ("BG", "Bulgaria"), ("BF", "Burkina Faso"), ("BI", "Burundi"), ("CV", "Cabo Verde"),
        ("KH", "Cambodia"), ("CM", "Cameroon"), ("CA", "Canada"), ("CF", "Central African Republic"),
        ("TD", "Chad"), ("CL", "Chile"), ("CN", "China"), ("CO", "Colombia"), ("KM", "Comoros"),
        ("CG", "Congo"), ("CD", "Congo (Democratic Republic)"), ("CR", "Costa Rica"), ("HR", "Croatia"),
        ("CU", "Cuba"), ("CY", "Cyprus"), ("CZ", "Czech Republic"), ("DK", "Denmark"), ("DJ", "Djibouti"),
        ("DM", "Dominica"), ("DO", "Dominican Republic"), ("EC", "Ecuador"), ("EG", "Egypt"),
        ("SV", "El Salvador"), ("GQ", "Equatorial Guinea"), ("ER", "Eritrea"), ("EE", "Estonia"),
        ("SZ", "Eswatini"), ("ET", "Ethiopia"), ("FJ", "Fiji"), ("FI", "Finland"), ("FR", "France"),
        ("GA", "Gabon"), ("GM", "Gambia"), ("GE", "Georgia"), ("DE", "Germany"), ("GH", "Ghana"),
        ("GR", "Greece"), ("GD", "Grenada"), ("GT", "Guatemala"), ("GN", "Guinea"), ("GW", "Guinea-Bissau"),
        ("GY", "Guyana"), ("HT", "Haiti"), ("HN", "Honduras"), ("HU", "Hungary"), ("IS", "Iceland"),
        ("IN", "India"), ("ID", "Indonesia"), ("IR", "Iran"), ("IQ", "Iraq"), ("IE", "Ireland"),
        ("IL", "Israel"), ("IT", "Italy"), ("JM", "Jamaica"), ("JP", "Japan"), ("JO", "Jordan"),
        ("KZ", "Kazakhstan"), ("KE", "Kenya"), ("KI", "Kiribati"), ("KP", "Korea, North"), ("KR", "Korea, South"),
        ("KW", "Kuwait"), ("KG", "Kyrgyzstan"), ("LA", "Laos"), ("LV", "Latvia"), ("LB", "Lebanon"),
        ("LS", "Lesotho"), ("LR", "Liberia"), ("LY", "Libya"), ("LI", "Liechtenstein"), ("LT", "Lithuania"),
        ("LU", "Luxembourg"), ("MG", "Madagascar"), ("MW", "Malawi"), ("MY", "Malaysia"), ("MV", "Maldives"),
        ("ML", "Mali"), ("MT", "Malta"), ("MH", "Marshall Islands"), ("MR", "Mauritania"), ("MU", "Mauritius"),
        ("MX", "Mexico"), ("FM", "Micronesia"), ("MD", "Moldova"), ("MC", "Monaco"), ("MN", "Mongolia"),
        ("ME", "Montenegro"), ("MA", "Morocco"), ("MZ", "Mozambique"), ("MM", "Myanmar"), ("NA", "Namibia"),
        ("NR", "Nauru"), ("NP", "Nepal"), ("NL", "Netherlands"), ("NZ", "New Zealand"), ("NI", "Nicaragua"),
        ("NE", "Niger"), ("NG", "Nigeria"), ("MK", "North Macedonia"), ("NO", "Norway"), ("OM", "Oman"),
        ("PK", "Pakistan"), ("PW", "Palau"), ("PA", "Panama"), ("PG", "Papua New Guinea"), ("PY", "Paraguay"),
        ("PE", "Peru"), ("PH", "Philippines"), ("PL", "Poland"), ("PT", "Portugal"), ("QA", "Qatar"),
        ("RO", "Romania"), ("RU", "Russia"), ("RW", "Rwanda"), ("KN", "Saint Kitts and Nevis"), ("LC", "Saint Lucia"),
        ("VC", "Saint Vincent and the Grenadines"), ("WS", "Samoa"), ("SM", "San Marino"), ("ST", "Sao Tome and Principe"),
        ("SA", "Saudi Arabia"), ("SN", "Senegal"), ("RS", "Serbia"), ("SC", "Seychelles"), ("SL", "Sierra Leone"),
        ("SG", "Singapore"), ("SK", "Slovakia"), ("SI", "Slovenia"), ("SB", "Solomon Islands"), ("SO", "Somalia"),
        ("ZA", "South Africa"), ("SS", "South Sudan"), ("ES", "Spain"), ("LK", "Sri Lanka"), ("SD", "Sudan"),
        ("SR", "Suriname"), ("SE", "Sweden"), ("CH", "Switzerland"), ("SY", "Syria"), ("TW", "Taiwan"),
        ("TJ", "Tajikistan"), ("TZ", "Tanzania"), ("TH", "Thailand"), ("TL", "Timor-Leste"), ("TG", "Togo"),
        ("TO", "Tonga"), ("TT", "Trinidad and Tobago"), ("TN", "Tunisia"), ("TR", "Turkey"), ("TM", "Turkmenistan"),
        ("TV", "Tuvalu"), ("UG", "Uganda"), ("UA", "Ukraine"), ("AE", "United Arab Emirates"), ("GB", "United Kingdom"),
        ("US", "United States"), ("UY", "Uruguay"), ("UZ", "Uzbekistan"), ("VU", "Vanuatu"), ("VA", "Vatican City"),
        ("VE", "Venezuela"), ("VN", "Vietnam"), ("YE", "Yemen"), ("ZM", "Zambia"), ("ZW", "Zimbabwe")
    ]
    country = models.CharField(max_length=100, choices=countries)

    def __str__(self):
        return self.country

# Region modeli
class Region(models.Model):
    name = models.CharField(max_length=100)  # Region nomi
    country = models.CharField(max_length=100)  # Davlat nomi
    
    def __str__(self):
        return f"{self.name}, {self.country}"

# Shahar modeli
class City(models.Model):
    name = models.CharField(max_length=100)  # Shahar nomi
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

# Profil modeli
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey("City", related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)

# SIGNAL: Foydalanuvchi yaratilganda yangi profil yaratish
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# SIGNAL: Profilni saqlash
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
