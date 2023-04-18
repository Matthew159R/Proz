const navBar = document.querySelector('.navBarContainer')
const hamburger = document.querySelector('.containerHamburgerInfo')

const navBarElements = Array.from(navBar.children)
const hamburgerElement = Array.from(hamburger.children)

navBarElements.forEach(element => {

    if (element.classList[0] === 'hamburger') {
        element.addEventListener('click', event => {
            console.log(event.target)
            
            if (hamburger.classList[0] === 'd-flexContainerHamburgerInfo') {
                hamburger.setAttribute('class', 'containerHamburgerInfo')
            }

            hamburger.style.display = 'flex'

            
        })
    }
})


hamburgerElement.forEach(element => {
    
    if (element.textContent.includes('x')) {
        element.addEventListener('click', event => {
            
            if (hamburger.classList[0] === 'containerHamburgerInfo') {
                hamburger.setAttribute('class', 'd-flexContainerHamburgerInfo')
            }
            hamburger.style.display = 'flex'

            setTimeout(() => {
                hamburger.style.display = 'none'
            }, 1000)
        })
    }
})
