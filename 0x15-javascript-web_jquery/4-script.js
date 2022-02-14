const $ = window.jQuery;
let classValue = $('header').attr('class');
$('DIV#toggle_header').click(function () {
  $('header').removeClass(classValue);
  if (classValue === 'green') {
    classValue = 'red';
  } else {
    classValue = 'green';
  }
  $('header').addClass(classValue);
});
