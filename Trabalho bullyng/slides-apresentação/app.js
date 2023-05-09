const container_imgs = document.querySelector('.container-imgs')
const buttonNext = document.querySelector('.next')
const buttonBack = document.querySelector('.back')

const imgs = Array.from(container_imgs.children)

let countIndex = 0

buttonNext.addEventListener('click', event => {
    countIndex += 1
    buttonNext.disabled = true
    if (countIndex > imgs.length - 1) {
        countIndex = 0
    }else if (countIndex < 0) {
        countIndex = imgs.length - 1
    }

    imgs.forEach((img, index) => {
        if (countIndex === 0) {
            imgs[imgs.length - 1].classList.add('animationBack')
            imgs[0].classList.add('animationTop')
            imgs[0].classList.remove('none')
            imgs[imgs.length - 1].classList.add('none')

            setTimeout(() => {
                buttonNext.disabled = false
            }, 1000)

        }else if (index === countIndex) {
            imgs[countIndex - 1].classList.add('animationBack')
            imgs[countIndex].classList.add('animationNext')
            imgs[countIndex].classList.remove('none')

            setTimeout(() => {
                imgs[countIndex - 1].classList.add('none')

                imgs[countIndex - 1].classList.remove('animationBack')
                imgs[countIndex].classList.remove('animationNext')
                buttonNext.disabled = false
            }, 1000)

        }
        console.log(countIndex)
    })
})

document.addEventListener('keydown', event => {
    if (event.key === 'ArrowRight') {
        
        countIndex += 1
    
    if (countIndex > imgs.length - 1) {
        countIndex = 0
    }else if (countIndex < 0) {
        countIndex = imgs.length - 1
    }

    imgs.forEach((img, index) => {
        if (countIndex === 0) {
            imgs[imgs.length - 1].classList.add('animationBack')
            imgs[0].classList.add('animationNext')
            imgs[0].classList.remove('none')
            imgs[imgs.length - 1].classList.add('none')

        }else if (index === countIndex) {
            imgs[countIndex - 1].classList.add('animationBack')
            imgs[countIndex].classList.add('animationNext')
            imgs[countIndex].classList.remove('none')

            setTimeout(() => {
                imgs[countIndex - 1].classList.add('none')

                imgs[countIndex - 1].classList.remove('animationBack')
                imgs[countIndex].classList.remove('animationNext')
                buttonNext.disabled = false
            }, 1000)

        }
        console.log(countIndex)
    })
    }
})



/*

ArrowRight

*/