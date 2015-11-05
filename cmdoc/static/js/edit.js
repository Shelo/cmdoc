var RequestModule = (function ($) {
    var options = {
        requestEdit: '',
        cancel: '',
        csrfToken: ''
    };

    var init = function (args) {
        options = $.extend(options, args);
    };

    var requestEdit = function (id, success, failure) {
        $.ajax({
            url: options.requestEdit,
            method: 'POST',
            data: {
                sectionId: id,
                csrfmiddlewaretoken: options.csrfToken
            }
        }).done(function(data) {
            if (data.status) {
                success(data);
            } else {
                if (failure) {
                    failure(data);
                } else {
                    alert("Section is being edited by " + data.current);
                }
            }
        });
    };

    var cancelEdit = function (id, success, failure) {
        $.ajax({
            url: options.cancel,
            method: 'POST',
            data: {
                sectionId: id,
                csrfmiddlewaretoken: options.csrfToken
            }
        }).done(function(data) {
            if (data.status) {
                success(data);
            } else {
                if (failure) {
                    failure(data);
                } else {
                    alert("Failed to cancel edition.")
                }
            }
        });
    };

    return {
        init: init,
        requestEdit: requestEdit,
        cancelEdit: cancelEdit
    };
}(jQuery));


var EditModule = (function ($) {
    var body = $('html, body');

    var lockEditor = false;
    var currentEditor;

    var options = {
        addSectionButton: '#add-section',
        sectionClass: '.section',
        sectionsId: '#sections',
        positionInput: '.position',
        sectionRemove: '.section-remove',
        template: {
            base: '#editor-template',
            cancel: '.cancel-button'
        },
        editButton: '.edit-button',
        addBefore: '.add-before'
    };

    var init = function (config) {
        options = $.extend(options, config);

        $(options.addSectionButton).click(createEditor);

        // ask the user if he/she really wants to remove the section.
        $(options.sectionRemove).click(function () {
            if (confirm('Are you sure?')) {
                window.location.href = $(this).data('href');
            }
        });

        $(options.editButton).click(function () {
            createEditorFromEditButton($(this).parent().parent());
        });

        $(options.addBefore).click(function () {
            createEditorFromAddBefore($(this).parent().parent());
        });
    };

    var createEditorFromAddBefore = function (section) {
        if (lockEditor)
            return;

        lockEditor = true;

        var id = section.data('id');
        var before = section.prev();
        var position = 0;

        if (before.hasClass(options.sectionClass.replace('.', ''))) {
            position = parseInt(before.data('position')) + 1;
        }

        currentEditor = new Editor(id, position, function (editor, panel) {

            panel.insertBefore(section);

        }, function (editor, panel) {

            panel.remove();
            editor.reset();

        });
    };

    var createEditorFromEditButton = function (section) {
        if (lockEditor)
            return;

        lockEditor = true;

        var id = section.data('id');
        var position = section.data('position');

        RequestModule.requestEdit(id, function (data) {
            currentEditor = new Editor(id, position, function (editor, panel) {
                panel.insertBefore(section);
                panel.find('textarea').val(data.content);
                panel.find('form').attr('action', section.data('edit-url'));
            }, function (editor, panel) {
                RequestModule.cancelEdit(id, function () {
                    panel.remove();
                    editor.reset();
                });
            });
        });
    };

    var createEditor = function () {
        if (lockEditor)
            return;

        lockEditor = true;

        currentEditor = new Editor(-1, -1, function (editor, panel) {
            $(options.sectionsId).append(panel);
        }, function (editor, panel) {
            panel.remove();
            editor.reset();
        });
    };

    /***
     * Creates a new editor.
     *
     * @param id            id of the section to edit.
     * @param position      position of the section within the document.
     * @param ready         a callback(editor, panel) to add this to the DOM.
     * @param cancel        a callback(editor, panel) to call when the user cancels the edition.
     */
    var Editor = function (id, position, ready, cancel) {
        this.position = position;
        this.id = id;
        this.cancel = cancel;

        // create the panel from the base and modify some attributes.
        this.panel = $(options.template.base).clone();
        this.panel.removeAttr('id');
        this.panel.show();

        // bind the cancel callback to the cancel button.
        this.panel.find(options.template.cancel).click((function () {
            this.cancel(this, this.panel)
        }).bind(this));

        this.panel.find(options.positionInput).val(position);

        ready(this, this.panel);

        body.animate({
            scrollTop: this.panel.offset().top - 60
        });

        // hide the add section button to avoid conflicts.
        $(options.addSectionButton).hide();

        this.reset = function () {
            $(options.addSectionButton).show();
            lockEditor = false;
        };
    };

    return {
        init: init
    };
}(jQuery));
