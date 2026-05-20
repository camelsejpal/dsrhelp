---
title: 15. Stav vypravení
---

# 15. Stav vypravení

## 15.1 Jednotlivé stavy vypravení

Každé vypravení může být v jednom z následujících stavů:
- **Čeká na vypravení:** jedná se o stav, kdy ještě nebyl dokument adresátovi vypraven, ale již je k vypravení připraven.
- **Vypraveno:** dokument již byl adresátovi vypraven, ale stále nebyl doručen.
- **Doručeno čeká na doručenku:** dokument byl úspěšně doručen, ale v systému zatím není doručenka evidována. Může se jednat například o dokumenty vypravené HKP, u kterých se doručenka nahraje do systému později.
- **Doručeno:** dokument byl adresátovi úspěšně doručen a v systému je již evidována doručenka nebo jiný záznam o doručení (protokol o osobním předání, záznam o svěšení z úřední desky atp.)
- **Nedoručeno zpracováno:** dokument nebyl z nějakého důvodu doručen a tato situace již byla zpracována/zaevidována, například: byla vrácena obálka a bylo vydáno rozhodnutí o opakovaném doručení.
- **Stornováno:** vypravení dokumentu bylo zastaveno/stornováno před samotným doručením. Stornování vypravení může být například z důvodu omylem založeného vypravení nebo rozhodnutím nahradit dokument jeho novou verzí, která bude následně vypravena místo stornovaného dokumentu.
- **Vráceno:** stav Vráceno se týká převážně zásilek vypravených pomocí HKP a ručního vypravení a je v systému ISSŘ evidován s několika dalšími dodatečnými stavy:
  - **adresát neznámý:** Obvykle se jedná o situaci, kdy taková osoba/adresát na dané adrese vůbec neexistuje, například nemá na adrese poštovní nebo jinou doručovací schránku.
  - **adresát se odstěhoval bez udání adresy:** Jedná se o případ, kdy osoba, které bylo vypravováno na adrese dříve pobývala, ale již zde nebydlí a neudala novou adresu. Zásilku tak není možné ani přeposlat.
  - **nepřijato:** Adresát (nebo jeho oprávněná osoba) odmítl zásilku převzít.
  - **nevyžádáno:** Zásilka nebyla během prvotního pokusu o doručení doručena a následně byla uložena k vyzvednutí na poště. Adresát si ji ale v určené lhůtě nevyzvedl.
  - **adresa nedostatečná:** Adresa pro doručení je neúplná nebo nepřesná, takže doručení nebylo možné.
  - **jiný důvod (ověřeno):** Zásilka byla vrácena z jiného důvodu než z ostatních uvedených. Tento důvod byl ověřen – potvrzen. Mohlo se jednat například o chybu na straně doručovatele nebo specifickou situaci doloženou dokladem.
  - **jiný důvod (neověřeno):** Zásilka byla vrácena z jiného důvodu než z ostatních uvedených. Tento důvod ale nebyl spolehlivě ověřen – informace od doručovatele chybí, nebo jsou nejednoznačné či nejasné.

## 15.2 Tlačítko pro ruční synchronizaci stavu vypravení

V záložce Vypravení každého dokumentu je dostupné tlačítko `Ruční synchronizace stavu vypravení`. Tato funkcionalita umožňuje aktualizaci všech údajů v záložce vypravení u všech adresátů.

Po načtení synchronizace doporučujeme zavřít daný panel (pomocí tlačítka X) a znovu otevřít příslušné číslo jednací. Poté přejít do záložky "Vypravení", kde se již zobrazí aktuální stav.

## 15.3 Podací číslo

V ISSŘ je u dokumentů vypravených prostřednictvím HKP dostupná informace o podacím čísle zásilky, včetně interaktivního odkazu na webové stránky České pošty pro sledování zásilky. Tento údaj naleznete u každého účastníka v záložce "Vypravení" v poli "Podací číslo".

Podací číslo je také možné zadat v rámci evidování doručenky v případě ručního vypravení.

## 15.4 Řazení a filtrování v tabulkovém režimu vypravení

V tabulkovém zobrazení vypravení lze řadit jednotlivé položky vypravení vzestupně či sestupně a filtrovat, což usnadňuje kontrolu, u kterých účastníků řízení ještě nedošlo k doručení. Stejně jako v jiných případech, lze individuálně upravit zobrazení a pořadí sloupců dle Vašich potřeb.

Jedná se o položky Osoba, Doručenka, Vypravený hlavní dokument, Akce nelze logicky řadit. Prázdná pole se vždy zobrazují na konci seznamu.

![](_page_57_Picture_12.jpeg)
