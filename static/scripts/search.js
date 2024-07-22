document.addEventListener('DOMContentLoaded', () => {
    const ps = document.querySelectorAll('.img-container p');

    ps.forEach(p => {
        const score = parseFloat(p.getAttribute('data-score'));
        let color;

        // Örnek renkleme işlevi
        if (score >= 90 && score <= 100) {
            color = '#fa6e4f'; // Yüksek benzerlik
        } else if (score >= 83 && score <= 90) {
            color = '#FFAF59'; // Orta benzerlik
        } else if (score >= 70 && score <= 82) {
            color = '#bfbb80'; // Düşük benzerlik
        } else {
            color = '#cccccc'; // Çok düşük benzerlik
        }

        p.style.backgroundColor = color;
    });
});
