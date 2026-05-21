---
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
