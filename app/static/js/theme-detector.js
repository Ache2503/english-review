/**
 * Theme Detector & Manager
 * Detecta automáticamente el modo oscuro/claro del sistema
 * Usa el atributo data-bs-theme de Bootstrap 5.3
 */

(function() {
    'use strict';

    const THEME_CONFIG = {
        LIGHT: 'light',
        DARK: 'dark',
        STORAGE_KEY: 'theme-preference'
    };

    const html = document.documentElement;
    const themeToggle = document.getElementById('themeToggle');

    function detectSystemTheme() {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return THEME_CONFIG.DARK;
        }
        return THEME_CONFIG.LIGHT;
    }

    function getStoredTheme() {
        return localStorage.getItem(THEME_CONFIG.STORAGE_KEY);
    }

    function saveTheme(theme) {
        localStorage.setItem(THEME_CONFIG.STORAGE_KEY, theme);
    }

    function getCurrentTheme() {
        const stored = getStoredTheme();
        if (stored) {
            return stored;
        }
        return detectSystemTheme();
    }

    function updateToggleIcon(theme) {
        if (!themeToggle) return;
        
        const icon = themeToggle.querySelector('i');
        if (icon) {
            if (theme === THEME_CONFIG.DARK) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        }
    }

    function applyTheme(theme) {
        html.setAttribute('data-bs-theme', theme);
        updateToggleIcon(theme);
        
        if (theme === THEME_CONFIG.DARK) {
            html.style.colorScheme = 'dark';
        } else {
            html.style.colorScheme = 'light';
        }
    }

    function initThemeDetector() {
        const currentTheme = getCurrentTheme();
        applyTheme(currentTheme);

        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        if (mediaQuery.addEventListener) {
            mediaQuery.addEventListener('change', (e) => {
                const stored = getStoredTheme();
                if (!stored) {
                    applyTheme(e.matches ? THEME_CONFIG.DARK : THEME_CONFIG.LIGHT);
                }
            });
        }

        if (themeToggle) {
            themeToggle.addEventListener('click', function() {
                const currentTheme = html.getAttribute('data-bs-theme');
                const newTheme = currentTheme === THEME_CONFIG.DARK ? THEME_CONFIG.LIGHT : THEME_CONFIG.DARK;
                saveTheme(newTheme);
                applyTheme(newTheme);
                
                const event = new CustomEvent('themechange', { detail: { theme: newTheme } });
                document.dispatchEvent(event);
            });
        }

        window.setTheme = function(theme) {
            saveTheme(theme);
            applyTheme(theme);
            
            const event = new CustomEvent('themechange', { detail: { theme } });
            document.dispatchEvent(event);
        };

        window.getTheme = function() {
            return getCurrentTheme();
        };

        window.resetTheme = function() {
            localStorage.removeItem(THEME_CONFIG.STORAGE_KEY);
            const theme = detectSystemTheme();
            applyTheme(theme);
            
            const event = new CustomEvent('themechange', { detail: { theme } });
            document.dispatchEvent(event);
        };
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initThemeDetector);
    } else {
        initThemeDetector();
    }
})();
