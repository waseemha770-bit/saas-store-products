// Shared frontend helpers for TajerGo.
(function () {
    'use strict';

    window.fixImg = window.fixImg || function (img) {
        if (!img || img.dataset.proxied) return;
        img.dataset.proxied = 'true';
        const src = img.getAttribute('src');
        if (src && src !== '' && !src.includes('placeholder')) {
            img.src = 'https://wsrv.nl/?url=' + encodeURIComponent(src);
        }
    };
})();
