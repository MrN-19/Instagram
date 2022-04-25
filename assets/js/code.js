function LikePost(code) {
    let csrf = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    $.ajax({
        url: "/like-post",
        type: "POST",
        data: {
            code: code,
            csrfmiddlewaretoken: csrf
        },
        success: function (res) {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 2000,
            });
            if (res.like == true) {
                document.getElementById("like-heart-color" + code).style.fill = "red";
            }
            else {
                document.getElementById("like-heart-color" + code).style.fill = "black";
            }
        },
        error: function (res) {
            let data = JSON.parse(res.responseText);
            iziToast.error({
                message: data.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        }
    })
}

function SavePost(code) {
    let csrf = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    $.ajax({
        url: "/save-post",
        type: "POST",
        data: {
            code: code,
            csrfmiddlewaretoken: csrf
        },
        success: function (res) {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 2000,
            });
            let save_element = document.getElementById("save-post-color" + code);
            if (res.saved == true) {
                save_element.style.fill = "red";
            }
            else {
                save_element.style.fill = "black";
            }
        },
        error: function (res) {
            let data = JSON.parse(res.responseText);
            iziToast.error({
                message: data.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        }
    })
}

function StartWaiting() {
    let img_waiting = document.getElementById("img-waiting");
    img_waiting.style.display = "inline-block";
    img_waiting.src = "/assets/img/dark-loader.gif";

}
function StopWaiting() {
    let img_waiting = document.getElementById("img-waiting");
    img_waiting.style.display = "none";
}

