import os

output_dir = 'vypraveni-prirucka'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def zapis_soubor(nazev_souboru, obsah):
    cesta = os.path.join(output_dir, nazev_souboru)
    with open(cesta, "w", encoding="utf-8") as f:
        f.write(obsah.strip() + "\n")
    print(f"Vytvořeno: {cesta}")

# ==========================================
# 00
# ==========================================
zapis_soubor("00-uvodni-informace.md", """---
title: Úvodní informace
outline: deep
---

![](_page_0_Picture_0.jpeg)

# Vypravování dokumentů
**Informační systém stavebního řízení**

## Verze dokumentu

| Číslo verze | Datum       | Změny |
|-------------|-------------|-------|
| 1.0         | 3. 3. 2025  | První vydání |
| 1.1         | 27. 5. 2025 | Aktualizovaná verze s rozšířením |
| 1.2         | 9. 9. 2025  | Přepracování manuálu |
| 1.3         | 22. 4. 2026 | Doplněno ruční vypravení, vypravení příloh, oboustranný tisk, počet listů pro vypravení, tisk adres na obálky, okamžik doručení, hromadná evidence vyvěšení a sejmutí vyhlášky, notifikace o doručení všem adresátům, zobrazení informace o úmrtí osoby. |

## Úvod

Proces vypravení dokumentů zahrnuje několik částí, které je nezbytné zohlednit a nastavit tak, aby bylo možné dokumenty vypravit. V rámci procesu vypravení uživatel nastavuje jednotlivé účastníky řízení, následně vytváří dokument, který bude vypravován, a závěrem probíhá samotné vypravení daného dokumentu. V jednotlivých kapitolách této příručky jsou podrobně uvedeny náležitosti, které musí být splněny, pro správné vypravení dokumentů.

::: info PRINCIP AKTUALIZACE DAT
ISSŘ spravuje osoby/účastníky v záměrech, řízeních a dokumentech. Upozorňujeme uživatele, že **aktualizace dat mezi těmito částmi není vždy automatická**. 
* Přidání nové osoby do záměru nevytvoří automaticky nového účastníka v řízení.
* Přidání osoby do rozdělovníku v řízení nepřidá automaticky tuto osobu do rozdělovníků dokumentů připravovaných k odeslání.
:::

::: warning POZOR NA ZMĚNY ÚDAJŮ
Změna údajů účastníka v řízení se automaticky projeví i v rozdělovníku dokumentu, avšak tato změna **se nepropíše automaticky do obsahu již vygenerovaného dokumentu**, který je nutné v případě potřeby znovu vygenerovat.
:::

Proto doporučujeme věnovat zvýšenou pozornost při provádění změn v údajích osob a účastníků, aby bylo zajištěno správné a úspěšné vypravení dokumentů.
""")

# ==========================================
# 01
# ==========================================
zapis_soubor("01-1-pridani-osoby-do-rizeni.md", """---
title: 1. Přidání osoby do řízení a její nastavení
outline: deep
---

# 1. Přidání osoby do řízení a její nastavení

Prvním krokem pro bezchybné vypravení jsou aktuální skupiny v rozdělovníku řízení a dokumentu, obsahující všechny účastníky řízení s korektními údaji včetně způsobu komunikace.

V případě, že řízení bylo založeno na základě žádosti doručené z Portálu stavebníka, bude jako první účastník automaticky odesílatel žádosti. V systému ISSŘ je osoba odesílatele žádosti automaticky ztotožněna již při doručení dokumentu do systému ISSŘ.

Odesílatel je ověřen v detailu dokumentu, záložka `Základní informace`.

![](_page_3_Figure_9.jpeg)

Informace o ztotožnění je uvedena v auditním záznamu.

![](_page_4_Figure_1.jpeg)

Po založení řízení či vložení žádosti do řízení je ztotožněná osoba odesílatele automaticky vložena do řízení.

![](_page_4_Figure_3.jpeg)

::: warning ODSTRANĚNÍ ODESÍLATELE
Pokud není odesílatel žádosti účastníkem řízení, **je nutné tuto osobu z řízení odstranit**. I po odstranění bude mít osoba viditelné řízení na Portálu stavebníka jakožto odesílatel.
:::

Při vytvoření doručeného dokumentu v ISSŘ je nutné odesílatele ověřit před založením řízení, jinak řízení na Portálu stavebníka neuvidí. Pokud je ověřený v žádosti před založením řízení, ověření se automaticky přenese do řízení.

Pro přidání dalších účastníků v daném řízení, ve kterém vypravujete dokument, vyberte kartu `Účastníci`.

![](_page_4_Figure_7.jpeg)

## 1.1 Přidání osoby do řízení

Vyberte tlačítko `+ Přidat osobu`.

![](_page_5_Figure_2.jpeg)

Zde vyplňte požadované údaje o druhu osoby (stavebník nebo zástupce, vlastník/oprávněný k pozemku nebo stavbě, soused, jiný). Dále vyberte, o jakou osobu se jedná (fyzická, právnická, fyzická osoba podnikající) a potvrďte.

![](_page_5_Figure_4.jpeg)

### Fyzická osoba a fyzická osoba podnikající

Po výběru osoby Fyzická osoba či Fyzická osoba podnikající se vám zobrazí další karty po vyplnění údajů.

![](_page_5_Picture_7.jpeg)

Vyplňte kartu `Základní údaje`. 

::: info ZAHRANIČNÍ OSOBA
V případě, že se jedná o zahraniční osobu či o osobu, kterou z jiného důvodu nelze ztotožnit, zaškrtněte příslušný checkbox `Nelze ztotožnit / Zahraniční osoba`. Tyto osoby nelze ztotožnit, jelikož ztotožnění probíhá vůči českým základním registrům.
:::

![](_page_6_Figure_1.jpeg)

Dále vyplňte kartu `Adresa pobytu`. Zde zadejte adresu pobytu daného účastníka. V případě, že se jedná o zahraniční adresu, zaškrtněte checkbox `Zahraniční adresa` (následně se zobrazí další pole, která je nezbytné vyplnit pro úplnost zahraniční adresy a následné vypravení).

![](_page_6_Picture_3.jpeg)

V případě, že byla sdělena doručovací adresa, vyplňte kartu `Doručovací adresa` (v tomto případě zkontrolujte, že máte v části **Způsob komunikace** vybránu možnost `Poštou na doručovací adresu`). I v tomto případě zaškrtněte checkbox `Zahraniční adresa` pro možnost zadání plné adresy, pakliže je doručovací adresa v zahraničí.

![](_page_7_Picture_1.jpeg)

### Právnická osoba

Po výběru osoby Právnická osoba se Vám zobrazí další karty pro vyplnění údajů. Tyto karty jsou totožné jako v případě Fyzické osoby s následujícími dvěma rozdíly:

1. Na kartě `Základní údaje` je k dispozici řádek **K rukám**. Toto pole umožňuje specifikovat osobu, které má být zásilka předána. Jedná se o nepovinné pole, u kterého se vyplněný text následně přenese na obálku vypravených dokumentů (propíše se pouze vyplněný text, nikoli samotné spojení "K rukám").
2. Je viditelná karta `Oprávněná osoba`. V této kartě vyplňte údaje Oprávněné osoby (pokud ji právnická osoba má).

![](_page_7_Picture_5.jpeg)
![](_page_8_Figure_1.jpeg)

## 1.2 Přidání obce do řízení

Vyberte tlačítko `+ Přidat obec`.

![](_page_8_Figure_4.jpeg)

Vyberte příslušný obecní úřad. Po jeho výběru a potvrzení se úřad zobrazí na příslušné kartě. Dané obce a jejich úřady mají nastavena data a není potřeba je upravovat.

![](_page_8_Picture_6.jpeg)
![](_page_9_Picture_0.jpeg)
""")

