async function sendmessage(){
    const userinput=document.getElementById('userinput')
    const usermessage=userinput.value.trim()
    if(usermessage==="")return;
    addmessage("user",usermessage)
    userinput==""
    try{
        const response= await fetch("/bat_ai",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify({message:usermessage})

        })
        const data= await response.json()
        addmessage("ai",data.response)
    }catch(error){
        addmessage('ai'," ERROR IN CONNECTION TRY LATER")
    }

}



function addmessage(sender,text){
    const chatbox= document.getElementById("inputarea")
    const msg= document.createElement("div")
    msg.classList.add(sender)
    msg.innerText=text
    chatbox.appendChild(msg)
    chatbox.scrollTop=chatbox.scrollHeight
}