# API projekt - 50/50 Chuck/Fox

## Teknologier/Språk

Hela projektet är skrivet i Python. Mer specifikt är det Python 3.10. Programmet använder sig av det inbyggda Python biblioteken time. Samt även av biblioteken requests, openpyxl och getpwd. Programmet är på engelska med kommenteringen är på svenska.

## Hur det fungerar (Usage)

Programmet börjar med att fråga om du vill logga in eller avsluta programmet. När programmet avslutas skriver det ut 'Goodbye' och ett Chuck Norris skämt. När man loggar in ber programmet att man skiver in sitt För och efternamn och sedan frågar det efter lösenordet. Om användaren loggas in kommed den till en meny med olika alternativ. Alternativen på vad användaren kan göra beror på om den är Admin, User eller Underage_user. Det som är gemensamt med alla är alternativet att logga ut.

Som admin kan man skapa en ny användare, byta lösenord på sin användare och finna information om alla användare givet att man har namnet på användaren. Anledningen till att admin inte kan kolla på vem som helst är för att det skulle vara för mycket makt i programmet. Om det hade varit en riktig bank får ju bara personalen kolla i folks information om de har tillstånd från personen.

som User kan du kolla hur mycket pengar du har och byta lösenord.

Som Underage_user kan du bara kolla hur mycket pengar du har. Detta är också pågrund av säkerhetsskäl.

Funktioner:

login() funktionen är redan i beskrivningen.

create_new_user(). Skapar en nyh användare genom att fråga efter den relevanta infomrationen och sedan för att vara säker skriver den ut informationen och frågar om den är rätt.

change_password(). Frågar om det nya lösen ordet och sedan att man ska skriva in den igen för att vara säker på att man skrev rätt.

"Find user information" är inte en funktion enligt programmerings deffinitionen men det är en funktion hos admin användare. Den frågar efter för och efternamn på personen som informationen ska hämtas ifrån och sedan ges olika alternativ på vilken information man vill komma åt. Lösenord, konto saldo, användartyp (admin ,user eller underage_user) och ingenting.

"Money money money money... MONEY!(In falsetto)". Skriver ut hur mycket pengar användaren har i sitt konto.

"Loggout". Loggar ut användaren.

get_chuck(). Hämtar in ett Chuck Norris skämt från 'https://api.chucknorris.io/jokes/random' API:n och skriver ut det.

## UML-Diagram

![Skärmbild (9)](https://user-images.githubusercontent.com/91462301/168466665-6c669984-057b-477e-9b37-c9c3184d39da.png)

## Installation

Det som behöver installeras för att köra programmet är Python biblioteken requests, openpyxl och getpwd.

För att installera:

```powershell
pip install requests
```

```powershell
pip install openpyxl
```

```powershell
pip install getpwd
```

## Medvetna fel (issue tracker)

Inga medvetna fel förekommer.

## To do

Det finns ingen anledning att fortsätta utveckla programmet. Det har bara ett examinerande värde och bör därför inte fortsättas på.

## Att bidra (contribution)

Inga bidrag kommer accepteras.
Det är ett skolprojekt och behöver inte vidare utvecklas.
Det går bra att använda koden för eget bruk men jag ser ingen riktig anledning till att göra det.
Om du använder programmet får du gärna ange mig som en Contributor men det gör inget om inte.

## Projektet är färdigt

Projektet är färdigt och blev klart 15-05-2022.

## Licens (License)

[MIT](https://choosealicense.com/licenses/mit/)

## Kontakt information

Noneofyourdamnbusiness.com
och på github antar jag ;)
