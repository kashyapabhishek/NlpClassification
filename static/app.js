$(document).ready(function(){
    $('#testResultSection, #testResultSectionLoader, #trainResultSectionLoader, #trainResponse').hide()
})

$("#TestFormSubmit").click( function (event)
{
    $('#testResultSectionLoader').show()
    text = $('#testText').val()
    data = {"text": text}
    $.ajax({
      type: "POST",
      url: "/test",
      data: data,
      success: function (response) {
            console.log(response)
             $('#testResultSectionLoader').hide()
            $('#testResultSection').show()
            $('#testResponse').text(response)
           // You will get response from your PHP page (what you echo or print)
        },
        error: function(jqXHR, textStatus, errorThrown) {
         $('#testResultSectionLoader').hide()
           console.log(textStatus, errorThrown);
        }
    });
});

$('#trainButton').click(function(event){
    $("#trainResultSectionLoader").show()
    data = {"text": 'train'}
    $.ajax({
      type: "POST",
      url: "/train",
      data: data,
      success: function (response) {
            console.log(response)
             $('#trainResultSectionLoader, #trainButton').hide()
            $('#trainResponse').show()
            $('#trainResponse').text(response)
           // You will get response from your PHP page (what you echo or print)
        },
        error: function(jqXHR, textStatus, errorThrown) {
         $('#trainResultSectionLoader').hide()
           console.log(textStatus, errorThrown);
        }
    });
});