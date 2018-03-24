function hi()
{
return function()
{
var url = document.URL;

var check = url.slice(0,31)

if(check=="https://www.wittyfeed.com/story")
window.location = "http://192.168.2.12/witty/";
};
}

    $('#headingTags').html(
    '<div class="roundbox sidebox" style="" align="right">' +
        '<div class="roundbox-lt" >&nbsp;</div>' +
        '<div class="roundbox-rt" >&nbsp;</div>' +
        '<table class="rtable ">' +
            '<tbody>' +
                '<tr><th class="left" style="width:100%;"><a style="color: black" href="">Videofy</a></th></tr>' +
                '<tr>' +
                    '<td class="left bottom" colspan="1">' +
                      '<div style="text-align:right;margin:1em;" id="code_now_button_box">' +
                      '</div>' +
                    '</td>' +
                '</tr>' +
            '</tbody>' +
        '</table>' +
    '</div>');

        var button = $('<button/>', {
            text : 'Go to main website. This Way',
	    click: hi()
        });
        $('#code_now_button_box').append(button);
       
    
    console.log("Button Added !!");