# ==========================================
# 02
# ==========================================
zapis_soubor("02-2-overeni.md", """---
title: 2. Ověření
outline: deep
---

# 2. Ověření

Po zadání účastníka řízení je potřeba jej ověřit. V případě, že se jedná o zahraniční osobu (ať již fyzickou či právnickou), tyto není možné ověřit. V takovém případě je potřeba zaškrtnout příslušný checkbox `Nelze ztotožnit / Zahraniční osoba`. V takovém případě je osoba označena jako ověřena, aby nebyl blokován další proces řízení.

## 2.1 Ověření osoby

Jednotlivé osoby lze ověřit kliknutím na tlačítko `Ověřit osobu` v kartě nebo řádku dané osoby.

![](_page_9_Picture_5.jpeg)

Akci následně potvrďte kliknutím na tlačítko `Potvrdit`.

![](_page_10_Picture_1.jpeg)

Po ověření osoby se zobrazí nové ikony: `Zobrazit data ze záměru`, `Zobrazit ztotožněná data`, `Zkopírovat ověřená data do řízení`.

Po ověření osob se primárně zobrazují data ze záměru, která jsou doplněna o upozornění. Data nejsou automaticky přepsána na data z registru – uživatel je může převzít kliknutím na tlačítko `Zkopírovat ověřená data`.

![](_page_10_Picture_4.jpeg)

* V sekci **Zobrazit data ze záměru** jsou uvedena data, která byla vámi zadána při přidávání osoby nebo nahrána z Portálu stavebníka.
* V sekci **Zobrazit ztotožněná data** jsou uvedena data, která jsou pro danou osobu vedena v základních registrech.

Pakliže se chcete ujistit, že údaje účastníka odpovídají údajům ze základních registrů, zvolte ikonu `Zkopírovat ověřená data do řízení`. Tímto krokem dojde ke **kompletnímu přepsání** (tedy i údajů, které byly vámi zadány). Zaškrtněte checkbox přepsat data a potvrďte.

![](_page_11_Figure_1.jpeg)

::: danger DŮLEŽITÉ: ÚDAJE PRO VYPRAVENÍ
**Vypravení probíhá vždy dle údajů uvedených v Datech ze záměru!** Doporučujeme tedy využít funkcionalitu `Zkopírovat ověřená data do řízení`, abyste předešli případným chybám ve vyplněných údajích. Údaje můžete později vždy znovu upravit prostřednictvím funkcionality `Upravit osobu`.
:::

![](_page_11_Picture_4.jpeg)

## 2.2 Ověření osob se shodným jménem a datem narození

V případě, kdy je v záměru nebo řízení více osob se shodným jménem a datem narození (typicky Jan Novák), je potřeba nejprve ověřit adresu osoby a až poté ověřit osobu samotnou.

1. Nejprve klikněte na adresu pobytu.
2. V novém okně klikněte na `Ověřit adresu`.
3. Potvrďte.

![](_page_12_Figure_1.jpeg)
![](_page_12_Figure_3.jpeg)
![](_page_12_Figure_5.jpeg)

Po ověření adresy již systém určí, o kterou osobu se jedná. Pokračujte standardním způsobem ověření osoby kliknutím na ikonu lupy.

## 2.3 Ověření oprávněné osoby

V případě oprávněné osoby u právnických osob je při ověřování vždy nutné ověřit oprávněnou osobu zvlášť kliknutím na tlačítko `Ověřit oprávněnou osobu`.

![](_page_13_Picture_3.jpeg)

*(Při hromadném ověření osob v záměru/účastníků v řízení je oprávněná osoba PO také ověřena automaticky).*

## 2.4 Zobrazení informace o úmrtí osoby

Do ISSŘ bylo doplněno zobrazení informace o evidenci úmrtí osoby přímo v základním náhledu dat ze záměru. Pokud je při ověření zjištěno, že je u FO evidováno úmrtí, je tato skutečnost viditelná již v defaultním zobrazení, nikoli pouze ve ztotožněných datech.

![](_page_13_Picture_7.jpeg)

Informace je taktéž zobrazena při rozkliknutí oprávněné osoby PO.

![](_page_14_Figure_0.jpeg)

Po kliknutí na oprávněnou osobu se zobrazí dialog s náhledem oprávněné osoby včetně informace o evidenci úmrtí.

![](_page_14_Figure_2.jpeg)

## 2.5 Ověření obce

Ověření obce probíhá standardním způsobem, kliknutím na `Ověřit osobu` a chová se totožně jako ověření fyzické/právnické osoby.

![](_page_15_Figure_2.jpeg)

## 2.6 Hromadné ověření

V řízení je možné hromadně ověřit všechny účastníky kliknutím na tlačítko `Ověřit vše`. Akci potvrďte kliknutím na tlačítko `Potvrdit`.

![](_page_15_Figure_5.jpeg)
![](_page_15_Figure_7.jpeg)

::: info DÉLKA TRVÁNÍ
Hromadné ověření může dle počtu ověřovaných osob trvat déle. O jeho dokončení je uživatel informován notifikací v pravém horním rohu obrazovky.
:::

## 2.7 Ztotožněná data

Data, která systém získá ze základních registrů, jsou v systému pojmenována jako ztotožněná data. **Jméno a příjmení u osob a název společnosti jsou zobrazeny vždy VELKÝMI PÍSMENY u dat z registru.**

Ztotožněná data **není možné editovat**.

![](_page_16_Figure_3.jpeg)

## 2.8 Upozornění na rozdílná data ze záměru vs. ztotožněná data

Systém disponuje funkcí upozornění na rozdíly mezi daty načtenými z registrů a daty doplněnými uživatelem. U položek, které se liší od dat z registrů, se zobrazí **ikona vykřičníku**. Rozdíl se nevyhodnocuje podle velikosti písmen ani přítomnosti diakritiky.

![](_page_17_Figure_0.jpeg)

::: tip VÝJIMKA PRO PORTÁL STAVEBNÍKA
Při vytvoření osoby v záměru na základě podání žádosti v PS se vyplní u fyzických osob položka název. Jelikož FO nemají tuto položku v registrech, systém upozorní na nesoulad. V současné době není možné tuto položku u FO v ISSŘ editovat, proto toto upozornění ignorujte.
:::

![](_page_17_Figure_2.jpeg)

## 2.9 Data ze záměru vs. ztotožněná data – Dotčené orgány

Data se ověřují vůči nadřazenému orgánu. Z toho důvodu může být po ověření ikona vykřičníku v položce název nebo adresa. **Tato ikona je pouze informativní a neupozorňuje na chybu.** Je tedy možné tuto ikonu nebrat v potaz.

![](_page_18_Figure_2.jpeg)
![](_page_18_Picture_4.jpeg)
""")

