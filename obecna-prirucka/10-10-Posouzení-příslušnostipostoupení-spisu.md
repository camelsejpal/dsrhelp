---
title: 10. Posouzení příslušnosti / postoupení spisu
outline: deep
---

# 10. Posouzení příslušnosti a postoupení spisu

## 10.1 Posouzení příslušnosti ihned po přijetí žádosti

### Pracovní postup nepříslušného úřadu (který postupuje spis)

1. Úřad obdrží žádost, která mu nepřísluší.
2. Uživatel, který je nastavený jako příjemce dokumentů, obdrží aplikační či emailovou notifikaci (dle osobního nastavení).
3. Žádost zpracuje založením nového řízení.
4. V řízení vytvoří vlastní dokument **Usnesení o postoupení** (Druh = *Usnesení o postoupení pro nepříslušnost*) a jako hlavní dokument vloží samotné usnesení o postoupení.

![](_page_194_Picture_7.jpeg)

::: warning DŮLEŽITÉ UPOZORNĚNÍ
Vždy vložte do dokumentu Usnesení o postoupení **hlavní dokument**. Bez vložení hlavního dokumentu nebude moci úřad, kterému je postupováno, založit řízení (vložit dokument do řízení). V případě, kdy zpracovatel nepřidal hlavní dokument k dokumentu Usnesení pro nepříslušnost, dokument nebude v nabídce pro vybrání. Zpracovatel je upozorněn hláškou.

![](_page_195_Picture_0.jpeg)
:::

Výběr dokumentu pro postoupení spisu je omezen pomocí validace, kde rozsah nabízených dokumentů pro pole `Dokument` na formuláři `Postoupit spis` a formuláři `Určit příslušnost žádosti v řízení` bude obsahovat pouze dokumenty následujících druhů:
* Usnesení o postoupení pro nepříslušnost
* Procesní usnesení
* Usnesení

Pokud se v nabídce nezobrazí žádný dokument, uživatel musí nejprve vytvořit potřebné usnesení.

::: danger POVINNÉ POLE
Pokud pole zůstane prázdné (uživatel nemá nic na výběr) a klikne na tlačítko `Potvrdit`, vyskočí chyba ohledně povinného pole.

![](_page_196_Figure_0.jpeg)

![](_page_196_Figure_1.jpeg)
:::

::: info POZNÁMKA
Pokud byly v daném řízení již vytvořeny jakékoli jiné vlastní dokumenty, budou postoupeny ve formě příloh i tyto dokumenty. Zkontrolujte, zda mají být všechny dokumenty postoupeny, případně nevyhovující dokumenty zrušte.

V případě, že by během vytváření Hlavního dokumentu Usnesení nebo dokumentů na záložce Přílohy **nebylo vyplněno pole Název** a bylo ponecháno prázdné, systém automaticky doplní název PDF souboru do pole Název u postoupeného doručeného dokumentu.
:::

![](_page_197_Figure_1.jpeg)

Doručený dokument *Usnesení o postoupení*, který obdrží úřad, kterému byl spis postoupen, následně bude mít doplněný název z názvu PDF souboru:

![](_page_197_Figure_3.jpeg)

::: warning KONTROLA ÚKOLŮ
Při postoupení je třeba splnit úkoly na všech dokumentech. Není možné postoupit spis s rozpracovanými dokumenty.

![](_page_198_Figure_0.jpeg)
:::

5. **Postoupení spisu je možné dvěma způsoby v závislosti na procesu v řízení:**
   * **A) Řízení nemá proces (systém nenabízí úkoly ke zpracování):** V přehledu řízení použijete akční tlačítko `Postoupení spisu`. V dialogovém okně vložte dokument *Usnesení o postoupení* a zvolte příslušný úřad.
     ![](_page_198_Picture_3.jpeg)
   * **B) Řízení má proces (systém nabízí úkoly ke zpracování):** V novém dialogovém okně při splnění úkolu `Určit příslušnost žádosti v řízení` zvolte u otázky "Je žádost příslušná" možnost **Ne**, vložte dokument *Usnesení o postoupení* a zvolte příslušný úřad.
     ![](_page_199_Picture_0.jpeg)

::: info DOPLŇUJÍCÍ INFORMACE K VÝBĚRU DOKUMENTU
Rozsah nabízených dokumentů pro pole `Dokument` na formuláři bude obsahovat výhradně: *Usnesení o postoupení pro nepříslušnost*, *Procesní usnesení* a *Usnesení*. Jiný typ dokumentu formulář nebude brát v potaz a pole zůstane prázdné. V tomto případě je nutné nejdříve vytvořit příslušné usnesení.

![](_page_199_Picture_3.jpeg)

V případě, že jedno z polí zůstane prázdné, pak po kliknutí na tlačítko `Potvrdit` budete upozorněni, že se jedná o povinná pole.

![](_page_200_Picture_1.jpeg)
:::

6. Řízení je následně ve stavu `Ukončeno – postoupeno`.

![](_page_200_Picture_3.jpeg)

---

### Pracovní postup úřadu, kterému byl spis postoupen

