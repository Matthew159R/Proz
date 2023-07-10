const classExercise = {
    exercise1 () {
        let i = 11
        while(i > 1) {
            i--
            console.log(i)
        }
    },

    exercise2 () {
        const date = new Date()
        const day = date.getDay()
        const fullYear = date.getFullYear()
        console.log(fullYear)
        return day
    },

    exercise3 () {
        switch(this.exercise2()) {
            case 0:
                console.log('Domingo')
                break
            case 1:
                console.log('Segunda feira')
                break
            case 2:
                console.log('Terça feira')
                break
            case 3:
                console.log('Quarta feira')
                break
            case 4:
                console.log('Quinta feira')
                break
            case 5:
                console.log('Sexta feira')
                break
            case 6:
                console.log('Sábado')
                break

        }
    },

    exercise4 (number) {
        let fatorial = 1
        for (let i = number; i > 0; i--) {
            fatorial = i * fatorial
        }
        resultExercises[0].textContent = `O fatorial de !${number} = ${fatorial}`
        console.log(fatorial)
    },

    exercise5 (number) {
        let fibonacciBack = 1
        let fibonacci = 0
        const arrayFibonacciSequence = []

        for(let i = 0; i < number; i++) {
            arrayFibonacciSequence.push(fibonacci)
            fibonacci = fibonacciBack + fibonacci
            fibonacciBack = fibonacci - fibonacciBack
        }
        
        arrayFibonacciSequence.forEach(numberArrayFibonacciSequence => {
            console.log(numberArrayFibonacciSequence)
        })
        resultExercises[1].textContent = arrayFibonacciSequence.join(', ')
        console.log(arrayFibonacciSequence)
        
    },

    exercise6 (string) {
        const stringReverse = []

        for(let i = 1; i < string.length + 1; i++) {
            stringReverse.push(string[string.length - i])
        }

        let match = 0

        for(j = 0; j < stringReverse.length; j++) {
            if (string[j] === stringReverse[j]) {
                match++
            }
        } 
        
        if (match === string.length) {
            console.log(`"${string}" é um palíndromo`)
        }else {
            console.log(`"${string}" não é um palíndromo`)
        }

    }
} 

const resultExercisesElementDom = document.querySelector('.result-exercises')
const resultExercises = Array.from(resultExercisesElementDom.children)

classExercise.exercise1()
console.log('')
classExercise.exercise2()
console.log('')
classExercise.exercise3()
console.log('')
classExercise.exercise4(5)
console.log('')
classExercise.exercise5(14)
console.log('')
classExercise.exercise6('kaiak')
classExercise.exercise6('Hello world')