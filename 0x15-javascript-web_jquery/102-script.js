#!/usr/bin/node
$(function () {
    $("#btn_translate").click(function() {
        $.ajax({
            type: "GET",
            url: `https://www.fourtonfish.com/hellosalut/?lang=${$("#language_code").val()}`,
            success: function (response) {
                $("#hello").text(response["hello"])
            }
        })
    })
})