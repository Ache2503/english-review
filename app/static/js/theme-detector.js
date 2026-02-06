/**
 * Theme Detector & Manager
 * Detecta automáticamente el modo oscuro/claro del sistema
 * y aplica los estilos correspondientes
 */

(function() {
    'use strict';

    // Configuración del tema
    const THEME_CONFIG = {
        LIGHT: 'light',
        DARK: 'dark',
        AUTO: 'auto',
        STORAGE_KEY: 'theme-preference'
    };

    /**
     * Detecta la preferencia de tema del sistema
     */
    function detectSystemTheme() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return THEME_CONFIG.DARK;
        }
        return THEME_CONFIG.LIGHT;
    }

    /**
     * Obtiene la preferencia de tema almacenada
     */
    function getStoredTheme() {
        return localStorage.getItem(THEME_CONFIG.STORAGE_KEY);
    }

    /**
     * Guarda la preferencia de tema
     */
    function saveTheme(theme) {
        localStorage.setItem(THEME_CONFIG.STORAGE_KEY, theme);
    }

    /**
     * Obtiene el tema actual a usar
     */
    function getCurrentTheme() {
        const stored = getStoredTheme();
        if (stored) {
            return stored;
        }
        return detectSystemTheme();
    }

    /**
     * Aplica el tema al documento
     */
    function applyTheme(theme) {
        const htmlElement = document.documentElement;
        
        if (theme === THEME_CONFIG.DARK) {
            htmlElement.style.colorScheme = 'dark';
            document.body.style.colorScheme = 'dark';
        } else {
            htmlElement.style.colorScheme = 'light';
            document.body.style.colorScheme = 'light';
        }
    }

    /**
     * Inicializa la detección de tema
     */
    function initThemeDetector() {
        // Aplicar tema inicial
        const currentTheme = getCurrentTheme();
        applyTheme(currentTheme);

        // Escuchar cambios en la preferencia del sistema
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        // Para navegadores modernos
        if (mediaQuery.addEventListener) {
            mediaQuery.addEventListener('change', (e) => {
                const stored = getStoredTheme();
                // Solo cambiar si el usuario no ha establecido una preferencia manual
                if (!stored) {
                    applyTheme(e.matches ? THEME_CONFIG.DARK : THEME_CONFIG.LIGHT);
                    // Recargar estilos si es necesario
                    document.documentElement.style.colorScheme = e.matches ? 'dark' : 'light';
                }
            });
        }
        // Para navegadores antiguos
        else if (mediaQuery.addListener) {
            mediaQuery.addListener((e) => {
                const stored = getStoredTheme();
                if (!stored) {
                    applyTheme(e.matches ? THEME_CONFIG.DARK : THEME_CONFIG.LIGHT);
                }
            });
        }

        // Exponer función pública para cambiar tema manualmente
        window.setTheme = function(theme) {
            saveTheme(theme);
            applyTheme(theme);
            
            // Emitir evento personalizado
            const event = new CustomEvent('themechange', { detail: { theme } });
            document.dispatchEvent(event);
        };

        // Exponer función pública para obtener tema actual
        window.getTheme = function() {
            return getCurrentTheme();
        };

        // Exponer función pública para resetear a tema del sistema
        window.resetTheme = function() {
            localStorage.removeItem(THEME_CONFIG.STORAGE_KEY);
            const theme = detectSystemTheme();
            applyTheme(theme);
            
            const event = new CustomEvent('themechange', { detail: { theme } });
            document.dispatchEvent(event);
        };
    }

    // Ejecutar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initThemeDetector);
    } else {
        initThemeDetector();
    }
})();
