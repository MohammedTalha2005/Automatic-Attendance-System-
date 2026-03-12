// Main JavaScript functionality
document.addEventListener('DOMContentLoaded', function () {
    console.log("Main JS Loaded");
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});

// Utility functions
function showNotification(message, type = 'success', duration = 5000) {
    console.log("showNotification called:", message, type);

    // Create a very simple element that doesn't depend on complex IDs
    const toast = document.createElement('div');
    toast.className = `alert alert-${type}`;

    // Hardcoded simple styles to guarantee visibility
    toast.style.position = 'fixed';
    toast.style.top = '20px';
    toast.style.right = '20px';
    toast.style.zIndex = '10000';
    toast.style.padding = '15px 20px';
    toast.style.borderRadius = '8px';
    toast.style.minWidth = '250px';
    toast.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
    toast.style.borderLeft = '5px solid ' + (type === 'success' ? '#10b981' : '#ef4444');
    toast.style.background = '#1e293b';
    toast.style.color = '#fff';
    toast.style.display = 'flex';
    toast.style.alignItems = 'center';
    toast.style.gap = '10px';
    toast.style.fontSize = '14px';
    toast.style.fontWeight = '600';

    let icon = '🔔';
    if (type === 'success') icon = '✅';
    if (type === 'error' || type === 'danger') icon = '❌';
    if (type === 'warning') icon = '⚠️';

    toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;

    document.body.appendChild(toast);

    // Auto-remove
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.5s ease';
        setTimeout(() => toast.remove(), 500);
    }, duration);
}
