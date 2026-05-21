import DefaultTheme from 'vitepress/theme'
import { Fancybox } from '@fancyapps/ui'
import '@fancyapps/ui/dist/fancybox/fancybox.css' // Import CSS stylů pro Fancybox
import { onMounted, watch, nextTick } from 'vue'
import { useData } from 'vitepress'

export default {
  ...DefaultTheme,
  setup() {
    const { route } = useData()

    // Funkce, která vyhledá obrázky a připraví je pro Fancybox
    const initFancybox = () => {
      // Ukončíme předchozí instanci, aby se nehromadily na pozadí
      Fancybox.close()
      
      // Nabindujeme Fancybox na všechny obrázky uvnitř obsahu (.vp-doc)
      Fancybox.bind('.vp-doc img', {
        // Zde můžete definovat globální chování (např. animace, popisky)
        Hash: false, // Vypne přidávání #hashů do URL při otevření obrázku
      })
    }

    // Inicializace při prvním načtení stránky
    onMounted(() => {
      initFancybox()
    })

    // Klíčová část pro VitePress: Re-inicializace při překliknutí na jinou stránku
    watch(
      () => route.path,
      () => nextTick(() => initFancybox())
    )
  }
}