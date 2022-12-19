document.querySelectorAll('.board').forEach(function (play) {
    play.addEventListener('click', function (e) {
        window.location = '/playing?board=' + e.target.id;
    });
});