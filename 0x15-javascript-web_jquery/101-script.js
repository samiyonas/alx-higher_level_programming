#!/usr/bin/node
$('#add_item').click(function () {
  $('ul.my_list').append("<li>Item</li>");
});
$('#remove_item').click(function () {
  $("ul.mylist li:last-child").remove();
});
$('#clear_list').click(function () {
  $('ul.my_list').empty();
});
