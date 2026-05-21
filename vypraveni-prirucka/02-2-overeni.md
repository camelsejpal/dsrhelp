---
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