# ==========================================
# 03
# ==========================================
zapis_soubor("03-3-zahranicni-osoby.md", """---
title: 3. Zahraniční osoby
outline: deep
---

# 3. Zahraniční osoby

V této sekci jsou představeny náležitosti práce se zahraničními osobami v ISSŘ. Přidání nebo úprava zahraniční osoby se provádí stejným způsobem jako u českých osob.

::: warning ZVÝŠENÁ POZORNOST
Ověření zahraničních osob systémem není možné, jelikož systém je napojený pouze na české registry. **Věnujte proto, prosíme, zvýšenou pozornost při vyplňování nebo úpravě zahraničních osob.** Po přidání osoby a jejím označení jako zahraniční je tato osoba v systému označená zeleně jako "ověřená", aby bylo možné této osobě vypravit dokument.
:::

Určení osoby nebo adresy jako zahraniční se týká vždy pouze dané položky. Je tedy možné tvořit a spravovat i české osoby se zahraničními adresami a zahraniční osoby s českými adresami.

## 3.1 Fyzická osoba

Označení FO jako zahraniční provedete zaškrtnutím checkboxu `Nelze ztotožnit / Zahraniční osoba`.

![](_page_19_Figure_4.jpeg)
![](_page_19_Picture_6.jpeg)

U zahraniční fyzické osoby je nutné vyplnit pole: **Jméno, Příjmení a Datum narození**. Další položky vyplňujete dle uvážení.

## 3.2 Fyzická osoba podnikající

Označení FOP jako zahraniční provedete zaškrtnutím stejného checkboxu.

![](_page_20_Figure_2.jpeg)
![](_page_20_Picture_4.jpeg)

U zahraniční FOP je nutné vyplnit pole: **Jméno, Příjmení a IČ**. Další položky vyplňujete dle uvážení.

## 3.3 Právnická osoba

Označení PO jako zahraniční provedete zaškrtnutím checkboxu `Nelze ztotožnit / Zahraniční společnost`.

![](_page_21_Figure_2.jpeg)
![](_page_21_Figure_4.jpeg)

U zahraniční PO je nutné vyplnit pole: **Název společnosti a IČ**. Další položky vyplňujete dle uvážení.

## 3.4 Oprávněná osoba právnické osoby

Některé právnické osoby mají určenou oprávněnou osobu, která jménem těchto právnických osob jedná. Přidává se v záložce `Oprávněná osoba`.

![](_page_22_Picture_0.jpeg)

Při přidání nebo úpravě oprávněné osoby k PO byla doplněna validace povinných údajů. Systém vyžaduje:
- jméno
- příjmení
- datum narození

![](_page_22_Picture_6.jpeg)

::: danger POVINNÉ ÚDAJE OPRÁVNĚNÉ OSOBY
Pokud je vyplněn alespoň jeden z těchto údajů, systém nedovolí potvrdit formulář, dokud nebudou doplněny všechny tři povinné údaje. Pokud není vyplněn žádný z údajů, formulář lze uložit – znamená to, že oprávněná osoba není zadána.
:::

Oprávněnou osobu je také možné následně ověřit pomocí tlačítka `Ověřit oprávněnou osobu` nebo označit jako osobu zahraniční pomocí checkboxu `Nelze ztotožnit/Zahraniční osoba`.

![](_page_23_Figure_5.jpeg)
""")

