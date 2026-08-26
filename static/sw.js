const CACHE_NAME = 'tajergo-static-v20260825-2';
const STATIC_EXTENSIONS = /\.(?:css|js|png|jpg|jpeg|webp|svg|woff2?)$/i;

self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  // Dynamic pages/API: always use the network so new products/settings/orders
  // are never hidden by an old Service Worker cache.
  if (request.mode === 'navigate' || url.pathname.startsWith('/api/') ||
      url.pathname.startsWith('/store/') || url.pathname.startsWith('/dashboard') ||
      url.pathname.startsWith('/manifest/')) {
    event.respondWith(fetch(request));
    return;
  }

  if (!url.pathname.startsWith('/static/') || !STATIC_EXTENSIONS.test(url.pathname)) {
    return;
  }

  event.respondWith(
    caches.match(request).then(cached => {
      const network = fetch(request).then(response => {
        if (response.ok) {
          const copy = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        }
        return response;
      });
      return cached || network;
    })
  );
});
