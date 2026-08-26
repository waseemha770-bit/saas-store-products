
const CACHE_NAME = 'tajergo-pwa-v1';
self.addEventListener('install', (e) => {
  self.skipWaiting();
});
self.addEventListener('fetch', (e) => {
  // تمرير الطلبات للسيرفر بدون تعطيل العمليات الديناميكية
});
