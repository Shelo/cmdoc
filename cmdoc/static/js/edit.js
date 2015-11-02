const NEW_SECTION_CLASS = '.new-section-button';
var lock = false;
var body = $('html,body');

function makeTemplate() {
    var panel = $('#new-section-template').clone();
    panel.removeAttr("id");
    panel.removeClass('hide');
    panel.find('.cancel-button').click(done);
    $(NEW_SECTION_CLASS).hide();
    lock = true;

    return panel;
}

function done() {
    var panel = $(this).parent().parent().parent().parent();

    cancelEdit(panel.data('id'), function() {
        panel.remove();
        $(NEW_SECTION_CLASS).show();
        lock = false;
    });
}

$(NEW_SECTION_CLASS).click(function () {
    if (lock)
        return;

    var position = $('.section').last().data('position');

    var panel = makeTemplate();
    panel.insertBefore($(this));

    if (position !== undefined)
        panel.find('.position').val(position + 1);

    body.animate({
        scrollTop: panel.offset().top - 60
    });
});


$('.add-before').each(function () {
    $(this).click(function () {
        if (lock)
            return;

        var panel = makeTemplate();

        var before = $(this).parent().parent().prev();
        var position = 0;
        if (before.hasClass('section'))
            position = parseInt(before.data('position')) + 1;

        panel.find('.position').val(position);

        panel.insertBefore($(this).parent().parent());

        body.animate({
            scrollTop: panel.offset().top - 60
        });
    });
});


function confirmEdit(section, data) {
    var panel = makeTemplate();

    var position = parseInt(section.data('position'));

    panel.data('id', section.data('id'));

    panel.find('.position').val(position);
    panel.find('.edit').val("1");
    panel.find('.content').val(section.find('.plaintext').text());
    panel.find('form').attr('action', section.data('edit-url'));
    panel.insertBefore(section);

    body.animate({
        scrollTop: panel.offset().top - 60
    });
}


$('.edit').each(function () {
    $(this).click(function () {
        if (lock)
            return;


        var section = $(this).parent().parent();
        requestEdit(section, parseInt(section.data('id')), confirmEdit);
    });
});


$('#show-messages').click(function () {
    var messagesFrame = $('#messages-frame');
    var inner = messagesFrame.find('.messages-frame');
    messagesFrame.toggle();
    inner.scrollTop(inner.height());
});