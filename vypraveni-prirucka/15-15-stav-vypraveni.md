---
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
