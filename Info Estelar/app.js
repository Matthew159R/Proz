const navBar = document.querySelector('.navBarContainer')
const hamburger = document.querySelector('.containerHamburgerInfo')

const navBarElements = Array.from(navBar.children)
const hamburgerElement = Array.from(hamburger.children)

navBarElements.forEach(element => {

    if (element.textContent.includes('Info estelar')) {
        element.addEventListener('click', () => {
            location.reload()
        })
    }

    if (element.classList[0] === 'hamburger') {
        element.addEventListener('click', event => {
            console.log(event.target)
            
            if (hamburger.classList[0] === 'd-flexContainerHamburgerInfo') {
                hamburger.setAttribute('class', 'containerHamburgerInfo')
            }

            hamburger.style.display = 'flex'

        })
    }
    
    if (element.classList[0] === 'home') {
        element.addEventListener('click', event => {
            scrollTo(0, 0)
        })
        
    }

    if (element.classList[0] === 'matters') {
        element.addEventListener('click', event => {
            scrollTo(500, 500)
        })
    }

    
})


hamburgerElement.forEach(element => {
    
    if (element.textContent.includes('x') || element.classList[0] === 'homeHamburgerInfo') {
        
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

    if (element.classList[0] === 'mattersHamburgerInfo') {
        element.addEventListener('click', event => {
            scrollTo(500, 500)

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
