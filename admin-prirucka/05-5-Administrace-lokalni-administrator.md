---
title: 5. Administrace – lokální administrátor
outline: deep
---

# 5. Administrace – lokální administrátor

Pro přechod do administrace uživatel klikne na tlačítko `Administrace` v levém dolním rohu obrazovky.

![](_page_6_Picture_5.jpeg)

---

## 5.1 Návod pro lokálního administrátora SÚ/DO při prvním přístupu do systému

### 5.1.1 Vyplnění bankovního spojení úřadu

1. V menu vlevo dole klikněte na tlačítko `Administrace`.
2. Zvolte položku `Úřady` – v menu uvidíte vlastní organizaci. 
3. Kliknutím na záznam v seznamu se otevře vpravo okno s detailními informacemi.
4. Klikněte na tlačítko `Upravit` a vyplňte bankovní spojení.

![](_page_7_Figure_0.jpeg)

5. Po vyplnění bankovního spojení informace uložte stiskem tlačítka `Uložit` vpravo nahoře.

::: info POZNÁMKA K BANKOVNÍMU SPOJENÍ
Bankovní spojení je důležité pro tvorbu platebních příkazů. Bankovní účet uveďte v plné formě včetně kódu banky.
:::

![](_page_8_Figure_3.jpeg)

### 5.1.2 Nastavení rolí zaměstnancům stavebního úřadu

1. V menu administrace přejděte pod záložku `Adresářová struktura` a do podmenu `Uživatelé`.
2. V seznamu klikněte na vybraného uživatele. Otevře se vám vpravo okno s detailními informacemi.
3. Klikněte na černé tlačítko `Upravit` na řádku s atributem **Role**.

![](_page_9_Figure_0.jpeg)

4. Ve vyskakovacím okně vyberte z nabídky příslušné role. Zaměstnanci přidejte roli `Referent`, `Vedoucí zaměstnanec` nebo `Zaměstnanec sekretariátu`. 
5. K těmto lze navíc přidat roli `Oprávnění potvrzení platby` nebo `Podpisové oprávnění` (blíže k rolím viz kapitola 5.3). Roli `JIP-KAAS role` ponechte uživateli vždy zaškrtnutou.

![](_page_10_Picture_4.jpeg)

6. Roli přidělíte kliknutím na tlačítko `Potvrdit` ve vyskakovacím okně.

![](_page_10_Picture_6.jpeg)

7. Role je přidělena, na detailu uživatele nyní vidíte novou roli.

![](_page_11_Picture_4.jpeg)

::: warning POVINNOST PRO VŠECHNY ZAMĚSTNANCE
Tyto kroky je potřebné vykonat pro všechny zaměstnance úřadu jednotlivě. Každý uživatel musí mít kromě `JIP-KAAS role` přidělenou i konkrétní roli (např. Referent). Uživatel s nepřidělenou rolí nebude moci v systému vykonávat svoji práci.
:::

### 5.1.3 Nastavení rolí zaměstnancům dotčeného orgánu

1. V menu administrace přejděte pod záložku `Adresářová struktura` a do podmenu `Uživatelé`.
2. V seznamu klikněte na vybraného uživatele. Otevře se vpravo okno s detailními informacemi, kde klikněte na černé tlačítko `Upravit` na řádku s atributem **Role**.

![](_page_12_Picture_3.jpeg)

3. Ve vyskakovacím okně vyberte z nabídky roli. Zaměstnanci přidejte roli `Referent`, `Vedoucí zaměstnanec` nebo `Zaměstnanec sekretariátu`. Roli `JIP-KAAS role` ponechte uživateli zaškrtnutou.

![](_page_13_Figure_3.jpeg)
![](_page_14_Picture_0.jpeg)
![](_page_14_Picture_1.jpeg)
![](_page_14_Picture_2.jpeg)

4. Roli přidělíte kliknutím na tlačítko `Potvrdit` ve vyskakovacím okně.

![](_page_14_Picture_4.jpeg)

5. Role je přidělena, na detailu uživatele vidíte novou roli.

![](_page_15_Picture_2.jpeg)

::: warning POVINNOST PRO DO
Stejně jako u stavebního úřadu je potřeba tyto kroky vykonat pro všechny zaměstnance dotčeného orgánu jednotlivě. Uživatel s nepřidělenou rolí nebude moci pracovat.
:::

### 5.1.4 Vyplnění osoby pro příjem dokumentů

1. Přejděte do `Administrace` -> položka `Úřady`, vyberte vlastní organizaci a rozklikněte její detail.
2. Na detailu vpravo nahoře klikněte na tlačítko `Upravit`.
3. V editačním režimu nastavte doposud nevyplněné pole **Příjem dokumentů** na jednoho z uživatelů úřadu. Systém v rozevíracím seznamu nabídne na výběr pouze ty uživatele, kteří mají potřebnou roli pro příjem.
4. Po výběru uživatele vpravo nahoře klikněte na tlačítko `Uložit`.