1. Úřad obdrží dokument **Usnesení o postoupení**.
2. Uživatel, který je nastaven pro příjem dokumentů, obdrží notifikaci (aplikační či e-mailovou). Notifikace obsahuje identifikátor nového dokumentu (PID), odkaz na dokument a číslo původního řízení.
   * **Aplikační notifikace:**
     ![](_page_201_Figure_3.jpeg)
   * **E-mailová notifikace** (pokud je nastavena)
3. U doručeného dokumentu ke zpracování obsahuje záložka `Hlavní dokument` Usnesení o postoupení.

![](_page_202_Picture_4.jpeg)

::: warning CHYBĚJÍCÍ DOKUMENT
Pokud hlavní dokument k *Usnesení o nepříslušnosti* nebyl vložen postupujícím úřadem, systém Vás na to upozorní při zpracování úkolu `Určit způsob zpracování dokumentu`. V takovém případě prosím kontaktujte daný úřad a domluvte se na zaslání chybějícího dokumentu.

![](_page_202_Figure_7.jpeg)
:::

4. Pod záložkou `Přílohy` se nachází žádost (původní iniciační dokument), přílohy žádosti a další dokumenty, které byly obsaženy v původním řízení.

![](_page_203_Figure_0.jpeg)

5. U úkolu `Určit způsob zpracování dokumentu` může uživatel zvolit možnost **Založit řízení** nebo **Vložit dokument do řízení** (např. v případě doplnění žádosti).

![](_page_203_Picture_2.jpeg)

6. Záložka `Auditní záznamy` nyní obsahuje informaci o dokumentu Usnesení o postoupení.

![](_page_204_Figure_1.jpeg)

---

## 10.2 Postoupení spisu manuálně v průběhu procesu

Pokud je potřeba postoupit spis v průběhu procesu řízení, je možné toto učinit manuálně kliknutím na tlačítko `Postoupit spis` přímo v detailu řízení.

![](_page_205_Figure_2.jpeg)

V dialogovém okně vyberte dokument *Usnesení o postoupení* a příslušný úřad. Tento dokument musí být již vytvořen, aby ho bylo možné vybrat. Vybráním dokumentu v tomto dialogovém okně nedojde k jeho vypravení. Stiskněte tlačítko `Potvrdit`.

![](_page_205_Figure_4.jpeg)

Řízení je následně ve stavu `Ukončeno` s výsledkem `Postoupeno`. Řízení naleznete v pohledu **Ukončená řízení**.

![](_page_206_Figure_0.jpeg)

Uživatel z úřadu, na který byl spis postoupen, je upozorněn notifikací na nově založené řízení.

![](_page_206_Figure_2.jpeg)

::: warning NEDOKONČENÉ DOKUMENTY
Při postoupení spisu systém uživatele upozorní na existenci nedokončených dokumentů. V okně pro postoupení spisu se zobrazí seznam všech nedokončených dokumentů. Toto upozornění má **pouze informativní charakter** a nebrání uživateli spis postoupit.

![](_page_208_Figure_0.jpeg)

Seznam obsahuje PID, číslo jednací a název dokumentu (položky jsou seřazeny dle č.j.). Název dokumentu slouží jako odkaz, který otevře novou záložku prohlížeče a přesměruje uživatele přímo na detail nedokončeného dokumentu.
:::

**Co se považuje za nedokončený dokument:**
* Dokumenty (s hlavním dokumentem nebo bez) ve stavu `Rozpracovaný`.
* Dokumenty ve stavech `Ve schvalování`, `K podpisu` a `Podepsaný` (pokud nebyl založen do spisu).
* *(Naopak nejsou zobrazeny doručené a zrušené dokumenty, ani dokumenty ve stavu `Odeslaný` a `Podepsaný`, pokud už do spisu založeny byly).*

::: info AKTUALIZACE OKNA
Původní okno se seznamem nedokončených dokumentů není automaticky aktualizováno. Po případném zpracování některého z uvedených dokumentů je nutné stránku manuálně obnovit pomocí akčního tlačítka `Načíst znovu` (nebo F5 v prohlížeči).
:::

---

## 10.3 Postoupení žádosti ze Stavebního úřadu na Dotčený orgán

V případě chybného přiřazení žádosti ze strany úřadu či z centrální datové schránky lze žádost předat. Tuto možnost lze využít pouze pro dokumenty ve stavu `Ke zpracování`.

K provedení tohoto úkonu je oprávněn **pouze lokální administrátor úřadu**. Žádost lze předat pouze mezi stavebním úřadem a dotčeným orgánem (či naopak) **v rámci jedné obce/města**.

V detailu dokumentu klikněte na akční tlačítko `Změnit zpracovatele`.

![](_page_209_Figure_7.jpeg)

Po rozkliknutí se zobrazí dialogové okno, ve kterém lze vybrat cílový úřad. Po jeho výběru se automaticky nastaví uživatel, který je u vybraného úřadu nastaven jako příjemce dokumentů.

![](_page_210_Figure_0.jpeg)

Následně výběr potvrďte tlačítkem `Potvrdit`.

::: danger OMEZENÍ PŘEDÁVÁNÍ
Nelze předávat dokumenty mezi úřady jiných měst a obcí! V případě, že byla doručena žádost patřící úřadu jiné obce/města, je nutné žádost postoupit prostřednictvím *postoupení pro nepříslušnost*, případně se obrátit na podporu uživatelů (pokud se jedná o technickou chybu), kdy žádost předá globální administrátor.
:::