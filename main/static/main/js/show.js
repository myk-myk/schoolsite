function show(x)
{
    if (x == 2)
    {
        document.getElementById('login1').style.display = 'none';
        document.getElementById('signup1').style.display = 'block';
    }
    else
    {
        document.getElementById('login1').style.display = 'block';
        document.getElementById('signup1').style.display = 'none';
    }
}
show(1);

function save_value()
{
    var name_field = document.getElementById('name_input').value;
    var email_field = document.getElementById('email_input').value;
    var password_field = document.getElementById('password_input').value;
}