![](_page_18_Picture_4.jpeg)

5. Po uložení ověřte, že je správný uživatel pro příjem dokumentů skutečně nastaven.

![](_page_19_Picture_3.jpeg)
![](_page_19_Picture_4.jpeg)
![](_page_19_Figure_5.jpeg)

::: danger KRITICKÉ NASTAVENÍ: PŘÍJEM DOKUMENTŮ
Bez nastavení výchozího uživatele pro příjem dokumentů nebudou dokumenty ze spisové služby postoupeny na správný úřad v ISSŘ.
:::

---

## 5.2 Návod pro lokálního administrátora kompozitního úřadu (kompozitu)

Kompozitní úřad je nadřazenou organizací SÚ, DO nebo jiných kompozitních úřadů. Kompozitní úřad přiřazuje nově přihlášené uživatele k příslušnému úřadu, který pod něj spadá. Úkolem lokálního administrátora kompozitního úřadu je tedy změnit organizaci a roli nově přihlášenému uživateli do systému.

Lokální administrátor kompozitu může dále v případě potřeby editovat údaje podřízených úřadů. Roli lokálního administrátora kompozitu může přidělit globální admin MMR, nebo může být získána od již existujícího lokálního administrátora kompozitu.

### 5.2.1 Přiřazení nově přihlášeného uživatele na příslušný SÚ/DO

1. Lokální administrátor kompozitního úřadu přejde do administrace kliknutím na ikonu ozubeného kolečka v levém dolním rohu.

![](_page_20_Figure_8.jpeg)

2. V menu přejde do `Adresářová struktura` a následně vybere `Uživatelé`. V přehledu jsou zobrazeni uživatelé kompozitního úřadu a jemu podřízených úřadů.

![](_page_21_Figure_3.jpeg)

3. Vybere uživatele z přehledu a klikne na tlačítko `Upravit` u atributu **Organizace**.

![](_page_21_Figure_5.jpeg)

4. Následně ve vyskakovacím okně vybere podřízenou organizaci, do které chce uživatele přesunout. Uživatele tak odebere z organizace kompozitního úřadu.

![](_page_22_Picture_4.jpeg)

5. Změny potvrdí kliknutím na tlačítko `Potvrdit`.

![](_page_22_Figure_7.jpeg)

6. Následně klikne na tlačítko `Upravit` u atributu **Role**.

![](_page_23_Figure_4.jpeg)

7. Nastaví uživateli roli `JIP-KAAS stavebního úřadu` nebo `JIP-KAAS dotčeného orgánu` podle typu podřízené organizace. Pokud má být uživatel lokálním administrátorem dané podřízené organizace, nastaví mu také druhou roli `Lokální administrátor SÚ/DO`. 

::: info SPRÁVA PODŘÍZENÉ ORGANIZACE
O následnou správu dané podřízené organizace se již stará nově určený lokální administrátor příslušné organizace.
:::

![](_page_23_Figure_6.jpeg)

### 5.2.2 Zobrazení úřadů

Administrátor přejde do administrace a v menu klikne na položku `Úřady`. Následně vidí svůj úřad a všechny podřízené úřady.

::: tip SPRÁVNÉ NASTAVENÍ IČ
Správným nastavením je, když je IČ vyplněno na úrovni kompozitního úřadu a naopak je IČ nevyplněno pro podřízené úřady SÚ a DOSS. Lokální administrátor kompozitu vidí uživatele podřízených organizací, které nemají vyplněné IČ. IČ podřízených úřadů se automaticky propisuje z IČ nastaveného u kompozitu.
:::

![](_page_24_Picture_8.jpeg)

### 5.2.4 Zobrazit přehled úřadů

Uživatel v postranním menu klikne na `Úřady`. Běžný lokální administrátor vidí v přehledu pouze svůj úřad. Lokální administrátor kompozitu vidí v přehledu všechny podřízené úřady.

![](_page_25_Figure_3.jpeg)

### 5.2.5 Akce detailu úřadu

#### Načíst detail úřadu znovu
Uživatel přejde na detail úřadu a klikne na tlačítko `Načíst znovu`.

![](_page_25_Picture_7.jpeg)

#### Upravit úřad
Uživatel přejde na detail úřadu a klikne na tlačítko `Upravit`. Detail se otevře ve formě formuláře s předvyplněnými aktuálními údaji. Uživatel údaje upraví a změny uloží kliknutím na příslušné tlačítko.

![](_page_25_Figure_10.jpeg)

---

## 5.3 ISSŘ Role

ISSŘ role slouží pro nastavení přístupových práv k jednotlivým částem systému. Níže je přehled uživatelských rolí existujících v systému a jejich oprávnění:

### 5.3.1 Administrátor (globální administrátor) <Badge type="danger" text="Globální Admin" />
* Všechny funkce systému včetně administračních bez omezení na domovský úřad.

