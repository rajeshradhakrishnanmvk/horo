// js/serviceWorker.js
const cacheName = 'kanban-board-v1';
const cacheAssets = [
    '/',
    '/index.html',
    '/css/styles.css',
    '/js/main.js',
    '/js/kanbanService.js',
    '/js/serviceWorker.js'
];

self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(cacheName)
            .then(cache => {
                console.log('Caching files');
                return cache.addAll(cacheAssets);
            })
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', function(e) {
    e.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cache => {
                    if (cache !== cacheName) {
                        console.log('Clearing old cache');
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
    return self.clients.claim();
});

self.addEventListener('fetch', function(e) {
    e.respondWith(
        fetch(e.request).catch(() => caches.match(e.request))
    );
});
