window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        const target = event.target;
        console.log(target.name);
        console.log(target.value);

        $.ajax({
            url: "/baskets/edit/" + target.name + "/" + target.value + "/",
            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
    });
}
