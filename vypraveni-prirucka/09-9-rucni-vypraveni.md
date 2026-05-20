---
title: 9. Ruční vypravení
---

# 9. Ruční vypravení

Systém nabízí také možnost "Ruční vypravení", která se automaticky použije v případech, kdy nelze využít službu Hybridní konverzní pošty (HKP). Týká se následujících situací:
- **Úřad nemá uzavřenou smlouvu s Českou poštou (od 1. 2. 2026).**
- **Dokument překračuje limit počtu stran stanovený Českou poštou pro vypravení. Limity počtů stran dokumentů pro vypravení HKP jsou 99 listů pro zásilky v rámci ČR a EU nebo 8 listů pro zásilky mimo EU, přičemž 1 strana je vyhrazena pro konverzní doložku.**
- **Zásilka směřuje do země, kam Česká pošta nedoručuje.**

![](_page_38_Picture_4.jpeg)

Na záložce "Vypravení" je pole "Způsob doručení" automaticky nastaveno na "Ruční vypravení" a stav vypravení je "Čeká se na vypravení". Uživatel má možnost vyplnit údaje o odeslání dokumentu pomocí tlačítka `Odeslat`.

![](_page_38_Picture_6.jpeg)

V dialogovém okně "Odeslat" lze zadat datum odeslání a podací číslo. Datum odeslání je povinný údaj a nesmí předcházet datumu předání k vypravení. Podací číslo není povinné a musí obsahovat 13 alfanumerických znaků.

![](_page_38_Picture_8.jpeg)
![](_page_39_Figure_0.jpeg)

Po zadání data odeslání se stav vypravení automaticky změní na "Vypraveno" a uživatel má možnost vyplnit údaje o doručení dokumentu pomocí tlačítka `Nahrát doručenku`.

![](_page_39_Picture_2.jpeg)

V dialogovém okně "Nahrát doručenku" lze zadat datum doručení a nahrát soubor doručenky. Datum doručení je povinný údaj a nesmí předcházet datumu předání k vypravení. Nahrání doručenky je povinné pole.

![](_page_39_Picture_6.jpeg)
![](_page_40_Picture_0.jpeg)

Po nahrání doručenky se stav vypravení automaticky změní na "Doručeno".

![](_page_40_Picture_2.jpeg)

Uživatel má možnost zadaná data v případě potřeby opravit opětovným kliknutím na tlačítko `Nahrát doručenku`. Již nahranou doručenku však nelze smazat, pouze vyměnit za nový soubor. Tato funkcionalita umožňuje úředníkům evidovat ruční odeslání dokumentu přímo v ISSŘ, včetně všech potřebných údajů o jeho doručení.

Je důležité vědět, že způsobem Ruční vypravení systém nevypravuje dokument automaticky. Úředník musí dokument vypravit vlastním způsobem (dokument stáhnout, vložit a vypravit skrze systém, který je k tomuto účelu v rámci úřadu využíván, nebo dokument konvertovat do listinné podoby a vypravit fyzicky poštou).

Pro dokumenty vypravené pomocí ručního vypravení disponuje systém také funkcí Okamžik doručení. Tato funkce umožňuje úředníkovi zadat vlastní datum okamžiku doručení, které se může lišit od systémového data doručení uvedeného na doručence, například v případech fikce doručení dle právních předpisů.

## 9.1 Vypravení v případě překročení délky dokumentu

Funkcionalita zajišťuje ruční vypravení dokumentů překračující maximální povolenou délku mimo systém.

Systém automaticky kontroluje počet stran dokumentu při odesílání prostřednictvím Hybridní konverzní pošty (HKP). Pokud dokument přesáhne povolený limit pro vypravení (tj. 99 stran pro zásilky v rámci ČR a EU nebo 8 stran pro zásilky mimo EU, přičemž 1 strana je vyhrazena pro konverzní doložku), systém změní způsob vypravení na "ruční vypravení".

Uživatel je na tuto skutečnost upozorněn:

![](_page_41_Figure_2.jpeg)

## 9.2 Vypravení do zakázané země

Seznam zakázaných zemí spravuje globální administrátor MMR v samostatném administračním rozhraní.

Systém kontroluje, zda je možné odeslat dokument prostřednictvím Hybridní konverzní pošty (HKP) do zadané země. Pokud má účastník řízení uvedenou adresu v zemi, kam Česká pošta nedoručuje, systém zobrazí upozornění "Do dané země není možné odesílat" a dokument se neodešle prostřednictvím HKP, ale vytvoří se ruční vypravení, které je nutné provést mimo systém.

![](_page_41_Picture_6.jpeg)
