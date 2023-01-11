<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title></title>
    </head>
    <body style="font-family: Helvetica, sans-serif; font-size: 12pt; font-color: #222222; overflow-wrap: break-word; -webkit-nbsp-mode: space; line-break: after-white-space;">
        <p>
            {{ data['full_name'] }} |
            {{ data['job_role']}}
            {% if 'unit' in data and data['unit'] %} | {{data['unit']}} {% endif %}
        </p>
        <p >
        <img width="155" height="55" id="Xebia" src="https://assets.oblcc.com/xebia/xebia.png" alt="Xebia" name="Xebia" />
        </p>
        <p>
            <span><a style="color: #222222;" href="https://xebia.com">xebia.com</a> | <a style="color: #222222;" href="email:{{data['email']}}">{{data['email']}}</a> | <a style="color: #222222;" href="tel:{{data['phone'].replace(' ', '')}}">{{data['phone']}}</a></span>
        </p>
    </body>
</html>
