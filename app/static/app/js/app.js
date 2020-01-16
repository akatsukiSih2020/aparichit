
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "0px";
    document.getElementById("full_body").style.marginLeft = "150px";
}
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.getElementById("full_body").style.marginLeft = "0";
}


// $("#file-picker").change(

  function fileUpload(){

        var input = document.getElementById('file-picker');

        for (var i=0; i<input.files.length; i++)
        {
        //koala.jpg, koala.JPG substring(index) lastIndexOf('a') koala.1.jpg
            var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase()
        
        if (ext == 'csv') 
            {
                $("#msg").text("Files are supported")
            }
            else
            {
                $("#msg").text("Files are NOT supported")
                document.getElementById("file-picker").value ="";
            }
        }
    }