# ==========================================
# 04
# ==========================================
zapis_soubor("04-4-zpusob-komunikace.md", """---
title: 4. Způsob komunikace
outline: deep
---

# 4. Způsob komunikace

Nastavit nebo upravit způsob komunikace u osoby lze přímo na kartě osoby tlačítkem `Změnit způsob komunikace`.

![](_page_23_Picture_8.jpeg)

Při zvolení doručení **Poštou na adresu** systém použije pro vypravení údaje ze záložky Adresa pobytu / Místo podnikání / Adresa sídla. Při zvolení **Poštou na doručovací adresu** systém použije údaje ze záložky Doručovací adresa.

![](_page_24_Figure_1.jpeg)

Po zvolení těchto způsobů je třeba vybrat příslušnou **poštovní službu**.

::: warning KONTROLA POŠTOVNÍ SLUŽBY
Systém nekontroluje, jestli je poštovní služba vybrána adekvátně vzhledem k vyplněné adrese. **Věnujte zvýšenou pozornost při výběru způsobu komunikace i poštovní služby při vypravování do zahraničí.** V případě chybného výběru dojde k odmítnutí vypravení zásilky.
:::

![](_page_24_Figure_4.jpeg)

### Automatické nastavení způsobu komunikace

Způsob komunikace lze nastavit automaticky. Systém sám určí nejvhodnější způsob pro danou ověřenou osobu po kliknutí na tlačítko `Určit automaticky`.

![](_page_24_Figure_6.jpeg)

::: info AUTOMATICKÁ PRAVIDLA
1. U tuzemských PO, FOP a FO s datovou schránkou se nastaví komunikace datovou schránkou.
2. Pokud účastník nemá datovou schránku, ale je vyplněna doručovací adresa, nastaví se poštou na doručovací adresu.
3. Pokud účastník nemá ani datovou schránku, ani doručovací adresu, nastaví se poštou na adresu.
:::

![](_page_25_Figure_1.jpeg)

Pokud není vyplněna hodnota pro způsob komunikace nebo poštovní službu, zobrazí se upozornění pro uživatele.

![](_page_26_Figure_0.jpeg)

::: tip DOTČENÉ ORGÁNY (DO)
Vypravení Dotčeným orgánům je upraveno tak, že je vždy nastaveno automaticky systémem jako **výchozí vypravení do datové schránky**. Systém tedy nevypravuje DO interně, ale vždy primárně přes DS.
:::

![](_page_26_Figure_2.jpeg)
""")

# ==========================================
# 05
# ==========================================
zapis_soubor("05-5-podminky-vypraveni.md", """---
title: 5. Podmínky vypravení
outline: deep
---

# 5. Podmínky vypravení

Aby bylo možné dokument bez problémů vypravit, je potřeba splnit podmínky pro vypravení. Je nutné, aby osoba (adresát dokumentu) měla vyplněny následující údaje (pravidla platí i pro zahraniční subjekty):

* **Fyzická osoba (FO):** jméno, příjmení, datum narození, datová schránka / adresa dle způsobu komunikace.
* **Fyzická osoba podnikající (FOP):** jméno, příjmení, datum narození, IČ, datová schránka / adresa dle způsobu komunikace.
* **Právnická osoba (PO):** název, IČ, datová schránka / adresa dle způsobu komunikace.

::: warning CHYBĚJÍCÍ ÚDAJE
Pokud nejsou vyplněna všechna pole potřebná pro odeslání dokumentu, systém na tuto skutečnost upozorní:
1. Ikonou trojúhelníku s vykřičníkem v přehledu osob.
2. Textovým upozorněním v editačním dialogu osoby.
3. Během zpracování úkolu `Ukončit tvorbu dokumentu`.
:::

![](_page_27_Figure_5.jpeg)
![](_page_27_Picture_7.jpeg)
![](_page_28_Figure_0.jpeg)
""")

