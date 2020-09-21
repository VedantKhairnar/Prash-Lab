$(document).ready(function() {
    if ($(window).width() <= 768) {
        $('.not-first').each(function() {
            let prevnode = $(this).parent();
            let node = $(this).clone();
            let parentnode = $("<div class='carousel-item'>");
            $(parentnode).append($(node));
            $(prevnode).after(parentnode);
            $(this).remove();
        });
    }
});
