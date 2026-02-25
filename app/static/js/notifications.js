/**
 * Sistema de Notificaciones Toast
 * ==============================
 * Sistema de notificaciones visuales mejorado para la plataforma
 */

class ToastNotification {
    constructor() {
        this.container = null;
        this.init();
    }
    
    init() {
        // Crear contenedor de toasts
        this.container = document.createElement('div');
        this.container.id = 'toast-container';
        this.container.className = 'toast-container position-fixed top-0 end-0 p-3';
        this.container.style.zIndex = '9999';
        document.body.appendChild(this.container);
    }
    
    show(options) {
        const {
            title = '',
            message = '',
            type = 'info', // success, error, warning, info
            duration = 4000,
            icon = null,
            dismissible = true
        } = options;
        
        const toast = document.createElement('div');
        toast.className = `toast show align-items-center text-white bg-${type} border-0`;
        toast.setAttribute('role', 'alert');
        toast.setAttribute('aria-live', 'assertive');
        toast.setAttribute('aria-atomic', 'true');
        
        // Icono según tipo
        const icons = {
            success: 'fas fa-check-circle',
            error: 'fas fa-exclamation-circle',
            warning: 'fas fa-exclamation-triangle',
            info: 'fas fa-info-circle'
        };
        
        const iconClass = icon || icons[type] || icons.info;
        
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body d-flex align-items-center">
                    <i class="${iconClass} me-2 fs-5"></i>
                    <div>
                        ${title ? `<strong>${title}</strong>` : ''}
                        ${message}
                    </div>
                </div>
                ${dismissible ? `
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                ` : ''}
            </div>
        `;
        
        this.container.appendChild(toast);
        
        // Auto dismiss
        if (duration > 0) {
            setTimeout(() => {
                toast.classList.remove('show');
                setTimeout(() => toast.remove(), 300);
            }, duration);
        }
        
        return toast;
    }
    
    // Métodos快捷
    success(message, title = '¡Éxito!') {
        return this.show({ message, type: 'success', title });
    }
    
    error(message, title = 'Error') {
        return this.show({ message, type: 'danger', title, duration: 6000 });
    }
    
    warning(message, title = 'Advertencia') {
        return this.show({ message, type: 'warning', title });
    }
    
    info(message, title = 'Información') {
        return this.show({ message, type: 'info', title });
    }
    
    // Notificación con acciones
    action(message, actions) {
        const toast = document.createElement('div');
        toast.className = 'toast show align-items-center text-white bg-primary border-0';
        
        let actionsHtml = '';
        if (actions && actions.length > 0) {
            actionsHtml = '<div class="mt-2 pt-2 border-top">';
            actions.forEach(action => {
                actionsHtml += `<button class="btn btn-sm btn-light me-2" onclick="${action.onClick}">${action.label}</button>`;
            });
            actionsHtml += '</div>';
        }
        
        toast.innerHTML = `
            <div class="toast-body">
                ${message}
                ${actionsHtml}
            </div>
        `;
        
        this.container.appendChild(toast);
        
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 5000);
    }
}

// Inicializar globally
window.toast = new ToastNotification();

// Función global para usar desde cualquier lugar
window.showToast = function(message, type = 'info', title = '') {
    return window.toast.show({ message, type, title });
};
