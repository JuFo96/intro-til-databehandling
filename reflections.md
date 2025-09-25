## Generelle indtryk 
Jeg var generelt komfortabel med opgaverne, da jeg har arbejdet med lignende opgaver før. Derfor prøvede jeg at have ekstra fokus på dokumentation, konsistente variable navne og "self describing code". Derudover har jeg prøvet at udfordre mig selv ved at lave filerne interaktive med argparse, som jeg ikke har brugt før. 


### Nye biblioteker
Jeg har ikke arbejdet med følgende biblioteker før
- argparse
- pathlib 
- dataclasses

De er derfor også implementeret lidt forskelligt i de fire filer, da jeg fik mere erfaring med dem undervejs. Jeg er usikker på "best practises" i forhold til opbevaring af bruger input, jeg endte med at benytte dataclasses i de sidste to opgaver og laver et nyt objekt efter at have hentet bruger input

### Dokumentation
Jeg er usikker på hvad der forventes af docstrings, jeg prøvede at følge googles format, det føltes dog nogen gange overkill for simple funktioner og gjorde filen mindre overskuelig. Jeg har prøvet at minimere brugen af kommentarer og erstatte dem med variable navne hvor det gav mening.

### Generel struktur
Jeg har opbygget filerne efter en funktionel struktur, da det er hvad jeg generelt har mest erfaring med og tænker giver mest mening for relativt simple "læs data &rarr; bearbejd data &rarr; print/skriv data" workflows. Men jeg er meget åben for feedback, hvis OOP eller andre strukturer giver mere mening.

Derudover har jeg også været lidt usikker på mappestrukturen, jeg endte med at hardcode filstier med pathlib, det føles lidt som et hack, men igen er jeg usikker på, hvad best practices er.