### 5.3.2 Lokální administrátor SÚ/DO <Badge type="warning" text="Lokální Admin SÚ/DO" />
**Základní oprávnění:**
* Ztotožňování osob, parcel a stavebních objektů.
* Čtení listů vlastnictví a BPP balíčků.
* Pečetění BPP balíčků (ověření dokumentace) – *pouze pro lokálního administrátora SÚ*.

**Správa domovského úřadu a uživatelů:**
* Čtení a zápis adresy, kontaktů, bankovního spojení.
* Určení uživatele pro příjem dokumentů.
* Čtení, zápis a přiřazování rolí.

**Evidence a Agendy:**
* **Dokumenty:** Správa dokumentů domovského úřadu, změna zpracovatele, podepisování, schvalování, příjem, nastavení nabytí právní moci, storno.
* **Platební příkazy:** Čtení příkazů domovského úřadu.
* **Řízení:** Správa řízení, změna zpracovatele, ukončení a otevření řízení.
* **Záměry:** Čtení, zápis, zneplatnění záměru, přidělení IČS navrhovanému objektu, přepis do evidence stavebních objektů, tvorba BPP balíčku.
* **Stavební objekty:** Čtení, zápis, přidělení IČS, změna stavu objektu.

### 5.3.3 Lokální administrátor kompozitu <Badge type="warning" text="Lokální Admin Kompozitu" />
**Správa domovského úřadu a uživatelů:**
* Čtení a zápis adresy, kontaktů, bankovního spojení.
* Určení uživatele pro příjem dokumentů.
* Čtení, zápis a přiřazování rolí.

::: info HLAVNÍ ÚLOHA KOMPOZITU
Lokální administrátor kompozitu má hlavní úlohu rozřazovat uživatele do podřízených úřadů.
:::

### 5.3.4 Vedoucí zaměstnanec SÚ/DO <Badge type="info" text="Vedoucí" />
**Základní oprávnění:**
* Ztotožňování osob, parcel a staveb.
* Čtení listů vlastnictví a BPP balíčků.
* Pečetění BPP balíčků (ověření dokumentace) – *pouze pro vedoucího zaměstnance SÚ*.

**Evidence a Agendy:**
* **Dokumenty:** Správa dokumentů, změna zpracovatele, podepisování, schvalování a příjem dokumentů.
* **Platební příkazy:** Čtení platebních příkazů domovského úřadu.
* **Řízení:** Správa řízení, změna zpracovatele, ukončení řízení, správa přístupu.
* **Záměry:** Čtení, zápis, přidělení IČS navrhovanému objektu, přepis do stavebních objektů.
* **Stavební objekty:** Čtení, zápis, přidělení IČS, změna stavu objektu.

### 5.3.5 Referent SÚ/DO <Badge type="tip" text="Referent" />
**Základní oprávnění:**
* Ztotožňování osob, parcel a staveb.
* Čtení listů vlastnictví a BPP balíčků.
* Pečetění BPP balíčků (ověření dokumentace) – *pouze pro referenta SÚ*.

**Evidence a Agendy:**
* **Dokumenty a Řízení:** Správa dokumentů a řízení domovského úřadu, ukončení řízení.
* **Platební příkazy:** Čtení platebních příkazů domovského úřadu.
* **Záměry a Objekty:** Čtení, zápis, přidělení IČS, přepis navrhovaného objektu do evidence, změna stavu objektu.

### 5.3.6 Zaměstnanec sekretariátu SÚ/DO <Badge type="tip" text="Sekretariát" />
**Oprávnění:**
* Čtení BPP balíčků, řízení, záměrů a stavebních objektů.
* Čtení a zápis do evidence dokumentů.
* Čtení platebních příkazů domovského úřadu a označení platebního příkazu za zaplacený.

### 5.3.7 Oprávnění potvrzení platby SÚ/DO <Badge type="tip" text="Oprávnění" />
**Evidence platebních příkazů:**
* Čtení platebních příkazů domovského úřadu.
* Označení platebního příkazu za zaplacený.

::: info POZNÁMKA
Tato role je typicky kombinována podle potřeb úřadu s rolí vedoucího nebo referenta, kteří oprávnění potvrzení platby ve výchozím nastavení nemají.
:::

### 5.3.8 Podpisové oprávnění SÚ/DO <Badge type="tip" text="Oprávnění" />
**Evidence dokumentů:**
* Podepisování, schvalování a vrácení dokumentů.

::: warning DŮLEŽITÉ OMEZENÍ ROLE
Role se používá v kombinaci s rolí referenta. Referent s touto rolí může schválit a podepsat dokumenty, **které on sám vytvořil**. Tato role **neopravňuje** jejího držitele schvalovat a podepisovat dokumenty jiných referentů (toto oprávnění zůstává pouze vedoucímu). Důvodem je, že referent vidí pouze své dokumenty, zatímco vedoucí vidí všechny dokumenty úřadu.
:::