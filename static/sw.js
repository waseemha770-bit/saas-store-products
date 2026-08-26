const CACHE_NAME = 'tajergo-pwa-v2';

self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    fetch(e.request).catch((error) => {
      console.error('Network Error:', error);
      return new Response('حدث خطأ في الاتصال بالشبكة.', { status: 408 });
    })
  );
});