# ==========================================
# 06
# ==========================================
zapis_soubor("06-6-obsah-vypraveni.md", """---
title: 6. Obsah vypravení
outline: deep
---

# 6. Obsah vypravení

## 6.1 Vypravení hlavního dokumentu

U hlavního dokumentu je automaticky nastaven atribut `Odesílat` a atribut `Konvertovat`. To znamená, že je hlavní dokument **vždy vypraven a konvertován**. Výchozí nastavení nejsou zobrazené a nelze je měnit.

Počet stran hlavního dokumentu se zobrazuje na záložce `Hlavní dokument` pod řádkem Obsah.

![](_page_28_Picture_5.jpeg)

## 6.2 Vypravení příloh

Při vypravení vlastních dokumentů přes HKP i dalšími způsoby komunikace je k dispozici možnost odesílat přílohy. **Autorizovaná konverze vyžaduje soubor podepsaný kvalifikovaným elektronickým podpisem (mimo aplikaci).** Nepodepsané přílohy nebude možné přes HKP vypravit.

U příloh je výchozí atribut `Odesílat = ANO`, ale `Konvertovat = NE`. Bez změny nastavení budou přílohy vypraveny bez konverze. Nastavení lze změnit:

![](_page_29_Picture_2.jpeg)
![](_page_29_Figure_4.jpeg)
![](_page_30_Picture_0.jpeg)

::: warning POZOR NA KONVERZI U PŘÍLOH
Nelze nastavit `Konvertovat = ANO`, pokud je `Odesílat = NE`.
Pokud vypravení selže například z důvodu nevalidní přílohy nebo chyby konverze, zásilka se nevypraví a stav je evidován jako **Vrácená**. Přílohy, které si přejete konvertovat, je nutné vložit do dokumentu již předem podepsané.
:::

## 6.3 Počet listů pro vypravení

Počet listů je důležitý ukazatel pro vypravení HKP. V případě, že by byl tento limit překročen, dokument již nebude možné vypravit pomocí HKP a bude nutné použít ruční vypravení.

::: info OMEZENÍ POČTU LISTŮ PRO HKP
* Zásilky v rámci ČR a EU: **max 99 listů**
* Zásilky mimo EU: **max 8 listů**
*(Tisk probíhá oboustranně a 1 strana je vždy vyhrazena pro konverzní doložku)*
:::

*Poznámka k rozdílu:* Strana = jedna tištěná strana dokumentu. List = fyzický papír (obsahuje 2 strany).

Na záložce `Základní informace` je k dispozici pole **Počet listů zvoleného rozsahu zásilky**, které uvádí celkový počet fyzických listů. Hodnota zahrnuje: listy hlavního dokumentu + listy příloh + doložky.

![](_page_31_Picture_0.jpeg)
![](_page_31_Picture_6.jpeg)
![](_page_32_Figure_0.jpeg)
""")

# ==========================================
# 07
# ==========================================
zapis_soubor("07-7-vypraveni-do-zahranici.md", """---
title: 7. Vypravení do zahraničí
outline: deep
---

# 7. Vypravení do zahraničí

V této sekci jsou představeny náležitosti práce s možnostmi vypravení do zahraničí.

## 7.1 Způsob komunikace

Při zvolení způsobu `Poštou na adresu` nebo `Poštou na doručovací adresu` je třeba vybrat správnou poštovní službu. Pro vypravení do zahraničí je možné volit POUZE mezi službami:
* **Doporučená zásilka v EU**
* **Doporučená zásilka svět**

![](_page_32_Picture_5.jpeg)
![](_page_33_Picture_0.jpeg)

::: warning POŠTOVNÍ SLUŽBA PRO ZAHRANIČÍ
Systém nekontroluje, jestli je poštovní služba vybrána adekvátně k adrese. V případě chybného výběru služby (např. vnitrostátní služba pro cizí stát) dojde k odmítnutí vypravení zásilky!
:::

## 7.2 Zahraniční adresy

Ověření zahraničních adres systémem není možné. Věnujte proto zvýšenou pozornost při jejich vyplňování. Určení adresy jako zahraniční provedete zaškrtnutím checkboxu `Zahraniční adresa`.

![](_page_34_Picture_0.jpeg)

Zaškrtnutí checkboxu pozmění tuto záložku přidáním povinné položky **Stát**. Zahraniční adresa v řízení má tyto povinné položky: Stát, Obec a PSČ.

![](_page_34_Picture_2.jpeg)
![](_page_35_Picture_0.jpeg)
![](_page_35_Picture_2.jpeg)

## 7.3 Vypravování do zakázaných zemí

Systém ISSŘ kontroluje, zda je možné odeslat dokument prostřednictvím HKP do zadané země. Pokud má účastník adresu v zemi, kam Česká pošta nedoručuje, systém zobrazí upozornění a vytvoří se **ruční vypravení**, které je nutné provést mimo systém.

![](_page_36_Picture_0.jpeg)
""")

# ==========================================
# 08
# ==========================================
zapis_soubor("08-8-vypravovani-sluzbou-hkp.md", """---
title: 8. Vypravování službou HKP
outline: deep
---

# 8. Vypravování službou HKP

Doručování prostřednictvím Hybridní konverzní pošty (HKP) bylo dříve hrazeno MMR. **Pokud chce úřad nadále tuto službu využívat, je třeba uzavřít s Českou poštou smlouvu na vlastní náklady.**

V případě, že úřad nemá smlouvu a je zvolen způsob poštou, systém přepne na **ruční vypravení**. Pokud již úřad smlouvu má, je třeba kontaktovat Českou poštu, která MMR předá ID pro zavedení do ISSŘ. 

## 8.1 Ekonomické varianty poštovních služeb

Z nabídky poštovních služeb jsou dostupné čtyři varianty ekonomického zasílání, které šetří náklady úřadu.

::: tip DOSTUPNÉ EKONOMICKÉ VARIANTY
* Doporučená zásilka ekonomická – pouze s dodejkou
* Doporučená zásilka ekonomická – bez dodejky
* Úřední psaní ekonomické – do vl. rukou, nevracet vl. do schránky, uložit jen 10 dnů
* Úřední psaní ekonomické – do vl. rukou výhradně adresát, nevracet, uložit jen 10 dnů
:::

![](_page_37_Figure_1.jpeg)

Pokud není u osoby evidována datová schránka, systém automaticky jako výchozí nastaví ekonomickou variantu `Úřední psaní ekonomické – do vl. rukou, nevracet...`.

::: info EKONOMICKÝ VS. PRIORITNÍ REŽIM
Rozdíl je v ceně a v rychlosti doručení. Volba režimu **nemá vliv na právní účinky doručení**. Nové ekonomické varianty jsou dostupné pouze pro vypravení přes HKP (poštou na adresu).
:::
""")

