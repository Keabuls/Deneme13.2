/** Variables */
let files = [],
    dragArea = document.querySelector('.drop-area'),
    input = document.querySelector('.drop-area input'),
    container = document.querySelector('.container');

/** INPUT CHANGE EVENT */
input.addEventListener('change', () => {
    let file = input.files;
    
    // Kullanıcı hiçbir resim seçmediyse
    if (file.length === 0) return;
    
    for (let i = 0; i < file.length; i++) {
        // Sadece resim dosyalarını kabul et
        if (file[i].type.split("/")[0] !== 'image') continue;
        
        // Dosya daha önce eklenmemişse listeye ekle
        if (!files.some(e => e.name === file[i].name)) {
            files.push(file[i]);
        }
    }

    showImages();
});

/** SHOW IMAGES */
function showImages() {
    container.innerHTML = files.reduce((prev, curr, index) => {
        return `${prev}
            <div class="image">
                <span onclick="delImage(${index})">&times;</span>
                <img src="${URL.createObjectURL(curr)}" />
            </div>`;
    }, '');
}

/** DELETE IMAGE */
function delImage(index) {
    files.splice(index, 1);
    showImages();
    input.value = '';
}

function submitForm(actionUrl) {
    var form = document.getElementById('upload-form');
    form.action = actionUrl;
    form.submit();
}


/** DRAG & DROP */
/* dragArea.addEventListener('dragover', e => {
    e.preventDefault();
    dragArea.classList.add('dragover');
});
 */
/** DRAG LEAVE */
/* dragArea.addEventListener('dragleave', e => {
    e.preventDefault();
    dragArea.classList.remove('dragover');
}); */

/** DROP EVENT */
/* dragArea.addEventListener('drop', e => {
    e.preventDefault();
    dragArea.classList.remove('dragover');

    let file = e.dataTransfer.files;
    for (let i = 0; i < file.length; i++) {
        // Sadece resim dosyalarını kabul et
        if (file[i].type.split("/")[0] !== 'image') continue;

        // Dosya daha önce eklenmemişse listeye ekle
        if (!files.some(e => e.name === file[i].name)) {
            files.push(file[i]);
        }
    }
    showImages();
}); */

/* ****************************************************** */

/* document.querySelector('.button:nth-of-type(1)').addEventListener('click', () => {
    fetch('/remove-background', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}); */


document.querySelector('.button:nth-of-type(2)').addEventListener('click', () => {
    fetch('/search_result', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    }).catch(error => {
        console.error('Error:', error);
    });
});























