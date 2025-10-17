/**
 * Secure Image Loader usando Web Workers
 * Carrega imagens de forma que não seja possível acessar a URL original
 */

class SecureImageLoader {
    constructor() {
        this.worker = null;
        this.initWorker();
    }

    initWorker() {
        // Criar Web Worker inline
        const workerCode = `
            self.onmessage = function(e) {
                const { imageUrl } = e.data;
                
                fetch(imageUrl)
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Failed to load image');
                        }
                        return response.blob();
                    })
                    .then(blob => {
                        // Converter blob para ArrayBuffer
                        const reader = new FileReader();
                        reader.onload = function() {
                            self.postMessage({
                                success: true,
                                imageData: reader.result,
                                type: blob.type
                            });
                        };
                        reader.readAsArrayBuffer(blob);
                    })
                    .catch(error => {
                        self.postMessage({
                            success: false,
                            error: error.message
                        });
                    });
            };
        `;

        const blob = new Blob([workerCode], { type: 'application/javascript' });
        this.worker = new Worker(URL.createObjectURL(blob));
    }

    loadImage(imageUrl, canvas) {
        return new Promise((resolve, reject) => {
            if (!this.worker) {
                reject(new Error('Worker not initialized'));
                return;
            }

            const handleMessage = (e) => {
                const { success, imageData, type, error } = e.data;
                
                if (success) {
                    try {
                        // Converter ArrayBuffer de volta para Blob
                        const blob = new Blob([imageData], { type });
                        const blobUrl = URL.createObjectURL(blob);
                        
                        // Criar imagem temporária
                        const img = new Image();
                        img.onload = () => {
                            // Desenhar no canvas
                            const ctx = canvas.getContext('2d');
                            canvas.width = img.naturalWidth;
                            canvas.height = img.naturalHeight;
                            ctx.drawImage(img, 0, 0);
                            
                            // Limpar recursos
                            URL.revokeObjectURL(blobUrl);
                            img.onload = null;
                            img.onerror = null;
                            
                            resolve();
                        };
                        
                        img.onerror = () => {
                            URL.revokeObjectURL(blobUrl);
                            reject(new Error('Failed to load image into canvas'));
                        };
                        
                        img.src = blobUrl;
                        
                    } catch (error) {
                        reject(error);
                    }
                } else {
                    reject(new Error(error || 'Failed to load image'));
                }
                
                // Limpar listener
                this.worker.removeEventListener('message', handleMessage);
            };

            this.worker.addEventListener('message', handleMessage);
            this.worker.postMessage({ imageUrl });
        });
    }

    destroy() {
        if (this.worker) {
            this.worker.terminate();
            this.worker = null;
        }
    }
}

// Exportar para uso global
window.SecureImageLoader = SecureImageLoader;
