

function setback(button_id) {
    console.log("add to bookmarl",button_id);
  $("#"+button_id).text("Add to Bookmark");
}
 function search_value(){

     let search_input = document.getElementById('search_input').value;
    console.log(search_input);
    let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

  $.ajax({
  url: '/store_search/',
  method : 'POST',
         headers: {
           'X-CSRFToken': csrfToken
         },
  data: {"search_input": search_input},
  beforeSend: function() {
   // things to do before submit
  },
  success: function(data) {


   }
   });

}
function addToBookmark() {
    // console.log($(this).attr("id"));

    let buttonId = event.srcElement.value;
    console.log(buttonId);
    let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

  $.ajax({
  url: '/bookmarks/add_bookmark/',
  method : 'POST',
         headers: {
           'X-CSRFToken': csrfToken
         },
  data: {"button_id": buttonId},
  beforeSend: function() {
   // things to do before submit
  },
  success: function(data) {
      console.log(data);
      button_id = data.data
      if (data.response == "added")
      {
    console.log("added");
          $("#"+button_id).text("Added Successfuly");
          // $("#bookmarked"+button_id).css("background","green");
          setTimeout("setback(button_id)", 1000);
      }
      else
      {

    console.log("exist");
          $("#"+button_id).text("Already Exist");
          setTimeout("setback(button_id)", 1000);
      }


   }
   });
    
}


 function readMoreBooklist(){

    let buttonId = event.srcElement.value;
    console.log(buttonId);
    let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

  $.ajax({
  url: '/read_more/',
  method : 'POST',
         headers: {
           'X-CSRFToken': csrfToken
         },
  data: {"button_id": buttonId},
  beforeSend: function() {
   // things to do before submit
  },
  success: function(data) {
      let books = data.data;
      console.log(books.title);
      $('#info-modal .modal-body ').html(`
  <div class="card-modal"><img class="image-modal" src=${books.image}>
    <div class="info-modal">
      <h4>${books.title}</h4>
<table class="table table-striped align-middle">
  <tbody>
    <tr>
      <td colspan="2">Price</td>
      <td colspan="2">${books.price}</td>
    </tr>
    <tr>
      <td colspan="2">Rating</td>
      <td colspan="2">${books.rating}/5</td>
    </tr>
    <tr>
      <td colspan="2">Author</td>
      <td colspan="2">${books.authors}</td>
    </tr>
    <tr>
      <td colspan="2">Published</td>
      <td colspan="2">${books.year}</td>
    </tr>
    <tr>
      <td colspan="2">Pages</td>
      <td colspan="2">${books.pages}</td>
    </tr>
    <tr>
      <td colspan="2">ISBN-10</td>
      <td colspan="2">${books.isbn10}</td>
    </tr>
    <tr>
      <td colspan="2">ISBN-13</td>
      <td colspan="2">${books.isbn13}</td>
    </tr>
    <tr>
      <td colspan="2">Description</td>
      <td colspan="2">${books.desc}</td>
    </tr>
  </tbody>
</table>
      <button id="${books.isbn13}" type="button" class="btn btn-dark card-button" value="${books.isbn13}" onclick="addToBookmark()">Add to Bookmark</button>

    </div>
  </div>
`);
      $('#info-modal').modal('show');

   }
   });
 }

  $("#info-modal").on("hidden.bs.modal", function () {
      $( ".card-button" ).remove();
});

function deleteBookmark() {
    // console.log($(this).attr("id"));
    let buttonId = event.srcElement.id;
    let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
    // let current = current_page;

  $.ajax({
  url: '/bookmarks/delete_bookmark/',
  method : 'POST',
         headers: {
           'X-CSRFToken': csrfToken
         },
      data: {"button_id": buttonId},
  beforeSend: function() {
   // things to do before submit
  },
  success: function(data) {
      console.log(data.response);
 $('#book'+data.response).remove();
      $('#info-modal').modal('hide');
// location.reload(); 
   }
   });
    
}
  

  
 function readMoreBookmark(){

    let buttonId = event.srcElement.value;
    console.log(buttonId);
    let cookie = document.cookie
let csrfToken = cookie.substring(cookie.indexOf('=') + 1)

  $.ajax({
  url: '/read_more/',
  method : 'POST',
         headers: {
           'X-CSRFToken': csrfToken
         },
  data: {"button_id": buttonId},
  beforeSend: function() {
   // things to do before submit
  },
  success: function(data) {
      let books = data.data;
      console.log(books.title);
      $('#info-modal .modal-body ').html(`
  <div class="card-modal"><img class="image-modal" src=${books.image}>
    <div class="info-modal">
      <h4>${books.title}</h4>
<table class="table table-striped align-middle">
  <tbody>
    <tr>
      <td colspan="2">Price</td>
      <td colspan="2">${books.price}</td>
    </tr>
    <tr>
      <td colspan="2">Rating</td>
      <td colspan="2">${books.rating}/5</td>
    </tr>
    <tr>
      <td colspan="2">Author</td>
      <td colspan="2">${books.authors}</td>
    </tr>
    <tr>
      <td colspan="2">Published</td>
      <td colspan="2">${books.year}</td>
    </tr>
    <tr>
      <td colspan="2">Pages</td>
      <td colspan="2">${books.pages}</td>
    </tr>
    <tr>
      <td colspan="2">ISBN-10</td>
      <td colspan="2">${books.isbn10}</td>
    </tr>
    <tr>
      <td colspan="2">ISBN-13</td>
      <td colspan="2">${books.isbn13}</td>
    </tr>
    <tr>
      <td colspan="2">Description</td>
      <td colspan="2">${books.desc}</td>
    </tr>
  </tbody>
</table>
      <button id="${books.isbn13}" type="button" class="btn btn-dark" value="${books.isbn13}" onclick="deleteBookmark()">Delete Bookmark</button>
    </div>
  </div>
`);
      $('#info-modal').modal('show');

   }
   });
 }
