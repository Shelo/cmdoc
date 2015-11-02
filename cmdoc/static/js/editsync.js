function requestEdit(section, sectionId, callback) {
    $.ajax({
        url: REQUEST_EDIT_URL,
        method: 'POST',
        data: {
            sectionId: sectionId,
            csrfmiddlewaretoken: CSRF_TOKEN
        }
    }).done(function(data) {
        if (data.status) {
            callback(section, data);
        } else {
            alert("Section is being edited by " + data.current);
        }
    });
}

function cancelEdit(sectionId, callback) {
    $.ajax({
        url: CANCEL_EDIT_URL,
        method: 'POST',
        data: {
            sectionId: sectionId,
            csrfmiddlewaretoken: CSRF_TOKEN
        }
    }).done(function(data) {
        if (data.status) {
            callback(data);
        }
    });
}
