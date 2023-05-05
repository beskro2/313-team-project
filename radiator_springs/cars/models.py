from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

DChallenger = Car()
DChallenger.name = "Dodge Challenger"
DChallenger.description = "Dodge’s pony car, the 1970 Challenger, arrived at the peak of the classic muscle-car era. Closely related to the 1970 Plymouth Barracuda, the Challenger was offered as a coupe or convertible and could be had with an inline-six-cylinder engine or a broad range of increasingly muscular V-8s, reaching all the way up to the legendary 426 Hemi. The market for muscle and pony cars faded rapidly in the early '70s, and the original Challenger was gone after 1974. Today’s Challenger arrived as a 2008 model wearing retro-coupe styling inspired by the 1970 original."
DChallenger.save()

CCorvette = Car()
CCorvette.name = "1968 Chevrolet Corvette L88"
CCorvette.description = "Conceived as a bone-fide home-grown sportscar to rival European imports, the two seat Chevrolet Corvette may not fit the muscle car tag for many US enthusiasts. But to the rest of the world the car’s big block V8 engine options and affordable price tag made it a prime example of the breed. \n The Mako shark-inspired Corvette C3 Stingray arrived in 1968 at the peak of the muscle car era, and included an L88 big block engine option designed primarily for racing. The 427 cubic inch (7.0-litre) V8 had an advertised horsepower of 430bhp, but many believe production models actually escaped from the factory with upwards of 550bhp. Other L88 upgrades included a heavy-duty four speed manual gearbox, uprated brakes and suspension, and deletion of the air con, heater and radio options."
+ " \n In racing trim, the L88 Corvette would hit 171mph at Le Mans, and although GM had to offer it for sale to the public to meet racing rules it was never actively promoted as a road car. That’s why fewer than 200 examples were ever sold."
CCorvette.save()

DHellcat = Car()
DHellcat.name = "Dodge Challenger Hellcat"
DHellcat.description = "The muscle car revival that began in the early noughties has seen lots of big-hitting V8 models back in showrooms, but nothing has yet compared to the Dodge Challenger Hellcat introduced in 2015. \n If we thought the Chevrolet Camaro ZL1 was over the top with 580bhp, or the Ford Mustang GT500 was outrageous with 650bhp, then the 707bhp pumped out by the 6.2-litre Hemi V8-engined Dodge Challenger Hellcat is simply shocking. That means it’s packing more power than many supercars, and with the optional paddle-shifted eight-speed auto gearbox, the Hellcat races to 60mph in just 3.6 seconds. \n In true Muscle Car style it’s cheap too – at least compared to those Supercar rivals – with the sticker price starting at just over $64k. "
DHellcat.save()