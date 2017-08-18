function set_data_in_table(data) {
    $('#table-result-head').empty();
    $('#table-result-body').empty();

    var headers = data['headers'];
    var rows = data['rows'];

    var $thr = $('<tr>');
    $.each(headers, function(i, item) {
        $thr.append($('<th>').text(item))
    });
    $thr.appendTo('#table-result-head');

    $.each(rows, function(i, item) {
        var $tr = $('<tr>').append(
            $('<td>').text(item.name),
            $('<td>').append($('<a target="_blank" href="'+item.link+'">'+item.link+'</a>'))
        ).appendTo('#table-result-body');
    });
}
