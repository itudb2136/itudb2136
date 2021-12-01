// initial hide and show
// for manager
if (document.getElementById("role-0").checked)
{
    document.getElementById('teams-fan').style.display = "none";
    document.getElementById('teams-manager').style.display = "block";
}
// for fan
else if (document.getElementById("role-1").checked)
{
    document.getElementById('teams-manager').style.display = "none";
    document.getElementById('teams-fan').style.display = "block";
}

// event listener
// for manager
document.getElementsByClassName("form-radio")[0].addEventListener('change', function() {
    if (document.getElementById("role-0").checked)
    {
        document.getElementById('teams-fan').style.display = "none";
        document.getElementById('teams-manager').style.display = "block";
    }
});

// for fan
document.getElementsByClassName("form-radio")[1].addEventListener('change', function() {
    if (document.getElementById("role-1").checked)
    {
        document.getElementById('teams-manager').style.display = "none";
        document.getElementById('teams-fan').style.display = "block";
    }
});




