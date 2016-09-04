var $ = jQuery;
$(function() {
	$('#post-form').on('submit', function(event){
    event.preventDefault();
    create_post();
	});

	function create_post() {
  	var token = $('input[name="csrfmiddlewaretoken"]').prop('value');
  	$.ajax({
      url : "/fibonacci/", // the endpoint
      type : "POST", // http method
      data : {
      	number : $('#number').val(),
      	'csrfmiddlewaretoken': token
      }, // data sent with the post request

      // handle a successful response
      success : function(json) {
        $('#number').val('');
        if(json.result == "success") {
          $("#" + json.position).remove()
          $("#recent").prepend("<li id='" + json.position + "'>" +
            json.position + "th fibonacci is <strong>" + json.number +
            "</strong>; query time = " + json.time.toFixed(5) + " sec");
        }
        else {
          alert(json.result);
        }
      },

      // handle a non-successful response
      error : function(xhr, errmsg, err) {
          $('#recent').html('Sorry! Something went wrong.');
          console.log(xhr); // provide a bit more info about the error to the console
      }
    });
	};

});