# ==========================================
# 09
# ==========================================
zapis_soubor("09-9-rucni-vypraveni.md", """---
title: 9. Ruční vypravení
outline: deep
---

# 9. Ruční vypravení

Systém nabízí možnost **Ruční vypravení**, která se automaticky použije v případech, kdy nelze využít službu HKP.

::: info KDY SE POUŽIJE RUČNÍ VYPRAVENÍ
* Úřad nemá uzavřenou smlouvu s Českou poštou (od 1. 2. 2026).
* Dokument překračuje limit počtu stran (99 pro EU / 8 mimo EU).
* Zásilka směřuje do "zakázané" země.
:::

Na záložce Vypravení je stav "Čeká se na vypravení". Uživatel musí kliknout na `Odeslat`.

![](_page_38_Picture_4.jpeg)
![](_page_38_Picture_6.jpeg)

V dialogovém okně lze zadat datum odeslání (povinné) a podací číslo (nepovinné).

![](_page_38_Picture_8.jpeg)
![](_page_39_Figure_0.jpeg)

Po odeslání se stav změní na "Vypraveno" a zpřístupní se tlačítko `Nahrát doručenku`. Zde se zadává datum doručení a nahrává se fyzický soubor doručenky.

![](_page_39_Picture_2.jpeg)
![](_page_39_Picture_6.jpeg)
![](_page_40_Picture_0.jpeg)
![](_page_40_Picture_2.jpeg)

::: warning POZOR
Způsobem Ruční vypravení systém **nevypravuje dokument automaticky**. Úředník musí dokument fyzicky stáhnout a vypravit ho mimo ISSŘ (fyzickou poštou nebo jiným systémem).
:::

## 9.1 Překročení délky dokumentu

Pokud dokument přesáhne povolený limit (99 / 8 stran), systém změní způsob na "ruční vypravení". Uživatel je na to jasně upozorněn v rozhraní.

![](_page_41_Figure_2.jpeg)

## 9.2 Vypravení do zakázané země

Pokud má účastník řízení uvedenou adresu v zemi, kam Česká pošta nedoručuje, dokument se neodešle přes HKP, ale vytvoří se ruční vypravení.

![](_page_41_Picture_6.jpeg)
""")

# ==========================================
# 10
# ==========================================
zapis_soubor("10-10-tisk-adres-na-obalky.md", """---
title: 10. Tisk adres na obálky
outline: deep
---

# 10. Tisk adres na obálky

V detailu dokumentu v záložce `Vypravení` je možné zobrazit adresy osob v podobě, kterou lze snadno zkopírovat za účelem tisku adres na obálky. Tlačítko je viditelné pouze, pokud je součástí alespoň jedno ruční vypravení.

Uživatel si může zobrazit adresy všech osob pomocí ikony `Adresní štítky` v horní části obrazovky.

![](_page_42_Figure_3.jpeg)

Adresu konkrétní osoby je možné zobrazit přímo v detailu osoby pomocí tlačítka `Adresní štítek`.

![](_page_43_Picture_0.jpeg)
![](_page_43_Figure_1.jpeg)

Adresu jednoduše zkopírujete klávesovou zkratkou `CTRL+C`.
""")

# ==========================================
# 11
# ==========================================
zapis_soubor("11-11-vypraveni-prevzeti-osobne.md", """---
title: 11. Vypravení – převzetí osobně
outline: deep
---

# 11. Vypravení – převzetí osobně

Dokument vytvořený v ISSŘ lze doručit osobně. U daného účastníka je potřeba nastavit způsob komunikace `Osobně`.

![](_page_44_Picture_0.jpeg)

Při převzetí dokumentu je vhodné vyhotovit protokol o převzetí. Toto potvrzení následně vložíte do systému kliknutím na `Nahrát doručenku`.

![](_page_44_Picture_2.jpeg)

Vyplňte datum doručení a vložte dokument osvědčující osobní převzetí.

![](_page_44_Picture_4.jpeg)

Stav dokumentu se po doplnění doručenky změní na **Doručeno**. Jak datum, tak samotnou doručenku je možné opakovaně upravovat/vyměnit pomocí stejného tlačítka.

![](_page_45_Picture_0.jpeg)
![](_page_45_Picture_2.jpeg)
""")

