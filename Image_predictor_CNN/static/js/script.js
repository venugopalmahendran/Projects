async function uploadimage() {
    const file_uploaded=document.getElementById("inputfile")
    const file=file_uploaded.files[0]
    if(!file){
        alert("select the images to continue")
    return;
    }
    


    const fromdata=new FormData()
    fromdata.append('image',file)

    const respones=await fetch("http://127.0.0.1:5000/predict",{
        method:'POST',
        body:fromdata
    })
    const data =await respones.json()
    document.getElementById("result").innerText='prediction:'+data.result
}