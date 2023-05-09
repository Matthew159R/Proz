const popup = document.querySelector('.popup')
const popupLink = document.querySelector('.popup-link')

popupLink.addEventListener('click', () => {
    popup.classList.add('active')
})