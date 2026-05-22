import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  // Název vašeho GitHub repozitáře
  base: '/dsrhelp/',
  title: "Uživatelská příručka DSŘ",
  description: "Sada příruček DSŘ",
  themeConfig: {
    // Aktivace lokálního fulltextového vyhledávání s českým překladem
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: 'Hledat',
            buttonAriaLabel: 'Hledat v dokumentaci'
          },
          modal: {
            noResultsText: 'Nebyly nalezeny žádné výsledky',
            resetButtonTitle: 'Vymazat vyhledávání',
            footer: {
              selectText: 'vybrat',
              navigateText: 'pohyb',
              closeText: 'zavřít'
            }
          }
        }
      }
    },

    // Horní navigační menu
    nav: [
      { text: 'Domů', link: '/' },
      { text: 'Obecná příručka', link: '/obecna-prirucka/00-Uvodni-informace' },
      { text: 'Příručka lokálního administrátora', link: '/admin-prirucka/00-Titulni-strana' },
      { text: 'Vypravování dokumentů', link: '/vypraveni-prirucka/00-uvodni-informace' }
    ],

    // Vícenásobné levé menu (Sidebar) rozdělené podle složek [cite: 2]
    sidebar: {
      // SEKCE PRO OBECNOU PŘÍRUČKU
      '/obecna-prirucka/': [
        {
          text: 'Obecná příručka',
          items: [
            { text: 'Úvodní informace', link: '/obecna-prirucka/00-Uvodni-informace' },
            { text: '1. Úvod', link: '/obecna-prirucka/01-1-Úvod' },
            { text: '2. Přihlášení do ISSŘ a nastavení', link: '/obecna-prirucka/02-2-Přihlášení-do-ISSŘ-a-nastavení-uživatelského-účt' }, [cite: 3]
            { text: '3. Základní orientace v ISSŘ', link: '/obecna-prirucka/03-3-Základní-orientace-v-ISSŘ' }, [cite: 4]
            { text: '4. Nástěnka', link: '/obecna-prirucka/04-4-Nástěnka' }, [cite: 5]
            { text: '5. Záměry', link: '/obecna-prirucka/05-5-Záměry' }, [cite: 6]
            { text: '6. Řízení', link: '/obecna-prirucka/06-6-Řízení' }, [cite: 7]
            { text: '7. Dokumenty', link: '/obecna-prirucka/07-7-Dokumenty' }, [cite: 8]
            { text: '8. Správní poplatky', link: '/obecna-prirucka/08-8-Správní-poplatky' }, [cite: 9]
            { text: '9. Příjem žádosti a její evidence', link: '/obecna-prirucka/09-9-Příjem-žádosti-a-její-evidence' }, [cite: 10]
            { text: '10. Posouzení příslušnosti', link: '/obecna-prirucka/10-10-Posouzení-příslušnostipostoupení-spisu' }, [cite: 11]
            { text: '11. Přidání účastníků a ověření', link: '/obecna-prirucka/11-11-Přidání-odesílatele-podateleúčastníků-řízení-a-' }, [cite: 12]
            { text: '12. Vytvoření rozdělovníku', link: '/obecna-prirucka/12-12-Vytvoření-rozdělovníkuů' }, [cite: 13]
            { text: '13. Ověření navrhovaných objektů a parcel', link: '/obecna-prirucka/13-13-Ověření-ztotožnění-navrhovaných-objektů-parcel-' }, [cite: 14]
            { text: '14. Vyjádření dotčených orgánů', link: '/obecna-prirucka/14-14-Vyjádření-a-závazná-stanoviska-dotčených-orgánů' }, [cite: 15]
            { text: '15. Tvorba vlastního dokumentu', link: '/obecna-prirucka/15-15-Tvorba-vlastního-dokumentu' }, [cite: 16]
            { text: '16. Přerušení řízení', link: '/obecna-prirucka/16-16-Přerušení-řízení' }, [cite: 17]
            { text: '17. Vyznačení nabytí právní moci', link: '/obecna-prirucka/17-17-Vyznačení-nabytí-právní-moci' }, [cite: 18]
            { text: '18. Nahlížení do spisu interně', link: '/obecna-prirucka/18-18-Nahlížení-do-spisu-v-rámci-jednoho-úřadu-intern' } [cite: 19]
          ]
        }
      ],

      // SEKCE PRO PŘÍRUČKU LOKÁLNÍHO ADMINISTRÁTORA
      '/admin-prirucka/': [
        {
          text: 'Příručka lokálního administrátora',
          items: [
            { text: 'Titulní strana', link: '/admin-prirucka/00-Titulni-strana' },
            { text: '1. Verze dokumentu', link: '/admin-prirucka/01-1-Verze-dokumentu' }, [cite: 20, 21]
            { text: '2. Použité zkratky', link: '/admin-prirucka/02-2-Pouzite-zkratky' }, [cite: 22]
            { text: '3. Účel dokumentu', link: '/admin-prirucka/03-3-Ucel-dokumentu' }, [cite: 23]
            { text: '4. Přihlášení', link: '/admin-prirucka/04-4-Prihlaseni' }, [cite: 24]
            { text: '5. Administrace lokální administrátor', link: '/admin-prirucka/05-5-Administrace-lokalni-administrator' } [cite: 25]
          ]
        }
      ],

      // NOVÁ SEKCE PRO VYPRAVOVÁNÍ DOKUMENTŮ
      '/vypraveni-prirucka/': [
        {
          text: 'Vypravování dokumentů',
          items: [
            { text: 'Úvodní informace', link: '/vypraveni-prirucka/00-uvodni-informace' },
            { text: '1. Přidání osoby do řízení', link: '/vypraveni-prirucka/01-1-pridani-osoby-do-rizeni' }, [cite: 26, 27]
            { text: '2. Ověření', link: '/vypraveni-prirucka/02-2-overeni' }, [cite: 28]
            { text: '3. Zahraniční osoby', link: '/vypraveni-prirucka/03-3-zahranicni-osoby' }, [cite: 29]
            { text: '4. Způsob komunikace', link: '/vypraveni-prirucka/04-4-zpusob-komunikace' }, [cite: 30]
            { text: '5. Podmínky vypravení', link: '/vypraveni-prirucka/05-5-podminky-vypraveni' }, [cite: 31]
            { text: '6. Obsah vypravení', link: '/vypraveni-prirucka/06-6-obsah-vypraveni' }, [cite: 32]
            { text: '7. Vypravení do zahraniči', link: '/vypraveni-prirucka/07-7-vypraveni-do-zahranici' }, [cite: 33]
            { text: '8. Vypravování službou HKP', link: '/vypraveni-prirucka/08-8-vypravovani-sluzbou-hkp' }, [cite: 34]
            { text: '9. Ruční vypravení', link: '/vypraveni-prirucka/09-9-rucni-vypraveni' }, [cite: 35]
            { text: '10. Tisk adres na obálky', link: '/vypraveni-prirucka/10-10-tisk-adres-na-obalky' }, [cite: 36]
            { text: '11. Převzetí osobně', link: '/vypraveni-prirucka/11-11-vypraveni-prevzeti-osobne' }, [cite: 37]
            { text: '12. Vypravení vyhláškou', link: '/vypraveni-prirucka/12-12-vypraveni-vyhlaskou' }, [cite: 38]
            { text: '13. Opětovné vypravení', link: '/vypraveni-prirucka/13-13-opetovne-vypraveni-dokumentu' }, [cite: 39]
            { text: '14. Doručenky', link: '/vypraveni-prirucka/14-14-dorucenky' }, [cite: 40]
            { text: '15. Stav vypravení', link: '/vypraveni-prirucka/15-15-stav-vypraveni' }, [cite: 41]
            { text: '16. Notifikace', link: '/vypraveni-prirucka/16-16-notifikace' }, [cite: 42]
            { text: '17. Důvody nevypravení', link: '/vypraveni-prirucka/17-17-konkretni-duvody-nevypraveni' }, [cite: 43]
            { text: '18. Podpora', link: '/vypraveni-prirucka/18-18-podpora' } [cite: 44]
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})