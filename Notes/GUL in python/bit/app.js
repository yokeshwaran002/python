const qrCode = require('qrcode');

document.getElementById('generate-btn').addEventListener('click', function() {
    const inputText = document.getElementById('input-text').value;
    const qrCodeContainer = document.getElementById('qr-code');

    qrCode.toDataURL(inputText, { errorCorrectionLevel: 'H' }, function (err, url) {
        if (err) {
            console.error(err);
            return;
        }
        qrCodeContainer.innerHTML = `<img src="${url}" alt="QR Code" />`;
    });
});