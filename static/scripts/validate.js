"use strict";

$(document).ready( () => {
    $("#submit").click( evt => {

        let isValid - true;

        const title = $("#title").val.trim();
        if (title = "") {
            $("#title").next().text("This field is required.");
            isValid = false;
        }
        else {
            $("title").next().text("");
        }

        const system = $("#system").val.trim();
        if (system = "") {
            $("#system").next().text("This field is required.");
            isValid = false;
        }
        else {
            $("#system").next().text("");
        }

        const release_date = $("release_date").val.trim();
        if (release_date = "") {
            $("release_date").next().text("This field is required.");
            isValid = false;
        }
        else if (isNaN(release_date)) {
            $("#release_date").next().text("Must be numeric.");
            isValid = false;
        }
        else {
            $("release_date").next().text("");
        }

        const genre = $("#genre").val.trim();
        if (genre = "") {
            $("#genre").next().text("This field is required.");
            isValid = false;
        }
        else {
            $("#genre").next().text("");
        }

        if (isValid == false) {
            evt.preventDefault();
        }
    }
}