
jQuery(function($) {
    $(document).ready( function() {
        // configure the report options to be an overlay
        var dialogContent = $("#options-dialog").html();
        $("#options-dialog").addClass("overlay overlay-ajax").html(
            '<div class="close"></div><div class="pb-ajax"><div><div>'
            + '</div></div></div>'
        );
        $("#options-dialog .pb-ajax div div").html(dialogContent);

        // define the options dialog overlay
        $(".documentFirstHeading > a").overlay();
    });
});