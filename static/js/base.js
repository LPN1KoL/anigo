function showsearch(value){
    if (value != ''){
        document.getElementById('mod').style.display = 'block'
        const xhr = new XMLHttpRequest()
        xhr.open('GET', '/getsearch')
        xhr.responseType = 'json'
        xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            const status = xhr.status
            if (status === 0 || (status >= 200 && status < 400)) {
                const anims = xhr.response["animes"]
                let div = document.getElementById("anims")
                div.innerHTML = ''
                for (let i = 0; i < anims.length; i++){
                    let anime = anims[i]
                    if (anime.name.startsWith(value)) {
                        div.innerHTML += '<div class="anime modal"><a class="modal" href="ani/' + anime['id'] + '" id="ssilka"><img class="modal" src="' + anime['poster'] + '" alt="" id="poster"><span class="modal" id="aniname">' + anime['name'] + '</span></a></div>'
                        }
                    }
                }
            }
          }
        xhr.send();
        }
    }


document.addEventListener('mousedown', evt => {
    if (evt.target.classList.contains('modal')) {
        evt.preventDefault()
    }
    else {
        document.getElementById('mod').style.display = 'none'
        document.getElementById('search').value = ''
        }
})



