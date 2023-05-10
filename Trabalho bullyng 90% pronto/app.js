const buttonChatConversation = document.querySelector('.button-conversation')
const containerChat = document.querySelector('.content-chat')
const ChatConversation = document.querySelector('.chat-conversation')
const buttonRelato = document.querySelector('.button-relato')
const chatRelato = document.querySelector('.chat-relato')
const closeButton = document.querySelector('.close')
const submitButtonRelato = document.querySelector('.submit')

buttonChatConversation.addEventListener('click', event => {
    containerChat.classList.add('content-chat-animation')

    setTimeout(() => {
        containerChat.classList.add('class-none')
        ChatConversation.style.display = 'flex'
        ChatConversation.classList.add('chat-conversationAnimation')
    }, 1000)
})

buttonRelato.addEventListener('click', event => {
    containerChat.classList.remove('content-chat-animation-reverse')
    containerChat.classList.add('content-chat-animation')

    setTimeout(() => {
        containerChat.classList.add('class-none')
        chatRelato.style.display = 'flex'
        chatRelato.classList.remove('chat-relatoAnimationReverse')
        chatRelato.classList.add('chat-conversationAnimation')
    }, 1000)
})

closeButton.addEventListener('click', event => {
    chatRelato.classList.remove('chat-conversationAnimation')
    chatRelato.classList.add('chat-relatoAnimationReverse')

    setTimeout(() => {
        chatRelato.style.display = 'none'
        containerChat.classList.remove('class-none')
        containerChat.classList.remove('content-chat-animation')
        containerChat.classList.add('content-chat-animation-reverse')

    }, 1000)
})

submitButtonRelato.addEventListener('click', event => {

    chatRelato.classList.remove('chat-conversationAnimation')
    chatRelato.classList.add('chat-relatoAnimationReverse')

    setTimeout(() => {
        chatRelato.style.display = 'none'
        containerChat.classList.remove('class-none')
        containerChat.classList.remove('content-chat-animation')
        containerChat.classList.add('content-chat-animation-reverse')

    }, 1000)

    const nameInput = document.querySelector('#name')
    const emailInput = document.querySelector('#email')
    const textarea = document.querySelector('textarea')

    const inputValues = [nameInput.value.trim(), emailInput.value.trim(), textarea.value.trim()]

    const relatosContainer = document.querySelector('.all-relatos-container')

    const relato = `<div class="relato-container">
                        <div class="foto-name">
                            <img src="/imgs-index/aninumu.png" width="100px" height="50px" alt="">
                            <p class="name-user">${!inputValues[0] ? 'Anônimo' : inputValues[0]}</p>
                        </div>
                        <p class="text-relato">${inputValues[2]}</p>
                        <p class="date">Postado há <span>1</span> segundo atrás</p>
                    </div>`

    relatosContainer.insertAdjacentHTML('afterbegin', relato)
    nameInput.value = ''
    emailInput.value = ''
    textarea.value = ''


})


/*

<div class="relato-container">
                <div class="foto-name">
                    <img src="/imgs-index/aninumu.png" width="100px" height="50px" alt="">
                    <p class="name-user">Anônimo</p>
                </div>
                <p class="text-relato">O meu filho de 9 anos costumava ser animado na escola, mas recentemente começou a ser chamado de "bebezinho" pelos colegas, o que o deixou muito triste e choroso. Tudo o que ele fazia, incluindo sua garrafinha, capa de caderno e mochila, era motivo de zombaria. Ele queria mudar de escola e até pediu para trocar todo o seu material. A família procurou ajuda de um psicólogo e informou a escola sobre o problema. Com conversas e empatia, a situação foi controlada e ele está bem agora.</p>
                <p class="date">Postado há 3 dias</p>
            </div>

*/