# ==========================================
# 12
# ==========================================
zapis_soubor("12-12-vypraveni-vyhlaskou.md", """---
title: 12. Vypravení vyhláškou
outline: deep
---

# 12. Vypravení vyhláškou

Dokument vytvořený v ISSŘ je možné doručit účastníkům vyhláškou – vyvěšením na úřední desce úřadu (používá se u záměrů s více než 30 účastníky nebo u osob neznámého pobytu).

![](_page_45_Picture_6.jpeg)

Pro nastavení data vyvěšení využijte tlačítko `Datum vyvěšení`. Otevře se dialog pro zadání data. Po potvrzení se datum aplikuje na všechna vypravení doručovaná vyhláškou u daného dokumentu a stav se změní na **Vypraveno**.

![](_page_46_Figure_0.jpeg)
![](_page_46_Figure_2.jpeg)
![](_page_46_Picture_4.jpeg)

Následně se tlačítko skryje a zpřístupní se akce `Datum sejmutí`.

![](_page_47_Figure_0.jpeg)

Po kliknutí na tlačítko `Datum sejmutí` se otevře dialog, ve kterém můžete:
1. **Upravit datum vyvěšení** (musí předcházet datu sejmutí).
2. **Vyplnit datum sejmutí** (povinný údaj).
3. **Nahrát doručenku** (povinný dokument osvědčující datum vyvěšení a sejmutí).

![](_page_47_Picture_5.jpeg)
![](_page_48_Picture_0.jpeg)

Stav vypravení se po dokončení změní na **Doručeno**. Všechny tyto údaje lze opakovaně upravovat, změny se logují do auditu.

![](_page_48_Picture_3.jpeg)
""")

# ==========================================
# 13
# ==========================================
zapis_soubor("13-13-opetovne-vypraveni-dokumentu.md", """---
title: 13. Opětovné vypravení dokumentu
outline: deep
---

# 13. Opětovné vypravení dokumentu

Opětovné vypravení dokumentu se používá, když původní vypravení z nějakého důvodu selhalo, došlo ke změně způsobu komunikace/adresy u účastníka, nebo je přidán zcela nový účastník řízení.

## 13.1 Původní vypravení selhalo

V detailu odeslaného dokumentu klikněte v pravém horním rohu na tlačítko `Odeslat dokument jednotlivě`.

![](_page_49_Figure_3.jpeg)

Vyberte účastníka, kterému chcete dokument znovu odeslat, a potvrďte.

![](_page_49_Figure_5.jpeg)
![](_page_50_Figure_0.jpeg)

Na záložce Vypravení se objeví nový záznam o vypravení.

![](_page_50_Picture_2.jpeg)

## 13.2 Vypravení novému účastníkovi

1. Přidejte nového účastníka do řízení a proveďte jeho ověření (vč. nastavení komunikace).
2. Přejděte na záložku `Dokumenty` a otevřete detail již odeslaného dokumentu.
3. Klikněte na `Odeslat dokument jednotlivě`.
4. Vyberte nového účastníka a potvrďte. Dokument bude předán do výpravny.

![](_page_51_Figure_0.jpeg)
![](_page_51_Figure_2.jpeg)
![](_page_51_Figure_4.jpeg)
![](_page_52_Figure_2.jpeg)
![](_page_52_Figure_4.jpeg)
![](_page_53_Picture_0.jpeg)
""")

# ==========================================
# 14
# ==========================================
zapis_soubor("14-14-dorucenky.md", """---
title: 14. Doručenky
outline: deep
---

# 14. Doručenky

V ISSŘ se doručenky evidují odlišně podle způsobu vypravení zásilky:

* **Hybridní pošta (HKP):** Doručenky jsou skenovány Českou poštou a automaticky nahrávány do ISSŘ prostřednictvím spisové služby.
* **Datová schránka:** Po doručení je vygenerován soubor ZFO, který se do ISSŘ načte zcela automaticky jako doručenka.
* **Ruční vypravení / Osobní doručení:** Uživatel musí doručenku ručně nahrát tlačítkem `Nahrát doručenku`. Již nahranou doručenku nelze smazat, pouze vyměnit za nový soubor.
* **Doručení vyhláškou:** Po zadání data vyvěšení se zpřístupní tlačítko `Datum sejmutí`, přes které se doručenka nahrává.
* **Interní vypravení:** U interního předávání se doručenky neevidují.

## 14.1 Okamžik doručení u HKP a ručního vypravení

Systém umožňuje evidovat tzv. **Okamžik doručení**, který se může lišit od systémového data doručení uvedeného na doručence (např. v případech fikce doručení dle právních předpisů).

U vypravení přes HKP se datum zadává přímo přes ikonu `Okamžik doručení` v přehledu.

![](_page_54_Figure_7.jpeg)
![](_page_54_Figure_9.jpeg)

U Ručního vypravení zadání probíhá přímo v dialogu `Nahrát doručenku`.

![](_page_55_Picture_2.jpeg)
![](_page_55_Picture_4.jpeg)

::: info POUZE EVIDENČNÍ CHARAKTER
Zadané datum okamžiku doručení je čistě evidenční a nepřenáší se do žádných externích systémů. Můžete ho libovolně opakovaně upravovat (změny se logují do auditu).
:::

![](_page_56_Picture_0.jpeg)
""")

