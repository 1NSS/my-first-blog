/*!
* Start Bootstrap - Heroic Features v5.0.3 (https://startbootstrap.com/template/heroic-features)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-heroic-features/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

function save()  {

    if(fr.comments.value == "") {

        alert("값을 입력해 주세요.");
    
        fr.comments.focus();
    
        return false;
    
      }
    else return true;
}