
    // prevent enter key from submit the comment form
    //     document.getElementById('id_comment_content').addEventListener('keypress', function (event)
    //     {
    //         // enterkey
    //         if (event.keyCode == 13) {
    //             event.preventDefault();
    //         }
    //     });

    // for make the textarea extends with each enter
    $('#id_comment_content').on("keyup", function () {
        var maxrows = 10;
        var txt = this.value;
        var cols = this.cols;

        var arraytxt = txt.split('\n');
        var rows = arraytxt.length;

        for (i = 0; i < arraytxt.length; i++) {
            rows += parseInt(arraytxt[i].length / cols);
        }

        if (rows > maxrows) {
            this.rows = maxrows;
        }
        else {
            this.rows = rows;
        }
    });

    var like_status = "";

    $(".like").on("click", function (event) {

        if ($(".like-text").html() == "like") {
            if ($(".dislike-text").html() == "disliked") {
                $(".dislike-text").html("dislike");
                $("#dislikecount").html(parseInt($("#dislikecount").html()) - 1);

            }
            $(".like-text").html("liked");
            $("#likecount").html(parseInt($("#likecount").html()) + 1);
        }
        else {
            $(".like-text").html("like");
            $("#likecount").html(parseInt($("#likecount").html()) - 1);
        }


        var url = window.location + "/like/";
        ///alert(url);
        $.ajax({
            url: url,
            success: function () {
                //alert("like done");
            }
        });


    });

    $(".dislike").on("click", function (event) {

        if ($(".dislike-text").html() == "dislike") {
            if ($(".like-text").html() == "liked") {
                $(".like-text").html("like");
                $("#likecount").html(parseInt($("#likecount").html()) - 1);
            }
            $(".dislike-text").html("disliked");
            $("#dislikecount").html(parseInt($("#dislikecount").html()) + 1);

        }
        else {
            $(".dislike-text").html("dislike");
            $("#dislikecount").html(parseInt($("#dislikecount").html()) - 1);
        }

        var url = window.location + "/dislike/";
        //alert(url);
        $.ajax({
            url: url,
            success: function () {
                // alert("dislike done");
            }
        });

    });
