
$(document).on('submit', '#InvitationForm', function(event){
    event.preventDefault();
});

function invitationButtonClicked(button)
{
    console.log("Button is clicked");
    buttonName = button.getAttribute("name");
    value = button.getAttribute("value");
    console.log("Button name = " + buttonName);
    console.log("Button value = " + value);
    $.ajax({
      type : 'POST',
      url : "/study_group_invites",
      data : {"name": buttonName, "value": value},
      dataType: "text"
      });

    console.log(button.parentElement);
    console.log(button.parentElement.parentElement);
    // button.parentElement.parentElement.addClass('animateDeleteDiv');
    var parentDiv = button.parentElement.parentElement;
    if(buttonName == 'AcceptButton') {
        parentDiv.style.borderColor = '#4CAF50';
    }
    else {
        parentDiv.style.borderColor = '#AF4C4C';
    }

    var acceptButton = parentDiv.querySelector('button[name="AcceptButton"]');
    var rejectButton = parentDiv.querySelector('button[name="RejectButton"]');

    acceptButton.disabled = true;
    rejectButton.disabled = true;

    $(parentDiv).animate(
        {
            opacity: '0.00'
        },
        {
            easing: 'swing',
            duration: 1000,
            queue: false,
            done: function () {
                parentDiv.remove();
            }
        });
}


$('.notification').on('transitionend', function(e){
    $(e.target).remove()
});

