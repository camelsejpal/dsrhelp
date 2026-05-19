import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  // Název vašeho GitHub repozitáře
  base: '/dsrhelp/',
  title: "Uživatelská příručka DSŘ",
  description: "Sada příruček DSŘ",
  themeConfig: {
    // Horní navigační menu
    nav: [
      { text: 'Domů', link: '/' },
      { text: 'Obecná příručka', link: '/obecna-prirucka/00-Uvodni-informace' }
    ],

    // Levé menu (Sidebar) strukturované tak, aby se ukázalo jen u této příručky
    sidebar: {
      '/obecna-prirucka/': [
        {
          text: 'Obecná příručka',
          items: [
            { text: 'Úvodní informace', link: '/obecna-prirucka/00-Uvodni-informace' },
            { text: '1. Úvod', link: '/obecna-prirucka/01-1-Úvod' },
            { text: '2. Přihlášení do ISSŘ a nastavení', link: '/obecna-prirucka/02-2-Přihlášení-do-ISSŘ-a-nastavení-uživatelského-účt' },
            { text: '3. Základní orientace v ISSŘ', link: '/obecna-prirucka/03-3-Základní-orientace-v-ISSŘ' },
            { text: '4. Nástěnka', link: '/obecna-prirucka/04-4-Nástěnka' },
            { text: '5. Záměry', link: '/obecna-prirucka/05-5-Záměry' },
            { text: '6. Řízení', link: '/obecna-prirucka/06-6-Řízení' },
            { text: '7. Dokumenty', link: '/obecna-prirucka/07-7-Dokumenty' },
            { text: '8. Správní poplatky', link: '/obecna-prirucka/08-8-Správní-poplatky' },
            { text: '9. Příjem žádosti a její evidence', link: '/obecna-prirucka/09-9-Příjem-žádosti-a-její-evidence' },
            { text: '10. Posouzení příslušnosti', link: '/obecna-prirucka/10-10-Posouzení-příslušnostipostoupení-spisu' },
            { text: '11. Přidání účastníků a ověření', link: '/obecna-prirucka/11-11-Přidání-odesílatele-podateleúčastníků-řízení-a-' },
            { text: '12. Vytvoření rozdělovníku', link: '/obecna-prirucka/12-12-Vytvoření-rozdělovníkuů' },
            { text: '13. Ověření navrhovaných objektů a parcel', link: '/obecna-prirucka/13-13-Ověření-ztotožnění-navrhovaných-objektů-parcel-' },
            { text: '14. Vyjádření dotčených orgánů', link: '/obecna-prirucka/14-14-Vyjádření-a-závazná-stanoviska-dotčených-orgánů' },
            { text: '15. Tvorba vlastního dokumentu', link: '/obecna-prirucka/15-15-Tvorba-vlastního-dokumentu' },
            { text: '16. Přerušení řízení', link: '/obecna-prirucka/16-16-Přerušení-řízení' },
            { text: '17. Vyznačení nabytí právní moci', link: '/obecna-prirucka/17-17-Vyznačení-nabytí-právní-moci' },
            { text: '18. Nahlížení do spisu interně', link: '/obecna-prirucka/18-18-Nahlížení-do-spisu-v-rámci-jednoho-úřadu-intern' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})