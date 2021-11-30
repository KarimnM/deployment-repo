emailTextBox = document.getElementById("EmailTextBox");
passwordTextBox = document.getElementById("PasswordTextBox");


emailTextBox.addEventListener("keydown", submitFormIfEnterIsPressed);
passwordTextBox.addEventListener("keydown", submitFormIfEnterIsPressed);

function submitFormIfEnterIsPressed(event)
{
    if (event.key === "Enter")
    {
        submitForm();
    }
}

function loginButtonIsClicked()
{
    submitForm();
}

function submitForm()
{
    alert("Hello! You tried to log in!");
    console.log("Password = " + passwordTextBox.value);
    console.log("Email = " + emailTextBox.value);
}
