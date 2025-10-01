// Portal 3AII - JavaScript Principal

document.addEventListener('DOMContentLoaded', function() {
    initializeSidebar();
    initializeTooltips();
    initializeSearchBox();
    initializeNotifications();
    initializeTheme();
});

// Inicializar sidebar responsiva
function initializeSidebar() {
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('show');
        });
    }
    
    // Fechar sidebar ao clicar fora (mobile)
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 991.98) {
            if (!sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
                sidebar.classList.remove('show');
            }
        }
    });
    
    // Marcar link ativo na sidebar
    const currentPath = window.location.pathname;
    const sidebarLinks = document.querySelectorAll('.sidebar-menu a');
    
    sidebarLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// Inicializar tooltips do Bootstrap
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Inicializar caixa de busca
function initializeSearchBox() {
    const searchInput = document.querySelector('.search-box input');
    
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch(this.value);
            }
        });
        
        // Busca em tempo real (opcional)
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                if (this.value.length >= 3) {
                    performLiveSearch(this.value);
                }
            }, 500);
        });
    }
}

// Realizar busca
function performSearch(query) {
    if (query.trim()) {
        console.log('Buscando por:', query);
        // Implementar lógica de busca aqui
        // Pode redirecionar para uma página de resultados
        // window.location.href = `/busca/?q=${encodeURIComponent(query)}`;
    }
}

// Busca em tempo real
function performLiveSearch(query) {
    // Implementar busca AJAX aqui
    console.log('Busca em tempo real:', query);
}

// Inicializar sistema de notificações
function initializeNotifications() {
    const notificationDropdown = document.querySelector('.dropdown-toggle');
    
    if (notificationDropdown) {
        // Marcar notificações como lidas ao abrir o dropdown
        notificationDropdown.addEventListener('click', function() {
            setTimeout(() => {
                markNotificationsAsRead();
            }, 100);
        });
    }
    
    // Auto-atualizar notificações a cada 30 segundos
    setInterval(updateNotifications, 30000);
}

// Marcar notificações como lidas
function markNotificationsAsRead() {
    const badge = document.querySelector('.notification-badge');
    if (badge) {
        // Fazer requisição AJAX para marcar como lidas
        // Por enquanto, apenas esconder o badge
        setTimeout(() => {
            badge.style.display = 'none';
        }, 2000);
    }
}

// Atualizar notificações
function updateNotifications() {
    // Implementar AJAX para buscar novas notificações
    console.log('Atualizando notificações...');
}

// Inicializar tema (claro/escuro)
function initializeTheme() {
    const savedTheme = localStorage.getItem('portal-theme') || 'light';
    applyTheme(savedTheme);
    
    // Adicionar botão para alternar tema (se existir)
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = document.body.classList.contains('dark-theme') ? 'dark' : 'light';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            applyTheme(newTheme);
            localStorage.setItem('portal-theme', newTheme);
        });
    }
}

// Aplicar tema
function applyTheme(theme) {
    if (theme === 'dark') {
        document.body.classList.add('dark-theme');
    } else {
        document.body.classList.remove('dark-theme');
    }
}

// Utilitários para formulários
function setupFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

// Utilitários para modais
function showModal(modalId) {
    const modal = new bootstrap.Modal(document.getElementById(modalId));
    modal.show();
}

function hideModal(modalId) {
    const modal = bootstrap.Modal.getInstance(document.getElementById(modalId));
    if (modal) {
        modal.hide();
    }
}

// Utilitários para alerts
function showAlert(message, type = 'info', duration = 5000) {
    const alertContainer = document.querySelector('.alert-container') || document.querySelector('.content-area');
    
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    alertContainer.insertBefore(alert, alertContainer.firstChild);
    
    // Auto-remover após duration
    setTimeout(() => {
        if (alert.parentNode) {
            alert.remove();
        }
    }, duration);
}

// Utilitários para loading
function showLoading(element) {
    const originalContent = element.innerHTML;
    element.setAttribute('data-original-content', originalContent);
    element.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Carregando...';
    element.disabled = true;
}

function hideLoading(element) {
    const originalContent = element.getAttribute('data-original-content');
    if (originalContent) {
        element.innerHTML = originalContent;
        element.removeAttribute('data-original-content');
    }
    element.disabled = false;
}

// Utilitários para animações
function animateValue(element, start, end, duration = 1000) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (end - start) + start);
        element.textContent = value;
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Funções específicas para o dashboard
function updateStats() {
    // Animar contadores no dashboard
    const statCards = document.querySelectorAll('.stats-card .card-title');
    statCards.forEach(card => {
        const finalValue = parseInt(card.textContent) || 0;
        animateValue(card, 0, finalValue, 1500);
    });
}

// Função para formatar datas
function formatDate(date, format = 'dd/mm/yyyy') {
    const d = new Date(date);
    const day = String(d.getDate()).padStart(2, '0');
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const year = d.getFullYear();
    
    switch (format) {
        case 'dd/mm/yyyy':
            return `${day}/${month}/${year}`;
        case 'mm/dd/yyyy':
            return `${month}/${day}/${year}`;
        case 'yyyy-mm-dd':
            return `${year}-${month}-${day}`;
        default:
            return d.toLocaleDateString('pt-BR');
    }
}

// Função para calcular tempo restante
function timeUntil(targetDate) {
    const now = new Date();
    const target = new Date(targetDate);
    const diff = target - now;
    
    if (diff <= 0) return 'Expirado';
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    
    if (days > 0) return `${days} dias`;
    if (hours > 0) return `${hours} horas`;
    return `${minutes} minutos`;
}

// Função para copiar texto para clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Texto copiado para a área de transferência!', 'success', 2000);
    }).catch(() => {
        showAlert('Erro ao copiar texto', 'danger', 3000);
    });
}

// Função para download de arquivo
function downloadFile(url, filename) {
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Função para validar email
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Função para validar CPF (útil para cadastros)
function validateCPF(cpf) {
    cpf = cpf.replace(/[^\d]+/g, '');
    if (cpf.length !== 11 || !!cpf.match(/(\d)\1{10}/)) return false;
    
    cpf = cpf.split('').map(el => +el);
    const rest = (count) => (cpf.slice(0, count-12).reduce((soma, el, index) => (soma + el * (count-index)), 0) * 10) % 11 % 10;
    
    return rest(10) === cpf[9] && rest(11) === cpf[10];
}

// Exportar funções globalmente
window.PortalUtils = {
    showAlert,
    showModal,
    hideModal,
    showLoading,
    hideLoading,
    formatDate,
    timeUntil,
    copyToClipboard,
    downloadFile,
    validateEmail,
    validateCPF,
    updateStats
};

// Inicializar utilitários quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    setupFormValidation();
    
    // Se estiver no dashboard, atualizar stats
    if (window.location.pathname === '/') {
        setTimeout(updateStats, 500);
    }
});