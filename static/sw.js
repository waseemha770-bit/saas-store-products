const CACHE_NAME = 'tajergo-cache-v20260828';
const STATIC_EXTENSIONS = /\.(?:css|js|png|jpg|jpeg|webp|svg|woff2?|ico)$/i;

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

  // 1. مسارات الـ API والـ Manifest: دائماً من الشبكة لضمان التحديث الفوري
  if (url.pathname.startsWith('/api/') || url.pathname.includes('manifest')) {
    event.respondWith(fetch(request));
    return;
  }

  // 2. صفحات الموقع (HTML): استراتيجية Network First لتلبية شروط تثبيت التطبيق (PWA)
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request).catch(() => caches.match(request))
    );
    return;
  }

  // 3. الملفات الثابتة والصور: استراتيجية Stale-While-Revalidate لسرعة تحميل خارقة
  if (url.pathname.startsWith('/static/') || STATIC_EXTENSIONS.test(url.pathname)) {
    event.respondWith(
      caches.match(request).then(cachedResponse => {
        const fetchPromise = fetch(request).then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            const responseToCache = networkResponse.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(request, responseToCache));
          }
          return networkResponse;
        }).catch(() => { /* تجاهل أخطاء الشبكة للملفات الثابتة */ });
        
        // إرجاع الكاش فوراً إن وجد (للسرعة)، وإلا انتظار الشبكة
        return cachedResponse || fetchPromise;
      })
    );
  }
});