function GetFollowersToSharePost(postid) {
    StartWaiting();
    $.ajax({
        url: "/share-post-user",
        type: "GET",
        success: function (res) {
            let usernames = res.data;
            for (let i = 0; i < usernames.length; i++) {
                let li_username = document.createElement("li");
                li_username.id = "each_users_" + i;

                let img_user_picture = document.createElement("img");
                img_user_picture.id = "each_img" + i;
                img_user_picture.style.borderRadius = "50px";
                img_user_picture.style.width = "40px";
                img_user_picture.style.height = "40px";
                img_user_picture.style.marginRight = "12px";

                let check_to_send = document.createElement("input");
                check_to_send.value = usernames[i];
                check_to_send.id = "user_" + i;
                check_to_send.className = "user";
                check_to_send.type = "checkbox";
                check_to_send.style.margin = "10px 12px";

                document.querySelector("button.btn-send-post-other-directs").id = postid;

                let ul_list = document.getElementById("ul_list");
                $.ajax({
                    url: "/usernamepicture/" + usernames[i],
                    type: "GET",
                    success: function (res) {
                        img_user_picture.src = res.picture;
                        li_username.innerHTML = usernames[i];
                        li_username.append(img_user_picture);
                        li_username.append(check_to_send);

                        ul_list.appendChild(li_username);
                        console.log(ul_list);
                    },
                    error: function (err) {
                        console.log(err);
                    }
                })
            }
            StopWaiting();
        },
        error: function (res) {
            let data = JSON.parse(res.responseText);
            iziToast.error({
                message: data.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        }
    });
}

function ShowComments(code) {
    // Not Complete Share and Comment
    let once = document.getElementById("session_once_state").value;
    document.getElementById("postid_comment").value = code;
    $.ajax({
        url: "comments/" + code,
        type: "GET",
        success: function (res) {
            let data = JSON.parse(res.data);
            console.log(data[0].fields);
            for (let i = 0; i < data.length; i++) {
                // Image
                let image = document.createElement("img");
                image.style.borderRadius = "50px";
                image.style.width = "40px";
                image.style.height = "40px";
                image.style.margin = "10px";
                // End Image

                // li user name
                let li_username = document.createElement("li");
                li_username.className = "cursor-pointer";
                li_username.id = "user-commented_" + data[i].fields.user;
                li_username.addEventListener("click", function () {
                    let id = this.id.substring(15);
                    document.getElementById("header_comment").value = id;
                });
                // end li username

                // p comment User Name
                let comment = document.createElement("p");
                comment.innerHTML = data[i].fields.comment;
                // End p comment UserName

                let ul_list = document.querySelector("ul.comment-list");
                $.ajax({
                    url: "/user/" + data[i].fields.user,
                    type: "GET",
                    success: function (res) {
                        console.log(res);
                        li_username.innerHTML = res.username;
                        image.src = res.picture;
                        li_username.append(image);
                        li_username.append(comment);
                        ul_list.appendChild(li_username);
                    },
                    error: function (res) {
                        iziToast.error({
                            message: res.text,
                            position: 'bottomRight',
                            timeout: 3000,
                        });
                    }
                })
            }
        },
        error: function (res) {
            iziToast.error({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        },
    });
}

function SharePost() {
    let users = document.querySelectorAll("input[type=checkbox].user");
    let postid = document.querySelector("button.btn-send-post-other-directs").id;
    let usernames = [];
    for (let i = 0; i < users.length; i++) {
        if (users[i].checked == true) {
            usernames.push(
                users[i].value
            );
        }

    }
    if (usernames.length > 0) {
        $.ajax({
            url: "/direct/share",
            type: "POST",
            data: {
                users: usernames,
                csrfmiddlewaretoken: document.querySelector("input[name=csrfmiddlewaretoken]").value,
                postid: postid,
            },
            success: function (res) {
                iziToast.success({
                    message: res.text,
                    position: 'bottomRight',
                    timeout: 3000,
                });
            },
            error: function (res) {
                iziToast.error({
                    message: res.text,
                    position: 'bottomRight',
                    timeout: 3000,
                });
            }
        });
    }
    else {
        iziToast.error({
            message: "لطفا کاربران را انتخاب کنید",
            position: 'bottomRight',
            timeout: 3000,
        });
    }
}

function SetComment() {
    let comment_text = document.getElementById("comment_text");
    let header = document.getElementById("header_comment");
    let postid = document.getElementById("postid_comment").value;
    if (comment_text.value !== "" && comment_text.value !== undefined && comment_text.value != null) {
        $.ajax({
            url: "set-comment/" + comment_text.value + "/" + postid + "/" + header,
            type: "GET",
            success: function (res) {
                iziToast.success({
                    message: res.text,
                    position: 'bottomRight',
                    timeout: 3000,
                });
            },
            error: function (res) {
                iziToast.error({
                    message: res.text,
                    position: 'bottomRight',
                    timeout: 3000,
                });
            }
        });
    }
    else {
        iziToast.error({
            message: "لطفا متن نظر را وارد کنید",
            position: 'bottomRight',
            timeout: 3000,
        });
    }
}

function PostDetail(code) {
    let post_code_post_detail = document.getElementById("post_detail_post_code");
    alert(code);
    post_code_post_detail.value = code;
}

function UnFollowByPost() {
    let post_code_post_detail = document.getElementById("post_detail_post_code");
    alert(post_code_post_detail.value);
    $.ajax({
        url: "/request-action",
        type: "POST",
        data: {
            "code": post_code_post_detail.value,
            csrfmiddlewaretoken: document.querySelector("input[name=csrfmiddlewaretoken]").value,
            "type": "unfollow",
        },
        success: function (res) {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        },
        error: function (res) {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        },
    });
}
function FollowByPost() {
    let post_code_post_detail = document.getElementById("post_detail_post_code");
    $.ajax({
        url: "/request-action",
        type: "POST",
        data: {
            code: post_code_post_detail.value,
            csrfmiddlewaretoken: document.querySelector("input[name=csrfmiddlewaretoken]").value,
            type: "unfollow",
        },
        success: function (res) {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        },
        error: function (res) {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        },
    });
}
function Block() {
    let post_code_post_detail = document.getElementById("post_detail_post_code");
    $.ajax({
        url : "/block-user-post",
        type : "POST",
        data : {
            "code" : post_code_post_detail.value,
            csrfmiddlewaretoken: document.querySelector("input[name=csrfmiddlewaretoken]").value,
        },
        success : function(res)
        {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        },
        error : function(res)
        {
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 3000,
            });
        }
    })
}