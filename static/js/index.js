document.addEventListener("DOMContentLoaded", () => {
    const swiper = new Swiper(".swiper", {
        direction: "horizontal",
        loop: false,
        slidesPerView: 3,
        spaceBetween: 20,

        watchOverflow: true, // 🔥 Esta línea evita el desplazamiento cuando ya no hay más tarjetas

        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },

        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },

        scrollbar: {
            el: ".swiper-scrollbar",
        },

        autoplay: false,

        breakpoints: {
            1024: {
                slidesPerView: 3,
            },
            768: {
                slidesPerView: 2,
            },
            480: {
                slidesPerView: 1,
            },
        },
    });
});


document.addEventListener("DOMContentLoaded", () => {
    // Función para obtener el año actual y establecerlo en el elemento correspondiente
    const currentYearElement = document.querySelector("#current-year");
    if (currentYearElement) {
        currentYearElement.textContent = new Date().getFullYear();
    }

    // Ajuste del tamaño de la fuente para el título si existe el elemento
    const tituloElement = document.querySelector(".layout__logo h1"); // Asegúrate de que sea el selector correcto
    if (tituloElement) {
        tituloElement.style.fontSize = "24px";
    }
});


window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scrollToTopBtn").style.display = "block";
    } else {
        document.getElementById("scrollToTopBtn").style.display = "none";
    }
}

function scrollToTop() {
    document.body.scrollTop = 0; // Para Safari
    document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE y Opera
}


function toggleMenu() {
    const menuList = document.getElementById('menuList');
    const isOpen = menuList.classList.toggle('menu-open'); // Alterna clase de apertura
    document.querySelector('.layout__icons i').classList.toggle('fa-times'); // Cambia el ícono
}


var currentIndex = 0;
var images = [];

document.addEventListener("DOMContentLoaded", function () {
    // Recolectar todas las URLs de las imágenes en el arreglo images
    images = Array.from(document.querySelectorAll(".services__galeria img")).map(img => img.src);
});

function fullView(imageElement) {
    // Obtener el índice desde el atributo data-index del elemento clickeado
    currentIndex = imageElement.getAttribute('data-index');
    // Mostrar la imagen ampliada en el contenedor
    document.getElementById("fullImage").src = images[currentIndex];
    document.getElementById("fullImageView").style.display = "flex";
}

function closeFullView() {
    document.getElementById("fullImageView").style.display = "none";
}

function prevImage() {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
    document.getElementById("fullImage").src = images[currentIndex];
}

function nextImage() {
    currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
    document.getElementById("fullImage").src = images[currentIndex];
}