# ==========================================
# 15
# ==========================================
zapis_soubor("15-15-stav-vypraveni.md", """---
title: 15. Stav vypravení
outline: deep
---

# 15. Stav vypravení

## 15.1 Jednotlivé stavy vypravení

Každé vypravení může být v jednom z těchto stavů:
* **Čeká na vypravení:** Dokument je k vypravení připraven, ale zatím neodešel.
* **Vypraveno:** Dokument byl odeslán adresátovi, ale ještě nebyl doručen.
* **Doručeno čeká na doručenku:** Dokument byl doručen, ale eSSL/systém zatím fyzickou doručenku nezpracoval (typické u HKP).
* **Doručeno:** Dokument doručen a doručenka/protokol je evidována.
* **Nedoručeno zpracováno:** Dokument nebyl doručen, ale situace už byla úředníkem vyřešena (např. opakovaným doručením).
* **Stornováno:** Vypravení bylo před doručením zastaveno (např. omylem založené vypravení).
* **Vráceno:** Typické u HKP nebo pošty. Evidováno s doplňkovými stavy:
  * *adresát neznámý* (neexistuje schránka/jméno)
  * *adresát se odstěhoval*
  * *nepřijato* (odmítnuto adresátem)
  * *nevyžádáno* (nevyzvednuto v úložní době)
  * *adresa nedostatečná*
  * *jiný důvod (ověřeno)*
  * *jiný důvod (neověřeno)*

## 15.2 Tlačítko pro ruční synchronizaci

V záložce `Vypravení` klikněte na tlačítko `Ruční synchronizace stavu vypravení` pro vynucení okamžité aktualizace stavů od eSSL/Pošty.

## 15.3 Podací číslo

U HKP dokumentů naleznete v poli **Podací číslo** interaktivní odkaz na sledování zásilky na webu České pošty. U ručního doručení vyplňujete toto číslo manuálně.

## 15.4 Řazení a filtrování

V tabulkovém zobrazení vypravení lze záznamy řadit a filtrovat. To obrovsky usnadňuje kontrolu nedoručených zásilek u řízení s desítkami účastníků.

![](_page_57_Picture_12.jpeg)
""")

# ==========================================
# 16
# ==========================================
zapis_soubor("16-16-notifikace.md", """---
title: 16. Notifikace
outline: deep
---

# 16. Notifikace

V ISSŘ lze nastavit notifikaci upozorňující na události při vypravení dokumentu. Zvolit si můžete aplikační (zvoneček) i e-mailová upozornění.

![](_page_57_Picture_17.jpeg)
![](_page_58_Figure_1.jpeg)

## 16.1 Notifikace o selhání vypravení

Pokud dokument přejde do chybového stavu **vráceno – jiný důvod (neověřeno)**, systém okamžitě odesílá notifikaci zpracovateli dokumentu i vedoucímu příslušného úřadu.

## 16.2 Notifikace o doručení všem adresátům

Lze si nastavit upozornění pro moment, kdy u daného dokumentu konečně "zezelenají" (stav doručeno) úplně všechna vypravení pro všechny účastníky v rozdělovníku.
""")

# ==========================================
# 17
# ==========================================
zapis_soubor("17-17-konkretni-duvody-nevypraveni.md", """---
title: 17. Konkrétní důvody nevypravení dokumentu
outline: deep
---

# 17. Konkrétní důvody nevypravení dokumentu

Následující sekce shrnuje hlavní důvody, proč nemusí dojít k úspěšnému vypravení dokumentu (typicky skrze systém spadne do stavu `vráceno jiný důvod (neověřeno)`).

## 17.1 Chyby ve formě dokumentu (HKP)

::: warning CHYBÍ KVALIFIKOVANÝ PODPIS
Pro vypravení přes HKP (ale i konvertované přílohy) musí být hlavní dokument podepsán **kvalifikovaným certifikátem**. Přílohy se musí vkládat již podepsané. Nesprávně podepsaný dokument navíc *odejde* do Datových schránek (DS totiž úroveň podpisu nekontroluje), ale *zasekne se* u České pošty.
:::

::: info VERIFIKÁTOR PODPISŮ
Formu podpisu ověříte pomocí nástroje **Verifikátor podpisů**.
![](_page_59_Figure_7.jpeg)
:::

**Další formální chyby:**
* **Strany v jiném než A4 formátu:** HKP neumí vytisknout A3 výkresy atd.
* **Nevhodný formát PDF:** Je podporován pouze standard `PDF/A-1`.
* **Překročení velikosti souboru:** HKP = max 15 MB, Datové schránky = max 100 MB.
* **Překročení limitu počtu listů:** Max 99 (EU) nebo 8 (mimo EU).
* **Vypravování do zakázaných zemí.**
* **Úřad nemá uzavřenou smlouvu s Českou poštou.**

## 17.2 Nedostatečně nebo chybně vyplněné údaje účastníků

* **Neúplná adresa:** Údaje účastníka ze záměru nemají kompletní adresu (chybí PSČ atd.). Doporučujeme vždy přes tlačítko `Zkopírovat ověřená data do řízení` překlopit čistá data ze základních registrů.
* **Nesprávné ID datové schránky:** Stejný problém jako u adresy – pokud ID zadal účastník ručně špatně do portálu stavebníka, je v systému chybně. Přepište ho přeskopírováním z registrů.
* **Nesprávná kombinace druhu zásilky a poštovní služby:** Byla vybrána tuzemská poštovní služba pro osobu, která má zaškrtnutou Zahraniční adresu. U zahraničních adres musíte z roletky vybrat "Doporučená zásilka EU/Svět".
""")

# ==========================================
# 18
# ==========================================
zapis_soubor("18-18-podpora.md", """---
title: 18. Podpora
outline: deep
---

# 18. Podpora

::: info REKLAMACE DORUČENEK
V případě, že u doručeného dokumentu není do **10 dnů** k dispozici doručenka, obraťte se na podporu **digitalizace@mmr.gov.cz** s žádostí o reklamaci nedodání doručenky u České pošty. 

Uveďte prosíme vždy PID nebo číslo jednací předmětného dokumentu a adresáta, u kterého doručenka chybí.
:::

**Další zdroje:**
Další informace k vypravování a poštovním službám je možné nalézt v sekci FAQ na oficiálních stránkách MMR v sekci Odesílání dokumentů.
""")

print("✅ Všechny soubory příručky (00 až 18) byly úspěšně vytvořeny s čistým VitePress kódováním!")