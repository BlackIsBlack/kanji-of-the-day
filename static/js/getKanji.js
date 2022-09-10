// On page load, get the kanji from the server and display it

jQuery(function() { 

    // Get the kanji from the server
    $.ajax({
        url: "/kanjidata/"+ $("#kanji").text(),
        type: "GET",
        dataType: "json",
        success: function(data) {
            // Display the kanji
            displayKanji(data);
        }
    });
})

function displayKanji(data){
    var template = $('#kanji-meaning').html();
    for (var i = 0; i < 2; i++) {
        // If there are 2 meanings, add 'or' between them
        if (i > 0 && data.meanings.length >= 2) {
            $('#meaninglist').append(' or ');
        }
        var templateScript = Handlebars.compile(template);
        var context = {
            meaning: data.meanings[i]
        };
        var meaningHTML = templateScript(context);
        $('#meaninglist').append(meaningHTML);
    }

    
    try{
        $("#reading").text(data.kunyomi[0]);
    }catch{
        $("#reading").text(data.onyomi[0]);
    }
    $("#spinner").hide();
    $(".kanji-card").show(1000);
}