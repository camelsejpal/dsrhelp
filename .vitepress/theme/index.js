import DefaultTheme from 'vitepress/theme'
import { onMounted, watch, nextTick } from 'vue'
import { useData } from 'vitepress'

// CSS styl importujeme normálně, ten buildu nevadí
import '@fancyapps/ui/dist/fancybox/fancybox.css'

export default {
  ...DefaultTheme,
  setup() {
    const { route } = useData()

    const initFancybox = async () => {
      // Tímto zajistíme, že se kód spustí POUZE v prohlížeči, ne při buildu
      if (typeof window === 'undefined') return

      // Dynamicky importujeme celou knihovnu až za běhu v prohlížeči
      const { Fancybox } = await import('@fancyapps/ui')
      
      Fancybox.close()
      Fancybox.bind('.vp-doc img', {
        Hash: false,
      })
    }

    onMounted(() => {
      initFancybox()
    })

    watch(
      () => route.path,
      () => nextTick(() => initFancybox())
    )
  }
}