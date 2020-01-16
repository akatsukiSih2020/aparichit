
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
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
      (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
      // or any other URL that isn't scheme relative or absolute i.e relative.
      !(/^(\/\/|http:|https:).*/.test(url));
  }
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

function predict(){

    var getChecked = function () {
        return $('#shTable').find('input[type="checkbox"]')
          .filter(':checked')
          .toArray()
          .map(function (x) {
            return $(x).attr('name');
          });
      }
      filename = getChecked();
    //   console.log(students);
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
          if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
          $('#wait').show();
        }
      });
    $.ajax({
        url: 'cluster',
        type: 'POST',
        dataType: "json",
        data: {'file':filename} ,
        complete: function () {
        //   $('#wait').hide();
        },
        success: function (data) {
          //console.log(data);
        //   window.location.reload();
        window.location.href = "cluster";
        }
      });
  
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
